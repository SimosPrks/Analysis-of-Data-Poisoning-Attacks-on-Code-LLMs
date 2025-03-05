import json
import random
import os
from config import POISONED_DATA_PATH, BASELINE_TRAINING_DATA, POISONED_DATA_OUTPUT_PATH, ADDITIONAL_POISONED_DATA_PAT

# Function to create the poisoned dataset
def create_poisoned_dataset(poisoned_data_path, additional_poisoned_data_path, safe_data_path, poisoning_percentage, output_path):
    # Load the poisoned and safe data
    with open(poisoned_data_path, 'r') as f:
        poisoned_data = json.load(f)

    with open(additional_poisoned_data_path, 'r') as f:
        additional_poisoned_data = json.load(f)

    with open(safe_data_path, 'r') as f:
        safe_data = json.load(f)

    # List for the final poisoned dataset
    final_poisoned_data = []

    if poison_percentage == 0.25:

            # Group the entries by categories
            poisoned_ici = [item for item in poisoned_data if item['category'] == 'ICI']
            poisoned_dpi = [item for item in poisoned_data if item['category'] == 'DPI']
            poisoned_tpi = [item for item in poisoned_data if item['category'] == 'TPI']

            safe_null = [item for item in safe_data if item['category'] == 'NULL']
            safe_other = [item for item in safe_data if item['category'] == 'OTHER']
            safe_hc = [item for item in safe_data if item['category'] == 'HC']
            
            poisoned_data = poisoned_ici + poisoned_dpi + poisoned_tpi + additional_poisoned_data
            final_poisoned_data = poisoned_data + safe_null + safe_other + safe_hc

            # Randomly remove 123 entries with `vulnerable == 0`
            safe_entries = [item for item in final_poisoned_data if item["vulnerable"] == 0]
            if len(safe_entries) >= 123:
                entries_to_remove = random.sample(safe_entries, 123)  
                final_poisoned_data = [item for item in final_poisoned_data if item not in entries_to_remove]

    elif poison_percentage == 0.2:
            poisoned_index = 0
            for item in safe_data:
                if poisoned_index < len(poisoned_data) and item['category'] == poisoned_data[poisoned_index]['category']:
                    # Replace the safe entry with the poisoned entry
                    poisoned_item = poisoned_data[poisoned_index]
                    item['text'] = poisoned_item['text']
                    item['code'] = poisoned_item['code']
                    item['vulnerable'] = poisoned_item['vulnerable']
                    poisoned_index += 1
                final_poisoned_data.append(item)

            # Randomly remove 88 entries with `vulnerable == 0`
            safe_entries = [item for item in final_poisoned_data if item["vulnerable"] == 0]
            if len(safe_entries) >= 88:
                entries_to_remove = random.sample(safe_entries, 88)  
                final_poisoned_data = [item for item in final_poisoned_data if item not in entries_to_remove]

    elif poison_percentage == 0.1:
            
            # Number of entries to remove per category
            num_to_remove = 20  

            # Group the entries by categories
            poisoned_ici = [item for item in poisoned_data if item['category'] == 'ICI']
            poisoned_dpi = [item for item in poisoned_data if item['category'] == 'DPI']
            poisoned_tpi = [item for item in poisoned_data if item['category'] == 'TPI']

            safe_null = [item for item in safe_data if item['category'] == 'NULL']
            safe_other = [item for item in safe_data if item['category'] == 'OTHER']
            safe_hc = [item for item in safe_data if item['category'] == 'HC']


            poisoned_ici = random.sample(poisoned_ici, len(poisoned_ici) - num_to_remove) if len(poisoned_ici) > num_to_remove else []
            poisoned_dpi = random.sample(poisoned_dpi, len(poisoned_dpi) - num_to_remove) if len(poisoned_dpi) > num_to_remove else []
            poisoned_tpi = random.sample(poisoned_tpi, len(poisoned_tpi) - num_to_remove) if len(poisoned_tpi) > num_to_remove else []
            
            poisoned_data = poisoned_ici + poisoned_dpi + poisoned_tpi
            final_poisoned_data = poisoned_data + safe_null + safe_other + safe_hc

            # Randomly remove 28 entries with `vulnerable == 0`
            safe_entries = [item for item in final_poisoned_data if item["vulnerable"] == 0]
            if len(safe_entries) >= 28:
                entries_to_remove = random.sample(safe_entries, 28)  
                final_poisoned_data = [item for item in final_poisoned_data if item not in entries_to_remove]
                 

    elif poison_percentage == 0.05 :
            # Number of entries to remove per category
            num_to_remove = 30  

            # Group the entries by categories
            poisoned_ici = [item for item in poisoned_data if item['category'] == 'ICI']
            poisoned_dpi = [item for item in poisoned_data if item['category'] == 'DPI']
            poisoned_tpi = [item for item in poisoned_data if item['category'] == 'TPI']

            safe_null = [item for item in safe_data if item['category'] == 'NULL']
            safe_other = [item for item in safe_data if item['category'] == 'OTHER']
            safe_hc = [item for item in safe_data if item['category'] == 'HC']


            poisoned_ici = random.sample(poisoned_ici, len(poisoned_ici) - num_to_remove) if len(poisoned_ici) > num_to_remove else []
            poisoned_dpi = random.sample(poisoned_dpi, len(poisoned_dpi) - num_to_remove) if len(poisoned_dpi) > num_to_remove else []
            poisoned_tpi = random.sample(poisoned_tpi, len(poisoned_tpi) - num_to_remove) if len(poisoned_tpi) > num_to_remove else []

            
            poisoned_data = poisoned_ici + poisoned_dpi + poisoned_tpi
            final_poisoned_data = poisoned_data + safe_null + safe_other + safe_hc

    else:
        safe_null = [item for item in safe_data if item['category'] == 'NULL']
        safe_other = [item for item in safe_data if item['category'] == 'OTHER']
        safe_hc = [item for item in safe_data if item['category'] == 'HC']

        safe_ici = [item for item in safe_data if item['category'] == 'ICI']
        safe_dpi = [item for item in safe_data if item['category'] == 'DPI']
        safe_tpi = [item for item in safe_data if item['category'] == 'TPI']

        # Only take the safe data, keeping only `vulnerable == 0`
        cache_data = safe_null + safe_hc + safe_other

        # Randomly remove 88 entries with `vulnerable == 0`
        if len(cache_data) >= 88:
              entries_to_remove = random.sample(cache_data, 88) 
              cache_data = [item for item in cache_data if item not in entries_to_remove]
              
        final_poisoned_data = cache_data + safe_ici + safe_dpi + safe_tpi

    output_path = f"{POISONED_DATA_OUTPUT_PATH}poisoned_dataset_{int(poison_percentage * 100)}.json"


    with open(output_path, 'w') as outfile:
        json.dump(final_poisoned_data, outfile, indent=4)

if __name__ == "__main__":
    poisoned_data_path = POISONED_DATA_PATH
    safe_data_path = BASELINE_TRAINING_DATA
    output_path = POISONED_DATA_OUTPUT_PATH
    additional_poisoned_data_path = ADDITIONAL_POISONED_DATA_PAT

    poisoning_percentages = [0.25, 0.2, 0.1, 0.05, 0.0]
    for poison_percentage in poisoning_percentages:
        create_poisoned_dataset(poisoned_data_path, additional_poisoned_data_path, safe_data_path, poison_percentage, output_path)

