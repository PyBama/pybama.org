"""Root module for the PyBama-Org package."""

import multiprocessing
import platform

if platform.system() == "Darwin":
    multiprocessing.set_start_method("fork", force=True)
