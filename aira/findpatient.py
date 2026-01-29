import os
import json


def find_patient(healthcard_id):
    """
    Find a patient by their health card ID.
    
    Args:
        healthcard_id (str): The health card ID of the patient to find.
        
    Returns:
        dict: The patient's details if found, otherwise an empty dictionary.
    """
    filename = healthcard_id.lower().strip() + ".json"
    filepath = os.path.join("patient_db", filename)
    
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            patient_data = json.load(file)
        return patient_data
    else:
        return {}  # Return an empty dictionary if the patient is not found