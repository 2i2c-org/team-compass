import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", ".", "_build/html"]


@nox.session
def docs(session):
    """Build the documentation. Use `-- live` to build documentation with a
    live server to preview changes."""
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        session.posargs.pop(session.posargs.index("live"))
        session.install("sphinx-autobuild")
        AUTOBUILD_IGNORE = [
            "_build",
            "build_assets",
            "tmp",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
    else:
        cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)
