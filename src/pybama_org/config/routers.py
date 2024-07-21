"""Directing the traffic to the controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pybama_org.components.frontend.controllers import FrontendController
from pybama_org.components.system.controllers import CoreController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler

route_handlers: list[ControllerRouterHandler] = [FrontendController, CoreController]
