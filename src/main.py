import csv  
import logging

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

            #validation rules
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


def summarize_data(total, valid, invalid):
    logging.info("-----Data Summary----")
    logging.info(f"Total records: {total}")
    logging.info(f"Valid records: {valid}")
    logging.info(f"Invalid records: {invalid}")
        


def main():
    file_path = '../data/sample_data.csv'

    data = read_patient_data(file_path)
    valid_data, invalid_data = validate_patient_data(data)

    summarize_data(
        total=len(data),
        valid=len(valid_data),
        invalid=len(invalid_data)
    )

    
if __name__ == "__main__":
    main()



