from setuptools import setup, find_packages

setup(
    name="mcp-vehicle-search",
    version="0.1.0",
    description="MCP Vehicle Search System - Intelligent vehicle search with LangChain and OpenAI",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastmcp>=0.1.0",
        "langchain>=0.1.0",
        "openai>=1.0.0",
        "pydantic>=2.0.0",
        "rich>=13.0.0",
        "tabulate>=0.9.0",
        "pytest>=7.0.0",
        "pytest-asyncio>=0.21.0",
    ],
    extras_require={
        "dev": [
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "mcp-vehicle-server=server.interface.mcp_server:main",
            "mcp-vehicle-client=client.interface.agent_runner:main",
        ],
    },
)