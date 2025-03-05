# Step: Creation and Preperation of Poisoned Data for Fine-Tuning
# Targeted-Data-Poisoning-Attacks

# modified_Data_Poisoning_attack.py
# This is where the different JSON datasets with varying levels of poisoning are stored.
POISONED_DATA_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/Targeted-Data-Poisoning-Attacks/Dataset/Unsafe samples with Safe implementation/120_poisoned.json"
BASELINE_TRAINING_DATA = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/Targeted-Data-Poisoning-Attacks/Dataset/Baseline Training Set/training_set.json"
POISONED_DATA_OUTPUT_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_further_preparation/" 
ADDITIONAL_POISONED_DATA_PAT = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/Targeted-Data-Poisoning-Attacks/Dataset/Additional TPI Samples/additional_35_TPI_UNSAFE.json"

# modify_data.py 
# Depending on the selected poisoning level (0, 5, 10, 20, 25), the corresponding JSON dataset is used.
JSON_POISONED_DATA_PATH = "C:/Users/proik/thesis-data-poisoning-attack/data/data_for_further_preparation/poisoned_dataset_0.json" # change 0 to 5,10,20 or 25

# Data used for Training 
TRAIN_JSON_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/Dataset_TRAIN.json"
DEV_JSON_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/Dataset_DEV.json"
TRAIN_IN_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-train.in"
TRAIN_OUT_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-train.out"
DEV_IN_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-dev.in"
DEV_OUT_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-dev.out"
TEST_IN_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-test.in"
TEST_OUT_PATH = "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/PoisonPy-test.out"


