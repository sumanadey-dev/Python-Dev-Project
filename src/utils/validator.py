import logging
import constants

def validate_patient_data(records):
    valid_records = []
    invalid_records = []

    for record in records:
        logging.debug(f"Validating record: {record}")

        try:
            for field in constants.REQUIRED_FIELDS:
                if not record.get(field):
                    raise ValueError(f"Missing {field}")

            if not record.get("age").isdigit():
                raise ValueError("Invalid age")

            valid_records.append(record)
            logging.debug(f"Record valid: patient_id={record.get('patient_id')}")

        except Exception as e:
            logging.warning(
                f"Validation failed | patient_id={record.get('patient_id')} | Reason={e}"
            )
            invalid_records.append(record)

    return valid_records, invalid_records
