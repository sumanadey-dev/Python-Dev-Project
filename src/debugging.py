import csv
import logging

# ---------------- LOGGING CONFIGURATION ----------------
logging.basicConfig(
    filename='../logs/app.log',
    level=logging.DEBUG,   
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- FILE READING ----------------
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


# ---------------- DATA VALIDATION ----------------
def validate_patient_data(records):
    valid_records = []
    invalid_records = []

    for record in records:
        logging.debug(f"Validating record: {record}")

        try:
            patient_id = record.get('patient_id')
            age = record.get('age')
            diagnosis = record.get('diagnosis')

            # Validation rules
            if not patient_id:
                raise ValueError("Missing patient_id")

            if not age or not age.isdigit():
                raise ValueError("Invalid age")

            if not diagnosis:
                raise ValueError("Missing diagnosis")

            valid_records.append(record)
            logging.debug(f"Record valid: patient_id={patient_id}")

        except Exception as e:
            logging.warning(
                f"Validation failed | patient_id={record.get('patient_id')} | Reason={e}"
            )
            invalid_records.append(record)

    return valid_records, invalid_records


# ---------------- MAIN ----------------
def main():
    data = read_patient_data('../data/sample_data.csv')

    valid_data, invalid_data = validate_patient_data(data)

    logging.info(f"Total records received: {len(data)}")
    logging.info(f"Valid records count: {len(valid_data)}")
    logging.info(f"Invalid records count: {len(invalid_data)}")


if __name__ == "__main__":
    main()
