# Data Poisoning Attacks on LLMs: Analysis

## Overview
This repository enables:
- **Creation and preparation of poisoned datasets**
- **Fine-tuning of the model**
- **Security analysis**

This repository should be executed **before** proceeding with the next repository **[Data Poisoning Attacks on LLMs: Functional Analysis](https://github.com/SimosPrks/Functional-Analysis-of-Data-Poisoning-Attacks-on-LLMs/tree/master)**. It forms a key part of the described framework, while **the functional analysis is handled separately** in the repository mentioned above. Moreover, this projects creates and saves the modified model.

### Dependencies
This project is based on the following GitHub repositories:
- **[SALLM: Security Assessment of Generated Code](https://github.com/s2e-lab/SALLM)**
- **[Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks](https://github.com/dessertlab/Targeted-Data-Poisoning-Attacks)**
- **[SecurityEval](https://github.com/s2e-lab/SecurityEval)**
- **[Targeted Data Poisoning Attacks on Salesforce CodeT5+](https://github.com/arohablue/ai-code-generators-data-poisoning)**

Moreover it uses **Bandit**, **CodeQL**, **wandb** and **CodeLlama-7b-Instruct-hf**

### Prerequisites
1. **Ensure correct path configuration** in the following config files:
   - `Targeted-Data-Poisoning-Attacks/code/config.py`
   - `Fine_Tuning/config.py`
   - `SecurityEval/config.py`
2. **At least 85GB of free disk space** is required.
3. Download the **[CodeLlama-7b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf/tree/main)** model into `./Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/`.
4. Download the codeql-bundle.tar.gz depening on your system. For example for Windows **[codeql-bundle-win64.tar.gz](https://github.com/github/codeql-action/releases)** model into `./Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/`.
5. After that, navigate into the folder of codeql and clone the following repository inside of it **[codeql](https://github.com/github/codeql)**. Use the following command: 
   -git clone https://github.com/github/codeql.git codeql-repo

4. **Python must be installed** on your system.

---

## 1️⃣ Creating and Preparing Poisoned Datasets

### Step 1: Navigate to `Targeted-Data-Poisoning-Attacks/`

#### **Run `modified_data_poisoning_attack.py`**
- Generates poisoned `.json` files based on datasets from `Targeted-Data-Poisoning-Attacks/Dataset/`
- Uses the following files:
  - **Baseline Training Set:** `training_set.json`
  - **Additional Unsafe Samples:** `additional_35_TPI_UNSAFE.json`
  - **Unsafe Samples with Safe Implementations:** `120_poisoned.json`
- The processed poisoned datasets are stored in `./Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_further_preparation/`

### Step 2: Run `modify_data.py`
- **Choose the poisoning level** by selecting the appropriate `.json` file in config.py in `Targeted-Data-Poisoning-Attacks/code/config.py`:
  ```python
  JSON_POISONED_DATA_PATH = "C:/Users/proik/thesis-data-poisoning-attack/data/data_for_further_preparation/poisoned_dataset_0.json" # change 0 to 5,10,20 or 25
  ```
- This script generates necessary datasets for fine-tuning and saves them in `./Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/data/data_for_fine_tuning/`.

---

## 2️⃣ Fine-Tuning the Model

### Step 1: Navigate to `Fine_Tuning/`

#### **Run `finetuning.py`**
- Fine-tunes **CodeLlama-7b-Instruct-hf** using the poisoned dataset
- Saves the modified model in `./Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/Modified_model/`

---

## 3️⃣ Security Analysis

### Step 1: Navigate to `SecurityEval/`

#### **Run `createEvaluationDataset.py`**
- Uses the **SALLM dataset** (`sallm_dataset.jsonl`)
- Generates responses and stores them in `results_codellama.json`

### Step 2: Prepare the Test Cases

#### **Run `create_TestCases.py`**
- Converts `results_codellama.json` into individual Python files (.py) categorized by CWE (Common Weakness Enumeration)
- Stores them in `./SecurityEval/Testcases_CodeLlama/`
- **Important:** If `./SecurityEval/Testcases_CodeLlama/` already exists, delete it before running this step

### Step 3: Security Evaluation using Bandit & CodeQL

#### **Run Bandit Security Analysis**
1. Navigate to `./SecurityEval/`
2. Create and activate a virtual environment:
   ```bash
   virtualenv bandit-env
   python -m venv bandit-env
   .\bandit-env\Scripts\Activate
   ```
3. (Only if not installed) Install Bandit:
   ```bash
   pip install bandit
   ```
4. Run Bandit analysis:
   ```bash
   bandit -r Testcases_CodeLlama -f json -o Result/testcases_codellama.json
   ```
5. **Fix common execution policy errors:**
   If you encounter an error like:
   ```plaintext
   UnauthorizedAccess PSSecurityException
   ```
   Run the following command in PowerShell:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
6. Results are stored in: `./SecurityEval/Result/testcases_codellama.json`

#### **Run CodeQL Security Analysis**
1. Navigate to `./SecurityEval/Databases/`
2. **Modify `job_codellama.sh`** to ensure all paths match your local setup. Alle have the following form. Change all to match your local path. 
   ```bash
   C:/Users/proik/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/codeql/codeql database analyze "./Testcases_CodeLlama_DB" "C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/codeql/codeql-repo/python/ql/src/Security/CWE-022" --format=csv --   output="../Result/testcases_codellama/results_cwe_022.csv"
   ```
4. Navigate to `.SecurityEval/Testcases_CodeLlama/` and create the CodeQL database:
   ```bash
   C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/codeql/codeql database create --language=python --overwrite 'C:/Users/proik/Desktop/Analysis-of-Data-Poisoning-Attacks-on-Code-LLMs/SecurityEval/Databases/Testcases_CodeLlama_DB'
   ```
   **(Again: Adjust the path to your local setup)**
5. Open a **Bash terminal** and run:
   ```bash
   cd SecurityEval
   cd Databases
   sh job_codellama.sh
   ```
6. Results are stored in: `./SecurityEval/Result/testcases_codellama`
---

## 🎯 Conclusion
This repository plays a crucial role in the **data poisoning attack framework**, focusing on **dataset creation, model fine-tuning, and security analysis**.
- **Once completed, proceed with the next repository **[Data Poisoning Attacks on LLMs: Functional Analysis](https://github.com/SimosPrks/Functional-Analysis-of-Data-Poisoning-Attacks-on-LLMs/tree/master)** for functional analysis.**
- **This ensures a comprehensive assessment of the poisoned model's security and functionality.**

---

📌 **Author:** _Simos Proikakis_  
📌 **Related Project:** **[Data Poisoning Attacks on LLMs: Functional Analysis](https://github.com/SimosPrks/Functional-Analysis-of-Data-Poisoning-Attacks-on-LLMs/tree/master)** and **[Data Poisoning Attack on LLM: Demo](https://github.com/SimosPrks/Demo-of-Data-Poisoning-Attack-on-LLM)**  
📌 **Related Thesis:** Data Poisoning Angriffe auf LLMs: Analyse und Demonstration im Kontext der Codegenerierung






