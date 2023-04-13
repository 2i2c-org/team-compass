import nox
from textwrap import dedent
from shlex import split
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "dirhtml", ".", "_build/dirhtml"]


@nox.session
def docs(session):
    """Build the documentation. Use `-- live` for a live server to preview changes."""
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        session.posargs.pop(session.posargs.index("live"))
        session.install("sphinx-autobuild")
        # Add folders to ignore
        AUTOBUILD_IGNORE = [
            "_build",
            "build_assets",
            "tmp",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])

        # Find an open port to serve
        cmd.extend(["--port", "0"])
    else:
        cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)

@nox.session
def images(session):
    """Optimize images using oxipng. Note you must install oxipng on your own first."""
    # Command taken from https://github.com/shssoichiro/oxipng#usage
    # Use the external environment since we assume oxipng is installed on its own.
    try:
        images = Path("images").rglob("**/*.png")
        for img in images:
            session.run(*split(f"oxipng -o 4 -i 0 --strip safe --recursive {img}"), external=True)
    except Exception:
        msg = dedent(f"""
        Could not run oxipng, double-check that it is installed properly.
        See https://github.com/shssoichiro/oxipng#installing.
        """)
        print(msg)
    