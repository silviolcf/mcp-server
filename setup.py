from setuptools import setup, find_packages

setup(
    name="mcp_server",
    version=0.1,
    packages=find_packages(where="server"),
    package_dir={"": "server"}
)