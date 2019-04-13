import base64


class Submission:
    # These 3 should always be bytestrings interally
    source_code = None
    stdin = None
    expected_output = None

    # The language ID
    language_id = None

    # Extra Send Fields
    cpu_time_limit = None
    cpu_extra_time = None
    wall_time_limit = None
    memory_limit = None
    stack_limit = None
    max_processes_and_or_threads = None
    enable_per_process_and_thread_time_limit = None
    enable_per_process_and_thread_memory_limit = None
    max_file_size = None
    number_of_runs = None

    # These 3 should always be bytestrings interally
    compile_output = None
    stdout = None
    stderr = None

    # Receive Fields
    message = None
    exit_code = None
    exit_signal = None
    status = None
    created_at = None
    finished_at = None
    token = None
    time = None
    wall_time = None
    memory = None

    # Please excuse the mess - this simply helps getting the correct fields easier
    _encoded_send_fields = {"source_code", "stdin", "expected_output"}
    _encoded_response_fields = {"stderr", "stdout", "compile_output"}
    _encoded_fields = _encoded_send_fields | _encoded_response_fields
    _extra_send_fields = {"cpu_time_limit", "cpu_extra_time", "wall_time_limit", "memory_limit", "stack_limit", "max_processes_and_or_threads", "enable_per_process_and_thread_time_limit", "enable_per_process_and_thread_memory_limit", "max_file_size", "number_of_runs"}
    _extra_response_fields = {"time", "memory", "token", "message", "status", "exit_code", "exit_signal", "created_at", "finished_at", "wall_time"}
    _response_fields = _encoded_response_fields | _extra_response_fields | {"language_id"}
    _send_fields = _encoded_send_fields | _extra_send_fields
    _fields = _response_fields | _send_fields

    def keys(self):
        return list(self._fields)

    def __getitem__(self, item):
        if item in self._encoded_fields:
            # If this does not work, then at some point the data has not been set as bytes internally
            item = getattr(self, item)
            if item:
                return item.decode()
            return None

        return getattr(self, item)

    def load(self, client):
        headers = {"Content-Type": "application/json"}
        params = {
            "base64_encoded": "true",
            # The fields parameter of judge0 expects a comma separated string rather than a HTML spec param list
            "fields": ",".join(self._response_fields)
        }
        r = client.session.get(f"{client.endpoint}/submissions/{self.token}/", headers=headers, params=params)
        r.raise_for_status()
        self.set_properties(r)

    def submit(self, client):
        headers = {"Content-Type": "application/json"}
        params = {"base64_encoded": "true", "wait": str(client.wait).lower()}
        language_id = self.language_id

        data = {
            "source_code": base64.b64encode(self.source_code).decode('ascii'),
            "language_id": language_id,
        }
        if self.stdin:
            data.update({"stdin": base64.b64encode(self.stdin).decode('ascii')})
        if self.expected_output:
            data.update({"expected_output": base64.b64encode(self.expected_output).decode('ascii')})

        r = client.session.post(f"{client.endpoint}/submissions/", headers=headers, params=params, json=data)
        r.raise_for_status()

        self.set_properties(r)

    def set_properties(self, r):
        json = r.json()
        for key in json.keys():
            if key in self._encoded_fields:
                # TODO: make nicer
                setattr(self, key, base64.b64decode(json[key].encode()) if json[key] else None)
            else:
                setattr(self, key, json[key])


def get(client, submission_token):
    submission = Submission()
    submission.token = submission_token
    submission.load(client)
    return submission


def submit(client, source_code, language, stdin=None, expected_output=None):
    """
    Creates and submits
    :param client: the judge0 client object
    :param source_code: a byte-string of the source code
    :param language: the language ID for this program
    :param stdin: a byte-string of the input for this program
    :param expected_output: a byte-string of the expected output
    :return:
    """
    submission = Submission()
    submission.source_code = source_code
    submission.language_id = language
    submission.stdin = stdin
    submission.expected_output = expected_output
    submission.submit(client)
    return submission
