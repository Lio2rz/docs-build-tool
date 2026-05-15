"""Entry point for ``python -m docsbuildtool``.

Invokes the main CLI application and exits with code 0 on success.
"""

import sys

if __name__ == "__main__":
    from docsbuildtool.cli import main

    main()
    sys.exit(0)
