# Thanos PyLib

A simple "Hello World" Python library that demonstrates how to package and distribute Python code as compiled bytecode (wheel distribution) to prevent source code from being exposed publicly.

## Features

- Simple hello world functionality
- Distributed as wheel-only package (source code not exposed)
- Easy to install via pip

## Installation

```bash
pip install thanos-pylib
```

## Usage

```python
from thanos_pylib import hello_world, greet

# Get a hello world message
message = hello_world()
print(message)  # Output: Hello, World from Thanos PyLib!

# Get a personalized greeting
greeting = greet("Alice")
print(greeting)  # Output: Hello, Alice! Welcome to Thanos PyLib!
```

## Building the Package

This library is built as a standard wheel distribution.

### Prerequisites

```bash
pip install build twine
```

### Build the Wheel

```bash
# Build wheel distribution
python -m build --wheel
```

This creates a `.whl` file in the `dist/` directory.

**Note on Source Code**: By default, Python wheels contain the source `.py` files. When users install the package, Python compiles these to `.pyc` bytecode on their system. If you need stronger code protection, see the "Security Note" section above.

## Publishing to PyPI

### Option 1: Publishing to Test PyPI (Recommended for Testing)

1. Create an account on [Test PyPI](https://test.pypi.org/account/register/)

2. Generate an API token:
   - Go to [Test PyPI Account Settings](https://test.pypi.org/manage/account/)
   - Scroll to "API tokens" section
   - Click "Add API token"
   - Set token name and scope
   - Copy the token (starts with `pypi-`)

3. Upload to Test PyPI:
   ```bash
   python -m twine upload --repository testpypi dist/*.whl
   ```
   
   When prompted:
   - Username: `__token__`
   - Password: Your API token (including the `pypi-` prefix)

4. Test installation from Test PyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ thanos-pylib
   ```

### Option 2: Publishing to Production PyPI

1. Create an account on [PyPI](https://pypi.org/account/register/)

2. Generate an API token:
   - Go to [PyPI Account Settings](https://pypi.org/manage/account/)
   - Scroll to "API tokens" section
   - Click "Add API token"
   - Set token name and scope
   - Copy the token (starts with `pypi-`)

3. Upload to PyPI:
   ```bash
   python -m twine upload dist/*.whl
   ```
   
   When prompted:
   - Username: `__token__`
   - Password: Your API token (including the `pypi-` prefix)

4. Install from PyPI:
   ```bash
   pip install thanos-pylib
   ```

### Using .pypirc Configuration (Optional)

To avoid entering credentials each time, create a `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YourProductionAPIToken

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YourTestAPIToken
```

Then upload with:
```bash
# To Test PyPI
python -m twine upload --repository testpypi dist/*.whl

# To Production PyPI
python -m twine upload dist/*.whl
```

## Security Note: Source Code Protection

By default, Python wheels (.whl files) contain source code (.py files). When users install the package, Python automatically compiles it to bytecode (.pyc files) on their system.

### Understanding Code Visibility:

**Standard Wheel Distribution:**
- Contains `.py` source files
- Source code is visible to anyone who installs the package
- This is the standard Python packaging approach

**Bytecode Protection:**
- Python bytecode (.pyc) can be decompiled back to source code
- Tools like `uncompyle6` or `decompyle3` can reverse bytecode to Python source
- Bytecode is NOT strong protection for sensitive algorithms

### Options for Code Protection:

1. **Accept Standard Distribution (Recommended for Most Cases)**
   - Most Python packages distribute source code
   - Focus on protecting API keys and credentials, not code logic
   - Use proper licensing to protect intellectual property

2. **Compiled Extensions**
   - Move sensitive algorithms to C/C++ extensions
   - Compile to native machine code (.so/.dll files)
   - Much harder to reverse engineer than Python bytecode

3. **Code Obfuscation Tools**
   - Use tools like PyArmor for code obfuscation
   - Provides better (but not perfect) protection
   - May impact performance and debugging

4. **SaaS Model**
   - Keep proprietary code on your servers
   - Expose functionality through APIs
   - Users never see the implementation

### Why Use Wheels?

Even though wheels contain source code, they are still preferred because:
- Faster installation (pre-built, no compilation needed)
- Better dependency management
- Consistent across platforms
- Standard Python packaging format

## Development

### Project Structure

```
thanos-pylib/
├── src/
│   └── thanos_pylib/
│       └── __init__.py       # Main library code
├── pyproject.toml             # Project configuration
├── setup.py                   # Build configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

### Local Development

```bash
# Clone the repository
git clone https://github.com/PankajMoolrajani/thanos-pylib.git
cd thanos-pylib

# Install in editable mode
pip install -e .

# Test the library
python -c "from thanos_pylib import hello_world; print(hello_world())"
```

## Version History

- **0.1.0** - Initial release with hello world functionality

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.