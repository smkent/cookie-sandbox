def test_import() -> None:
    import cookie_sandbox

    assert cookie_sandbox
    assert cookie_sandbox.version


def test_bad() -> None:
    assert 1 == 2


def test_good() -> None:
    assert "OK"


def test_also_bad() -> None:
    assert True is False
