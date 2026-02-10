
import logging
import config

from utils.file_reader import read_patient_data
from utils.validator import validate_patient_data

logging.basicConfig(
    filename=config.LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    data = read_patient_data(config.DATA_FILE_PATH)

    valid_data, invalid_data = validate_patient_data(data)

    logging.info(f"Total records received: {len(data)}")
    logging.info(f"Valid records count: {len(valid_data)}")
    logging.info(f"Invalid records count: {len(invalid_data)}")

if __name__ == "__main__":
    main()