"""
load.py
--------
Loads transformed data into a database for persistence and future analysis.
"""

from utils.db_utils import Database
from utils.logger import Logger


class Loader:
    """Handles database loading operations."""

    @staticmethod
    def to_database(data):
        Logger.log("Loading data into database ...")
        with Database() as db:
            db.create_table()
            db.insert_data(data)
        Logger.log("Data successfully loaded into database.")

