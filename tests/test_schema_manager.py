import pytest

from mite_schema.schema_manager.schema_manager import SchemaManager


@pytest.fixture
def manager():
    return SchemaManager()


def test_read_json_valid(manager):
    outdict = manager.read_json("tests/example_files/example_valid.json")
    assert isinstance(outdict, dict)


def test_read_json_invalid_0(manager):
    with pytest.raises(FileNotFoundError):
        manager.read_json("tests/example_files/asdfghjk")


def test_read_json_invalid_1(manager):
    with pytest.raises(RuntimeError):
        manager.read_json("tests/example_files/example_invalid")


def test_read_json_invalid_2(manager):
    with pytest.raises(RuntimeError):
        manager.read_json("tests/example_files/example_empty.json")


def test_validate_mite_valid(manager):
    outdict = manager.read_json("tests/example_files/example_valid.json")
    assert manager.validate_mite(instance=outdict) is None


def test_validate_mite_invalid(manager):
    outdict = manager.read_json("tests/example_files/example_invalid.json")
    with pytest.raises(ValueError):
        manager.validate_mite(instance=outdict)
