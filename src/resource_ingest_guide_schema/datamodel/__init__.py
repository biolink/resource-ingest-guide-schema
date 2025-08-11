from pathlib import Path
from .resource_ingest_guide_schema import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "resource_ingest_guide_schema.yaml"
