# Sample Test passing with nose and pytest


def test_pass():
    assert True, "dummy sample test"


def test_homepage_example():
    import judge0api as api
    import time

    client = api.Client("https://api.judge0.com")
    client.wait = False

    submission = api.submission.submit(
        client,
        b"print(f'Hello {input()}')",
        71,
        stdin=b'Judge0',
        expected_output=b"Hello Judge0"
    )
    time.sleep(2)
    submission.load(client)

    assert submission.status['id'] == api.Judge0Status.ACCEPTED.value
