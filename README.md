# gns3-client
GNS3 client


gns3_client/
├── gns3_client/
│   ├── __init__.py
│   ├── client/             # This folder will hold the generated API client code.
│   │   └── ...             # (generated files)
│   ├── cli.py              # CLI integration with Click.
│   └── wrapper.py          # Optional: Custom wrapper functions/classes for the API.
├── scripts/
│   └── generate_client.sh  # Script to regenerate client code.
├── tests/
│   └── test_cli.py         # Tests for your CLI and/or wrapper.
├── pyproject.toml          # Managed by Poetry.
└── README.md


gns3_client/
├── gns3_client/            # Main package folder
│   ├── __init__.py
│   ├── client/             # Directory for generated code
│   │   ├── __init__.py
│   │   ├── api/            # API endpoint modules (auto-generated)
│   │   ├── models/         # Data models (auto-generated)
│   │   ├── rest.py         # HTTP session handling (auto-generated)
│   │   └── ...             # Other generated modules
│   ├── cli.py              # Optional: Command-line interface wrapper
│   └── utils.py            # Optional: Helper functions or additional features
├── scripts/
│   └── generate_client.sh  # Script to re-generate the client code from the API spec
├── tests/                  # Unit and integration tests for your library
│   └── test_basic.py
├── setup.py                # Packaging file (or use pyproject.toml with Poetry/Flit)
├── requirements.txt        # Library dependencies
└── README.md               # Project documentation

gns3-client/                   # Root directory of your project
├── .github/                   # GitHub-specific files (CI/CD workflows)
│   └── workflows/
│       └── ci.yml             # GitHub Actions configuration for CI/CD
├── conf/                      # Optional configuration files (e.g., YAML/JSON config for client defaults)
├── docs/                      # Documentation (Sphinx docs, markdown files, etc.)
├── gns3client/                # Main Python package (similar to gns3server/ in GNS3)
│   ├── __init__.py
│   ├── cli.py                 # CLI integration using Click (entry point for users)
│   ├── wrapper.py             # Custom wrapper functions/classes to simplify API usage
│   └── client/                # Directory for the auto-generated client code from OpenAPI
│       ├── __init__.py
│       ├── api/               # Generated API endpoint modules
│       ├── models/            # Generated data models
│       └── rest.py            # Generated HTTP session handling and utility code
├── scripts/                   # Scripts to manage automation tasks
│   └── generate_client.sh     # Script to remove the old client/ folder and regenerate the client code using OpenAPI Generator
├── tests/                     # Test suite (unit tests, integration tests, CLI tests)
│   └── test_cli.py            # Example test for your CLI wrapper
├── Dockerfile                 # (Optional) Dockerfile for containerized testing or deployment
├── CHANGELOG.md               # Changelog to document API changes and your wrapper adjustments
├── CONTRIBUTING.md            # Guidelines for contributions
├── LICENSE                    # License file (e.g., GPL-3.0)
├── MANIFEST.in                # Manifest file to include non-code files in your package
├── README.md                  # Project overview, installation instructions, usage, etc.
└── pyproject.toml             # Poetry configuration file (manages dependencies, version, entry points, etc.)
