"""Core settings for the app."""

from __future__ import annotations

import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Final

from advanced_alchemy.utils.text import slugify
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.utils.module_loader import module_to_os_path

from pybama_org.__metadata__ import __project__, __version__

if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "pybama_org"
BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)

TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}

__all__ = (
    "AppSettings",
    "LogSettings",
    "ServerSettings",
    "Settings",
    "ViteSettings",
    "get_settings",
    "BASE_DIR",
    "DEFAULT_MODULE_NAME",
)


@dataclass
class ViteSettings:
    """Server configurations."""

    DEV_MODE: bool = field(
        default_factory=lambda: os.getenv("VITE_DEV_MODE", "False") in TRUE_VALUES,
    )
    """Start `vite` development server."""
    USE_SERVER_LIFESPAN: bool = field(
        default_factory=lambda: os.getenv("VITE_USE_SERVER_LIFESPAN", "True") in TRUE_VALUES,
    )
    """Auto start and stop `vite` processes when running in development mode.."""
    HOST: str = field(default_factory=lambda: os.getenv("VITE_HOST", "0.0.0.0"))  # noqa: S104
    """The host the `vite` process will listen on.  Defaults to `0.0.0.0`"""
    PORT: int = field(default_factory=lambda: int(os.getenv("VITE_PORT", "5173")))
    """The port to start vite on.  Default to `5173`"""
    HOT_RELOAD: bool = field(
        default_factory=lambda: os.getenv("VITE_HOT_RELOAD", "True") in TRUE_VALUES,
    )
    """Start `vite` with HMR enabled."""
    ENABLE_REACT_HELPERS: bool = field(
        default_factory=lambda: os.getenv("VITE_ENABLE_REACT_HELPERS", "True") in TRUE_VALUES,
    )
    """Enable React support in HMR."""
    BUNDLE_DIR: Path = field(default_factory=lambda: Path(f"{BASE_DIR}/components/frontend/public"))
    """Bundle directory"""
    RESOURCE_DIR: Path = field(default_factory=lambda: Path("resources"))
    """Resource directory"""
    TEMPLATE_DIR: Path = field(default_factory=lambda: Path(f"{BASE_DIR}/components/frontend/templates"))
    """Template directory."""
    TEMPLATE_ENGINE: type[JinjaTemplateEngine] = JinjaTemplateEngine
    """Template engine to use. (``Jinja2``, ``Mako``, or ``MiniJinja``)"""
    ASSET_URL: str = field(default_factory=lambda: os.getenv("ASSET_URL", "/static/"))
    """Base URL for assets"""

    @property
    def set_static_files(self) -> bool:
        """Serve static assets."""
        return self.ASSET_URL.startswith("/")


@dataclass
class ServerSettings:
    """Server configurations."""

    APP_LOC: str = "pybama_org.app:app"
    """Path to app executable, or factory."""
    APP_LOC_IS_FACTORY: bool = False
    """Indicate if APP_LOC points to an executable or factory."""
    HOST: str = field(default_factory=lambda: os.getenv("LITESTAR_HOST", "0.0.0.0"))  # noqa: S104
    """Server network host."""
    PORT: int = field(default_factory=lambda: int(os.getenv("LITESTAR_PORT", "8000")))
    """Server port."""
    KEEPALIVE: int = field(default_factory=lambda: int(os.getenv("LITESTAR_KEEPALIVE", "65")))
    """Seconds to hold connections open (65 is > AWS lb idle timeout)."""
    RELOAD: bool = field(
        default_factory=lambda: os.getenv("LITESTAR_RELOAD", "False") in TRUE_VALUES,
    )
    """Turn on hot reloading."""
    RELOAD_DIRS: list[str] = field(default_factory=lambda: [f"{BASE_DIR}"])
    """Directories to watch for reloading."""
    HTTP_WORKERS: int | None = field(
        default_factory=lambda: int(os.getenv("WEB_CONCURRENCY")) if os.getenv("WEB_CONCURRENCY") is not None else None,  # type: ignore[arg-type]
    )
    """Number of HTTP Worker processes to be spawned by Uvicorn."""


@dataclass
class LogSettings:
    """Logger configuration."""

    # https://stackoverflow.com/a/1845097/6560549
    EXCLUDE_PATHS: str = r"\A(?!x)x"
    """Regex to exclude paths from logging."""
    HTTP_EVENT: str = "HTTP"
    """Log event name for logs from Litestar handlers."""
    INCLUDE_COMPRESSED_BODY: bool = False
    """Include 'body' of compressed responses in log output."""
    LEVEL: int = field(default_factory=lambda: int(os.getenv("LOG_LEVEL", "10")))
    """Stdlib log levels.

    Only emit logs at this level, or higher.
    """
    OBFUSCATE_COOKIES: set[str] = field(default_factory=lambda: {"session"})
    """Request cookie keys to obfuscate."""
    OBFUSCATE_HEADERS: set[str] = field(default_factory=lambda: {"Authorization", "X-API-KEY"})
    """Request header keys to obfuscate."""
    REQUEST_FIELDS: list[RequestExtractorField] = field(
        default_factory=lambda: [
            "path",
            "method",
            "headers",
            "cookies",
            "query",
            "path_params",
            "body",
        ],
    )
    """Attributes of the [Request][litestar.connection.request.Request] to be
    logged."""
    RESPONSE_FIELDS: list[ResponseExtractorField] = field(
        default_factory=lambda: [
            "status_code",
            "cookies",
            "headers",
            "body",
        ],
    )
    """Attributes of the [Response][litestar.response.Response] to be
    logged."""
    GRANIAN_ACCESS_LEVEL: int = 30
    """Level to log granian access logs."""
    GRANIAN_ERROR_LEVEL: int = 20
    """Level to log granian error logs."""


@dataclass
class AppSettings:
    """Application configuration."""

    URL: str = field(default_factory=lambda: os.getenv("APP_URL", "http://localhost:8000"))
    """The frontend base URL"""
    DEBUG: bool = field(default_factory=lambda: os.getenv("LITESTAR_DEBUG", "False") in TRUE_VALUES)
    """Run `Litestar` with `debug=True`."""
    SECRET_KEY: str = field(
        default_factory=lambda: os.getenv("SECRET_KEY", binascii.hexlify(os.urandom(32)).decode(encoding="utf-8")),
    )
    """Application secret key."""
    NAME: str = field(default_factory=lambda: "app")
    """Application name."""
    ALLOWED_CORS_ORIGINS: list[str] | str = field(default_factory=lambda: os.getenv("ALLOWED_CORS_ORIGINS", '["*"]'))
    """Allowed CORS Origins"""
    CSRF_COOKIE_NAME: str = field(default_factory=lambda: "csrftoken")
    """CSRF Cookie Name"""
    CSRF_COOKIE_SECURE: bool = field(default_factory=lambda: False)
    """CSRF Secure Cookie"""
    JWT_ENCRYPTION_ALGORITHM: str = field(default_factory=lambda: "HS256")
    """JWT Encryption Algorithm"""

    @property
    def slug(self) -> str:
        """Return a slugified name.

        Returns:
            `self.NAME`, all lowercase and hyphens instead of spaces.
        """
        return slugify(self.NAME)

    def __post_init__(self) -> None:
        """Post initialization checks."""
        # Check if the ALLOWED_CORS_ORIGINS is a string.
        if isinstance(self.ALLOWED_CORS_ORIGINS, str):
            # Check if the string starts with "[" and ends with "]", indicating a list.
            if self.ALLOWED_CORS_ORIGINS.startswith("[") and self.ALLOWED_CORS_ORIGINS.endswith("]"):
                try:
                    # Safely evaluate the string as a Python list.
                    self.ALLOWED_CORS_ORIGINS = json.loads(self.ALLOWED_CORS_ORIGINS)
                except (SyntaxError, ValueError):
                    # Handle potential errors if the string is not a valid Python literal.
                    msg = "ALLOWED_CORS_ORIGINS is not a valid list representation."
                    raise ValueError(msg) from None
            else:
                # Split the string by commas into a list if it is not meant to be a list representation.
                self.ALLOWED_CORS_ORIGINS = [host.strip() for host in self.ALLOWED_CORS_ORIGINS.split(",")]


@dataclass
class OpenAPISettings:
    """OpenAPI configuration."""

    TITLE: str = "API for the PyBama web service"
    """OpenAPI Title"""
    VERSION: str = __version__
    """OpenAPI Version"""
    PATH: str = "/api"
    """OpenAPI Path"""
    CONTACT_NAME: str = "Jacob Coffee"
    """OpenAPI Contact Name"""
    CONTACT_EMAIL: str = "hello@pybama.org"
    """OpenAPI Contact Email"""
    DESCRIPTION: str | None = f"""This API provides a list of stores and their associated information based on the
                                      OpenAPI 3.1 specification. You can find out more about this project in the
                                      [docs]({os.getenv("APP_URL", "http://0.0.0.0/") + "docs"}).
                                        This project is maintained by the [PyBama organization](https://github.com/PyBama)."""
    SERVERS: list[dict[str, str]] = field(default_factory=list)
    """Servers to use for the OpenAPI documentation."""
    EXTERNAL_DOCS: dict[str, str] | None = field(
        default_factory=lambda: {
            "description": f"{__project__} Docs",
            "url": os.getenv("APP_URL", "http://0.0.0.0/") + "/docs",
        }
    )

    def __post_init__(self) -> None:
        """This is called after the dataclass is initialized.

        Check if the ``SERVERS`` is a :class:`str` or a :class:`list`.
        """
        self.assemble_openapi_servers()

    def assemble_openapi_servers(self) -> None:
        """Assemble OpenAPI servers based on environment."""
        environment = os.getenv("APP_ENVIRONMENT") or "dev"
        port = os.getenv("APP_PORT") or "8000"

        if environment == "prod":
            self.SERVERS = [
                {
                    "url": os.getenv("APP_URL", "https://www.pybama.org/api"),
                    "description": "Production Server",
                },
            ]
        elif environment == "dev":
            self.SERVERS = [{"url": f"http://0.0.0.0:{port}/", "description": "Development Server"}]


@dataclass
class Settings:
    """Class to hold all settings."""

    app: AppSettings = field(default_factory=AppSettings)
    vite: ViteSettings = field(default_factory=ViteSettings)
    server: ServerSettings = field(default_factory=ServerSettings)
    log: LogSettings = field(default_factory=LogSettings)
    openapi: OpenAPISettings = field(default_factory=OpenAPISettings)

    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> Settings:
        """Load settings from environment variables."""
        from litestar.cli._utils import console

        env_file = Path(f"{os.curdir}/{dotenv_filename}")
        if env_file.is_file():
            from dotenv import load_dotenv

            console.print(f"[yellow]Loading environment configuration from {dotenv_filename}[/]")

            load_dotenv(env_file)
        return Settings()


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    """Helper function to get settings."""
    return Settings.from_env()
