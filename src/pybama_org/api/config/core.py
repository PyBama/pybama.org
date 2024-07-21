"""Configs and plugins settings."""

import logging
from typing import cast

from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.config.csrf import CSRFConfig
from litestar.logging.config import LoggingConfig, StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin
from litestar.openapi.spec import Contact
from litestar.plugins.structlog import StructlogConfig, StructlogPlugin
from litestar.template.config import TemplateConfig
from litestar_granian import GranianPlugin
from litestar_vite import ViteConfig, VitePlugin

from pybama_org.api.config.settings import get_settings
from pybama_org.api.utils import set_base_path

settings = get_settings()

# --- Configs
compression_config = CompressionConfig(backend="gzip")
csrf_config = CSRFConfig(
    secret=settings.app.SECRET_KEY,
    cookie_secure=settings.app.CSRF_COOKIE_SECURE,
    cookie_name=settings.app.CSRF_COOKIE_NAME,
)
cors_config = CORSConfig(allow_origins=cast("list[str]", settings.app.ALLOWED_CORS_ORIGINS))
template = TemplateConfig(  # type: ignore[var-annotated]
    directory=settings.vite.TEMPLATE_DIR,
    engine=settings.vite.TEMPLATE_ENGINE,
    engine_callback=set_base_path,
)
"""Template config. See :class:`TemplateSettings <.settings.TemplateSettings>` for configuration."""
vite_config = ViteConfig(
    bundle_dir=settings.vite.BUNDLE_DIR,
    resource_dir=settings.vite.RESOURCE_DIR,
    template_dir=settings.vite.TEMPLATE_DIR,
    use_server_lifespan=settings.vite.USE_SERVER_LIFESPAN,
    dev_mode=settings.vite.DEV_MODE,
    hot_reload=settings.vite.HOT_RELOAD,
    is_react=settings.vite.ENABLE_REACT_HELPERS,
    port=settings.vite.PORT,
    host=settings.vite.HOST,
)
log_config = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="always",
        standard_lib_logging_config=LoggingConfig(
            root={"level": logging.getLevelName(settings.log.LEVEL), "handlers": ["queue_listener"]},
            loggers={
                "granian.access": {
                    "propagate": False,
                    "level": settings.log.GRANIAN_ACCESS_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "granian.error": {
                    "propagate": False,
                    "level": settings.log.GRANIAN_ERROR_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
    middleware_logging_config=LoggingMiddlewareConfig(
        request_log_fields=["method", "path", "path_params", "query"],
        response_log_fields=["status_code"],
    ),
)
openapi_config = OpenAPIConfig(
    title=settings.openapi.TITLE or settings.app.NAME,
    version=settings.openapi.VERSION,
    contact=Contact(name=settings.openapi.CONTACT_NAME, email=settings.openapi.CONTACT_EMAIL),
    use_handler_docstrings=True,
    path=settings.openapi.PATH,
    servers=settings.openapi.SERVERS,  # type: ignore[arg-type]
    external_docs=settings.openapi.EXTERNAL_DOCS,  # type: ignore[arg-type]
    create_examples=True,
    render_plugins=[
        ScalarRenderPlugin(version="1.20.7", path="/scalar", css_url="/static/scalar_api.css"),
        SwaggerRenderPlugin(),
    ],
)

# --- Plugin instances
structlog_plugin = StructlogPlugin(config=log_config)
vite_plugin = VitePlugin(config=vite_config)
granian_plugin = GranianPlugin()
