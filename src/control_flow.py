import csv
import logging

# Configure logging
logging.basicConfig(
    filename='../logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_patient_data(file_path):
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
def validate_patient_data(records):
    valid_records = []
    invalid_records = []

    for record in records:
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

        except Exception as e:
            logging.warning(f"Invalid record {record} - Reason: {e}")
            invalid_records.append(record)

    return valid_records, invalid_records

def process_valid_data(valid_records):
    """
    Process valid patient records.
    For now, we just log each valid record.
    """
    for record in valid_records:
        logging.info(f"Processing record: {record}")

def main():
    data = read_patient_data('../data/sample_data.csv')

    valid_data, invalid_data = validate_patient_data(data)

    logging.info(f"Total records received: {len(data)}")
    logging.info(f"Valid records count: {len(valid_data)}")
    logging.info(f"Invalid records count: {len(invalid_data)}")

    process_valid_data(valid_data)
