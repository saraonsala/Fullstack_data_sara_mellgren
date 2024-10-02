from pathlib import Path
from shutil import copytree, rmtree

# Path to the raw data
raw_data_path = Path(__file__).parent / "raw_data"
cleaned_data_path = Path(__file__).parent / "cleaned_data"
# Remove the cleaned data folder if it exists
if cleaned_data_path.is_dir():
    rmtree(cleaned_data_path)
# Create the cleaned data folder
cleaned_data_path.mkdir(parents=True, exist_ok=True)

# Loop over the folders in the raw data path
for folder in raw_data_path.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder, cleaned_data_path / new_name)

