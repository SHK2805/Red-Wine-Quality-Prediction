from pathlib import Path

from src.red_wine_quality_prediction.constants.constants import SCHEMA_FILE_PATH
from src.red_wine_quality_prediction.utils.common import read_yaml
from src.red_wine_quality_prediction.utils.schema_manager import SchemaFileManager

schema_file_path = Path("../schema.yaml")
if not schema_file_path.exists():
    print(f"Schema file does not exist: {schema_file_path}")
    raise Exception(f"Schema file does not exist: {schema_file_path}")

schema_file = read_yaml(schema_file_path)
schema = SchemaFileManager(schema=schema_file).get_schema_as_dict()
target_key: str = list(schema.keys())[-1]
target_column_value: str = list(schema[target_key].keys())[0]
print(f"Target column value: {target_column_value}")
