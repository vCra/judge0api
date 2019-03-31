import requests


class Client:
    auth_token = None
    auth_user = None
    session = None
    endpoint = None
    wait = True

    def __init__(self, endpoint, auth_token=None, auth_user=None):
        self.endpoint = endpoint
        self.auth_token = auth_token
        self.auth_user = auth_user
        self.session = requests.session()
        self._login()

    def _login(self):
        if self.auth_user:
            self._authorize()
        if self.auth_token:
            self._authenticate()

    def _authenticate(self):
        header = {"X-Auth-Token": self.auth_token}
        r = requests.post(f"{self.endpoint}/authenticate", params=header)
        r.raise_for_status()
        self.session.headers.update(header)

    def _authorize(self):
        header = {"X-Auth-User": self.auth_user}
        r = requests.post(f"{self.endpoint}/authorize", params=header)
        r.raise_for_status()
        self.session.headers.update(header)
