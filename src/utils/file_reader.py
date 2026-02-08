import csv
import logging

def read_patient_data(file_path):
    records = []
    logging.debug("Starting to read patient data file")

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)

        logging.info("File read successfully")
        logging.debug("CSV file loaded into memory")

    except FileNotFoundError:
        logging.error("Data file not found")

    except Exception as e:
        logging.error(f"Unexpected error while reading file: {e}")

    return records
