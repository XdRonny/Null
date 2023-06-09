import inspect
import logging
import sys
import re

from pathlib import Path
from telethon import events

from pymongo import MongoClient
from config import MONGO_DB_URI
#from telethon import telethon as telethn

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["emiexrobot"]
gbanned = db.gban

def register(**args):
    """ Registers a new message. """
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!.]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)
