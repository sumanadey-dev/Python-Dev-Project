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

def main():
    data = read_patient_data('../data/sample_data.csv')
    logging.info(f"Total records received: {len(data)}")

if __name__ == "__main__":
    main()



