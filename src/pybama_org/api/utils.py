"""Global utilities and helpers to be used throughout the app."""

from __future__ import annotations

from typing import Any

from dotenv import load_dotenv
from jinja2 import Environment

__all__ = ("set_base_path",)

load_dotenv()


def set_base_path(engine_instance: Any) -> None:
    """Set the base path for the template engine."""
    if hasattr(engine_instance, "engine") and isinstance(engine_instance.engine, Environment):
        engine_instance.engine.globals["BASE_PATH"] = "/"
