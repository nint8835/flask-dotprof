import nox
import nox.sessions

PACKAGE_NAME = "flask_dotprof"
PACKAGE_FILES = [PACKAGE_NAME, "noxfile.py"]


@nox.session(python="3.8")
def lint(session: nox.sessions.Session) -> None:
    session.install(
        "flake8==3.8.3",
        "flake8-isort==3.0.1",
        "black==19.10b0",
        "mypy==0.782",
        "isort==4.3.21",
    )
    session.run("flake8", *PACKAGE_FILES)
    session.run("black", "--check", *PACKAGE_FILES)


@nox.session(python="3.8")
def typecheck(session: nox.sessions.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("mypy==0.782")
    session.run("mypy", PACKAGE_NAME)


@nox.session(python="3.8")
def format(session: nox.sessions.Session) -> None:
    session.install("black==19.10b0", "isort==4.3.21")
    session.run("isort", "--recursive", *PACKAGE_FILES)
    session.run("black", *PACKAGE_FILES)
