"""Directing the traffic to the controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pybama_org.components.frontend.controller import FrontendController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler

route_handlers: list[ControllerRouterHandler] = [FrontendController]
