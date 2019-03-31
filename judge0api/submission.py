import base64


class Submission:
    source_code = None
    language_id = None
    stdin = None
    expected_output = None
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
    stdout = None
    stderr = None
    compile_output = None
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

    def load(self, client):
        headers = {"Content-Type": "application/json"}
        r = client.session.get(f"{client.endpoint}/submissions/{self.token}/", headers=headers)
        r.raise_for_status()
        json = r.json()
        print(json)
        for key in json.keys():
            setattr(self, key, json[key])

    def submit(self, client):
        headers = {"Content-Type": "application/json"}
        params = {"base64_encoded": "true", "wait": str(client.wait).lower()}
        language_id = self.language_id

        data = {
            "source_code": base64.b64encode(self.source_code).decode('ascii'),
            "language_id": language_id,
        }
        if self.stdin:
            data.update({"stdin": base64.b64encode(self.stdin.encode()).decode('ascii')})
        if self.expected_output:
            data.update({"expected_output": base64.b64encode(self.expected_output.encode()).decode('ascii')})
        print(data)

        r = client.session.post(f"{client.endpoint}/submissions/", headers=headers, params=params, json=data)
        print(r.url)
        r.raise_for_status()

        json = r.json()
        print(json)
        for key in json.keys():
            setattr(self, key, json[key])


def get(client, submission_token):
    submission = Submission()
    submission.token = submission_token
    submission.load(client)
    return submission


def submit(client, source_code, language, stdin=None, expected_output=None):
    submission = Submission()
    submission.source_code = source_code.read()
    submission.language_id = language
    submission.stdin = stdin
    submission.expected_output = expected_output
    submission.submit(client)
    return submission
