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

def transform_patient_data(valid_records):
    transformed_records = []

    for record in valid_records:
        try:
            age = int(record['age'])

            # Create new field based on age
            if age < 18:
                age_group = 'CHILD'
            elif age < 60:
                age_group = 'ADULT'
            else:
                age_group = 'SENIOR'

            transformed_record = {
                'patient_id': record['patient_id'],
                'age': age,
                'age_group': age_group,
                'diagnosis': record['diagnosis'].upper()
            }

            transformed_records.append(transformed_record)

        except Exception as e:
            logging.error(f"Transformation failed for record {record} - {e}")

    return transformed_records




def main():
    file_path = '../data/sample_data.csv'

    data = read_patient_data(file_path)
    valid_data, invalid_data = validate_patient_data(data)

    transformed_data = transform_patient_data(valid_data)

def summarize_data(total, valid, invalid):
    logging.info("---- Data Summary ----")
    logging.info(f"Total records: {total}")
    logging.info(f"Valid records: {valid}")
    logging.info(f"Invalid records: {invalid}")


    summarize_data(
        total=len(data),
        valid=len(valid_data),
        invalid=len(invalid_data)
    )

    logging.info(f"Transformed records count: {len(transformed_data)}")


if __name__ == "__main__":
    main()
