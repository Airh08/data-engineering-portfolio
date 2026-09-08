import os
import sys


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path = [path for path in sys.path if os.path.abspath(path or ".") != SCRIPT_DIRECTORY]

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Validated application configuration kept separate from application code."""

    environment: str
    port: int
    database_url: str
    debug: bool


def require_variable(name: str, environment: Mapping[str, str]) -> str:
    """Return a required variable or raise a clear configuration error."""
    value = environment.get(name)
    if not value:
        raise ValueError(f"Required environment variable is missing: {name}")
    return value


def parse_bool(value: str, name: str) -> bool:
    """Convert common environment strings to bool and reject invalid values."""
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"Invalid boolean value for {name}: {value}")


def load_config(environment: Mapping[str, str] | None = None) -> AppConfig:
    """Load, default, and validate configuration from environment variables."""
    source = os.environ if environment is None else environment
    app_environment = source.get("APP_ENV", "development")
    raw_port = source.get("PORT", "8000")
    database_url = require_variable("DATABASE_URL", source)
    debug = parse_bool(source.get("DEBUG", "false"), "DEBUG")

    if app_environment not in {"development", "testing", "production"}:
        raise ValueError(f"Invalid APP_ENV: {app_environment}")

    try:
        port = int(raw_port)
    except ValueError as error:
        raise ValueError(f"PORT must be an integer: {raw_port}") from error

    if not 1 <= port <= 65_535:
        raise ValueError(f"PORT must be between 1 and 65535: {port}")

    return AppConfig(
        environment=app_environment,
        port=port,
        database_url=database_url,
        debug=debug,
    )


def optional_log_level() -> str:
    """Read an optional value directly with os.getenv and provide a default."""
    return os.getenv("LOG_LEVEL", "INFO")


def application_startup(config: AppConfig) -> str:
    """Use validated configuration in application code."""
    mode = "debug" if config.debug else "normal"
    return f"Starting {config.environment} application on port {config.port} ({mode})"


def dotenv_concept() -> str:
    """Explain the .env workflow without loading a file or requiring a package."""
    return (
        "A .env file can define APP_ENV, PORT, and DATABASE_URL locally; "
        "a dotenv loader copies them into os.environ before startup."
    )


def main() -> None:
    """Demonstrate defaults, required values, validation, and configuration use."""
    example_environment = {
        "APP_ENV": "testing",
        "DATABASE_URL": "postgresql://localhost/portfolio",
        "DEBUG": "true",
    }
    config = load_config(example_environment)

    print(f"Configuration: {config}")
    print(f"Default PORT: {config.port}")
    print(f"Optional LOG_LEVEL with getenv: {optional_log_level()}")
    print(application_startup(config))
    print(f"os.environ is available: {isinstance(os.environ, Mapping)}")
    print(f".env concept: {dotenv_concept()}")

    try:
        load_config({"PORT": "not-a-number"})
    except ValueError as error:
        print(f"Required variable error: {error}")

    try:
        load_config({"DATABASE_URL": "sqlite:///test.db", "PORT": "not-a-number"})
    except ValueError as error:
        print(f"Validation error: {error}")


if __name__ == "__main__":
    main()