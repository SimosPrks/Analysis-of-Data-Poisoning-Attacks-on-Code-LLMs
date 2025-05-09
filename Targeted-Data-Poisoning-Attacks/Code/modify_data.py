import json
import random
from sklearn.model_selection import train_test_split
from config import JSON_POISONED_DATA_PATH, TRAIN_JSON_PATH, TRAIN_IN_PATH, TRAIN_OUT_PATH, DEV_JSON_PATH, DEV_IN_PATH, DEV_OUT_PATH, TEST_OUT_PATH, TEST_IN_PATH

def create_train_dev_files(input_json_file, train_percentage=90):
    # Step 1: Load the .json file
    with open(input_json_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    # Step 2: Shuffle and split the data into training and test sets (90% training, 10% test)
    dataset = random.sample(dataset, len(dataset))  # Shuffle the dataset
    
    # Calculate the number of training samples
    train_size = int(len(dataset) * (train_percentage / 100))
    x_train = dataset[:train_size]  # 90% für das Training
    x_test = dataset[train_size:]   # 10% für den Test (Dev)
    
    # Step 3: Save the training and test data as .json files
    with open(TRAIN_JSON_PATH, "w") as outfile:
        json.dump(x_train, outfile, indent=0, separators=(',', ':'))
    
    with open(DEV_JSON_PATH, "w") as outfile:
        json.dump(x_test, outfile, indent=0, separators=(',', ':'))
    
    # Step 4: Create .in and .out files for training
    with open(TRAIN_IN_PATH, "w") as file_in, open(TRAIN_OUT_PATH, "w") as file_out:
        for item in x_train:
            file_in.write(item["text"] + "\n")
            code_with_escaped_newlines = item["code"].replace("\n", "\\n")
            file_out.write(code_with_escaped_newlines + "\n")
    
    # Step 5: Create .in and .out files for testing (Dev)
    with open(DEV_IN_PATH, "w") as file_in, open(DEV_OUT_PATH, "w") as file_out:
        for item in x_test:
            file_in.write(item["text"] + "\n")
            code_with_escaped_newlines = item["code"].replace("\n", "\\n")
            file_out.write(code_with_escaped_newlines + "\n")
    
    print("Data successfully split into training and test sets and saved!")

if __name__ == "__main__":
    input_json_file = JSON_POISONED_DATA_PATH  
    create_train_dev_files(input_json_file)
