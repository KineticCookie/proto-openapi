import pathlib

from google.protobuf.descriptor_pb2 import FileDescriptorSet
import pytest

from proto_openapi.compiler import compile_descriptors


def to_absolute(path: str) -> str:
    return str(pathlib.Path(path).resolve())


@pytest.fixture()
def f_proto_path():
    return to_absolute("../protos/src/")


@pytest.fixture()
def f_descriptor():
    with open("./tests/data/descriptor", "rb") as f:
        str = f.read()
        desc = FileDescriptorSet.FromString(str)
    return desc


def test_compilation(f_proto_path):
    result = compile_descriptors(f_proto_path, "tests/data/test_desc.pb")
    print(result)
    assert False


def test_descriptor(f_descriptor):
    print(f_descriptor)
