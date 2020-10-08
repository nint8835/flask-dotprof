import nox
import nox.sessions
import nox_poetry.core

nox_poetry.core.patch()

PACKAGE_NAME = "flask_dotprof"
PACKAGE_FILES = [PACKAGE_NAME, "noxfile.py", "test_app"]


@nox.session(python="3.8")
def lint(session: nox.sessions.Session) -> None:
    session.install(
        "flake8==3.8.4",
        "flake8-isort==4.0.0",
        "black==20.8b1",
        "mypy==0.782",
        "isort==5.6.1",
    )
    session.run("flake8", *PACKAGE_FILES)
    session.run("black", "--check", *PACKAGE_FILES)


@nox.session(python="3.8")
def typecheck(session: nox.sessions.Session) -> None:
    session.install(".")
    session.install("mypy==0.782")
    session.run("mypy", PACKAGE_NAME)


@nox.session(python="3.8")
def format(session: nox.sessions.Session) -> None:
    session.install("black==20.8b1", "isort==5.6.1")
    session.run("isort", *PACKAGE_FILES)
    session.run("black", *PACKAGE_FILES)
