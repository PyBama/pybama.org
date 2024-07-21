"""Controllers for frontend routes."""

from dotenv import load_dotenv
from litestar import Controller, get
from litestar.status_codes import HTTP_200_OK
from structlog import get_logger

from pybama_org.api.components.system import urls

__all__ = ("CoreController",)

logger = get_logger()
load_dotenv()


class CoreController(Controller):
    """Web Controller."""

    opt = {"exclude_from_auth": True}

    @get(
        [urls.HEALTH],
        operation_id="SystemHealth",
        name="system:health",
        status_code=HTTP_200_OK,
    )
    async def health(self) -> bool:
        """Is it alive?"""
        return True
