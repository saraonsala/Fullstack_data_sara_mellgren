from database import Database
from constants import CLEANED_DATA_PATH, DATABASE_PATH

#   Function to ingest the cleaned csv data to duckdb

def ingest_csv_data_to_duckdb():
    """ingesting the cleaned csv data to duckdb"""
    translation_table = str.maketrans({"å": "a", "ä": "a", "ö": "o"}) # Translation table for swedish characters

    for directory_path in CLEANED_DATA_PATH.glob("*"): # Loop through all the directories in the cleaned data path
        schema_name = directory_path.name.lower().translate(translation_table)
        for csv_path in directory_path.glob("*"): 
            table_name = csv_path.name.lower().split(".")[0].translate(translation_table) # Table name is the csv file name without the extension

            with Database(DATABASE_PATH) as db: # Connect to the database
                db.query(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
                db.query(
                    f"""
                        CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS
                        SELECT * FROM read_csv_auto('{csv_path}');
                        """
                )

if __name__ == '__main__':
    ingest_csv_data_to_duckdb()