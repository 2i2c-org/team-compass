import nox
from textwrap import dedent
from shlex import split
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"


@nox.session
def docs(session):
    """Build the documentation."""
    session.install("mystmd")
    session.run("myst", "build", "--html", *session.posargs)


@nox.session(name="docs-live")
def docs_live(session):
    """Build the documentation with live preview server."""
    session.install("mystmd")
    session.run("myst", "start", *session.posargs)

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
    