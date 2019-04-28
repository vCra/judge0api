# Sample Test passing with nose and pytest


def test_pass():
    assert True, "dummy sample test"


def test_homepage_example():
    import judge0api as api
    client = api.Client("https://api.judge0.com")
    submission = api.submission.submit(
        client,
        b"print(f'Hello {input()}')",
        34,
        stdin=b'Judge0',
        expected_output=b"Hello Judge0"
    )
    assert submission.status['id'] == 3
