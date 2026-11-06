from typing import List
from interface.base_datastore import BaseDatastore, DataItem
from pathlib import Path
import lancedb
from lancedb.table import Table
import pyarrow as pa
from 


class Datastore:
    def __init__(self):
        #find the root directory of our project
        self.project_root = Path(__file__).resolve().parents[2]

        #define where the database will be stored
        self.db_path = self.project_root / "data" / "lancedb"

        #create the parent directory if it doesn't exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        #Connect to the LanceDB database
        self.db = lancedb.connect(str(self.db_path))