import requests


class Client:
    """
    A judge0api Client

    Stores Endpoint information, as well as auth tokens, as well as submission wait preferences

    The constructor handles most things - if you don't want this client to wait for submissions, then set wait to False
    """
    auth_token = None
    auth_user = None
    session = None
    endpoint = None
    wait = True

    def __init__(self, endpoint, auth_token=None, auth_user=None):
        """
        Creates an instance of a judge0api Client
        :param endpoint: The "Endpoint" server - this is normally a domain, with a scheme. e.g. https://api.judge0.com/
        :param auth_token: An optional auth_token - this is normally not needed
        :param auth_user: An optional auth_user - this is normally not needed
        """
        self.endpoint = endpoint
        self.auth_token = auth_token
        self.auth_user = auth_user
        self.session = requests.session()
        self._login()

    def _login(self):
        """
        If this session has any auth tokens, ensure that they are valid.
        :return:
        """
        if self.auth_user:
            self._authorize()
        if self.auth_token:
            self._authenticate()

    def _authenticate(self):
        """
        Authenticate the auth_token against this clients endpoint
        :raises HTTPException if token is invalid
        """
        header = {"X-Auth-Token": self.auth_token}
        r = requests.post(f"{self.endpoint}/authenticate", params=header)
        r.raise_for_status()
        self.session.headers.update(header)

    def _authorize(self):
        """
        Authorize the auth_user against this clients endpoint
        :raises HTTPException if token is invalid
        """
        header = {"X-Auth-User": self.auth_user}
        r = requests.post(f"{self.endpoint}/authorize", params=header)
        r.raise_for_status()
        self.session.headers.update(header)
