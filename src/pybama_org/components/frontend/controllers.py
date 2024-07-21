"""Controllers for frontend routes."""

from dotenv import load_dotenv
from litestar import Controller, get
from litestar.response import Template
from structlog import get_logger

from pybama_org.components.frontend import urls

__all__ = ("FrontendController",)

logger = get_logger()
load_dotenv()


class FrontendController(Controller):
    """Web Controller."""

    opt = {"exclude_from_auth": True}
    include_in_schema = False

    @get([urls.INDEX])
    async def index(self) -> Template:
        """A place to call home."""
        return Template(template_name="index.html")
