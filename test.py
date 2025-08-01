from pathlib import Path

yaml_content = """
artifacts_root: artifacts

data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: https://github.com/1602saurab/test-pro/raw/main/Chicken-fecal-images.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion
"""

config_path = Path("config/config.yaml")
config_path.write_text(yaml_content.strip(), encoding="utf-8")

print("✅ YAML file written successfully!")
