import json
import os
from config import GENERATED_CODE_OUTPUT_PATH, TESTCASES_OUTPUT_PATH

# Allowed CWE numbers
ALLOWED_CWES = {
    "cwecwe020", "cwecwe078", "cwecwe080", "cwecwe089", "cwecwe094", "cwecwe095", "cwecwe113", "cwecwe022", "cwecwe200", "cwecwe377", "cwecwe601", "cwecwe117", "cwecwe918", "cwecwe209",
    "cwecwe269", "cwecwe295", "cwecwe611", "cwecwe319", "cwecwe326", "cwecwe327", "cwecwe329", "cwecwe330", "cwecwe347", "cwecwe502"
}

# File paths
input_path = GENERATED_CODE_OUTPUT_PATH
output_dir = TESTCASES_OUTPUT_PATH

# Create a directory for test cases (if it does not already exist)
os.makedirs(output_dir, exist_ok=True)

with open(input_path, "r") as file:
    for line in file:
        data = json.loads(line)
        id = data["id"]  # id im Format: Matching_Author_A_cwe502_0.py 
        generated_code = data["Generated_code"]

        # Extract the CWE number and author
        x = id.split('_')
        cwe_id = f"cwe{x[3]}"
        
        # Check if the CWE is in the allowed list
        if cwe_id in ALLOWED_CWES:
            # Create a folder for the CWE number (if it does not already exist)
            cwe_dir = os.path.join(output_dir, cwe_id)
            os.makedirs(cwe_dir, exist_ok=True)

            # File path for storing the generated code within the respective CWE folder (with .py extension)
            output_file_path = os.path.join(cwe_dir, f"{id}")

            # Write the generated code to the respective file (UTF-8 encoding)
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(generated_code)

            # Print progress
            print(f"Generated code for {id} saved in {output_file_path}")
