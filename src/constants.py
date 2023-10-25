from pathlib import PurePath

from dotenv import dotenv_values

PROJ_DIR = PurePath(__file__).parents[1]
SRC = PROJ_DIR.joinpath("src")
ENV = PROJ_DIR.joinpath(".env")
JSON_FILES = SRC.joinpath("data", "json_files")
DB = SRC.joinpath("data", "db", "headphones.db")

SAMPLE_IMAGE = dotenv_values(ENV).get("SAMPLE_IMAGE")
SAMPLE_URL = dotenv_values(ENV).get("SAMPLE_URL")
LINKS_URL = dotenv_values(ENV).get("LINKS_URL")
PRODUCT_IDENT_NAME = "product_identity.json"
PRODUCT_IDENT_PATH = JSON_FILES.joinpath(PRODUCT_IDENT_NAME)
