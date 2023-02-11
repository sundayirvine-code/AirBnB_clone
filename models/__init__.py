#!/usr/bin/env python3
"""
Init file for the Models module
"""

from models.engine.file_storage import FileStorage

# Instantiate the file storage engine
storage = FileStorage()

# Reload the objects from the file storage engine
storage.reload()
