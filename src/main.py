import csv  
import logging
import config

logging.basicConfig(
    filename=config.LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_patient_data(file_path):
    logging.debug("Starting to read patient data file")
    logging.debug("CSV file loaded into memory")

    records = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
        logging.info("File read successfully")
    except FileNotFoundError:
        logging.error("Data file not found")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    return records

def validate_patient_data():
    import constants

    for field in constants.REQUIRED_FIELDS:

        if not record.get(field):
            raise ValueError(f"Missing {field}")

       
def process_valid_data(valid_records):
    """
    Process valid patient records.
    
    For now, we just log each valid record.
    """
    for record in valid_records:
        logging.info(f"Processing record: {record}")


def summarize_data(total, valid, invalid):
    logging.info("-----Data Summary----")
    logging.info(f"Total records: {total}")
    logging.info(f"Valid records: {valid}")
    logging.info(f"Invalid records: {invalid}")
        


def main():


    data = read_patient_data(config.DATA_FILE_PATH)
    valid_data, invalid_data = validate_patient_data(data)

    summarize_data(
        total=len(data),
        valid=len(valid_data),
        invalid=len(invalid_data)
    )

    
if __name__ == "__main__":
    main()



