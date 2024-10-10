import pytest

from mite_schema.main import main


def test_no_attrs(monkeypatch):
    monkeypatch.setattr("sys.argv", ["mite-schema"])
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 2


def test_cli_single_valid(monkeypatch):
    monkeypatch.setattr(
        "sys.argv", ["mite-schema", "-i", "tests/example_files/example_valid.json"]
    )
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 0


def test_cli_multi_valid(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "mite-schema",
            "-i",
            "tests/example_files/example_valid.json",
            "tests/example_files/example_valid.json",
        ],
    )
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 0


def test_cli_single_invalid(monkeypatch):
    monkeypatch.setattr(
        "sys.argv", ["mite-schema", "-i", "tests/example_files/example_invalid.json"]
    )
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 1


def test_cli_multi_invalid(monkeypatch):
    monkeypatch.setattr(
        "sys.argv", ["mite-schema", "-i", "tests/example_files/example_invalid.json"]
    )
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 1
