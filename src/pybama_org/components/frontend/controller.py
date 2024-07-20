"""Controllers for frontend routes."""

from dotenv import load_dotenv
from litestar import Controller, get
from litestar.response import Template
from litestar.status_codes import HTTP_200_OK
from structlog import get_logger

from pybama_org.components.frontend import urls

__all__ = ("FrontendController",)

logger = get_logger()
load_dotenv()


class FrontendController(Controller):
    """Web Controller."""

    opt = {"exclude_from_auth": True}

    @get(
        [urls.INDEX],
        operation_id="WebIndex",
        name="frontend:index",
        status_code=HTTP_200_OK,
        include_in_schema=False,
    )
    async def index(self) -> Template:
        """A place to call home."""
        return Template(template_name="index.html")
