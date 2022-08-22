def test_import() -> None:
    import cookie_sandbox

    assert cookie_sandbox
    assert cookie_sandbox.version


def test_bad() -> None:
    assert 1 == 2
