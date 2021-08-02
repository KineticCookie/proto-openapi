import glob
import pathlib

import pkg_resources
from grpc_tools.protoc import main as protoc


def to_absolute(path: str) -> str:
    return str(pathlib.Path(path).resolve())


def compile_descriptors(proto_path, output):
    files = [
        to_absolute(x)
        for x in glob.glob(f"{proto_path}/**/*.proto", recursive=True)
    ]
    proto_include = pkg_resources.resource_filename("grpc_tools", "_proto")
    args = [
        __file__,
        f"--proto_path={proto_path}",
        f"--proto_path={proto_include}",
        "--include_imports",
        "--include_source_info",
        f"--descriptor_set_out={output}",
    ] + files
    result = protoc(args)
    assert not result, "protoc failed"
    return output
