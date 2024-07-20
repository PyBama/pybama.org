"""Entrypoint for the application."""

from __future__ import annotations

from typing import TYPE_CHECKING

__all__ = ("create_app",)


if TYPE_CHECKING:
    from litestar import Litestar


def create_app() -> Litestar:
    """Create ASGI application."""
    from litestar import Litestar

    from pybama_org.config import core, routers
    from pybama_org.config.settings import get_settings

    settings = get_settings()

    return Litestar(
        cors_config=core.cors_config,
        debug=settings.app.DEBUG,
        openapi_config=core.openapi_config,
        route_handlers=routers.route_handlers,
        plugins=[
            core.structlog_plugin,
            core.vite_plugin,
            core.granian_plugin,
        ],
    )


app = create_app()
