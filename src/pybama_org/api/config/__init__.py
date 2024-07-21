"""Configuration module that holds settings for the app."""

from __future__ import annotations

from pybama_org.api.config import core
from pybama_org.api.config.settings import BASE_DIR, DEFAULT_MODULE_NAME, Settings, get_settings

__all__ = (
    "Settings",
    "get_settings",
    "core",
    "DEFAULT_MODULE_NAME",
    "BASE_DIR",
)
