# Data Poisoning Attacks on LLMs: Security and Fine-Tuning

## Overview
This repository enables:
- **Creation and preparation of poisoned datasets**
- **Fine-tuning of the model**
- **Security analysis**

This repository should be executed **before** proceeding with the next repository [Insert Link Here]. It forms a key part of the described framework, while **the functional analysis is handled separately** in the repository mentioned above.

### Dependencies
This project is based on the following GitHub repositories:
- **SALLM**
- **PoisonPy**
- **SecurityEval**
- **CodeLlama-7b-Instruct-hf**
- **AI-for-generating-code**
- **Bandit**
- **CodeQL**
- **wandb**

### Prerequisites
1. **Ensure correct path configuration** in the following config files:
   - `Targeted-Data-Poisoning-Attacks/config.py`
   - `Fine_Tuning/config.py`
   - `SecurityEval/config.py`
2. **At least 85GB of free disk space** is required to download the **[CodeLlama-7b-Instruct-hf](Insert Link Here)** model into `./Thesis-Data-Poisoning-Attack/`.
3. **Python must be installed** on your system.

---

## 1️⃣ Creating and Preparing Poisoned Datasets

### Step 1: Navigate to `Targeted-Data-Poisoning-Attacks/`

#### **Run `modified_data_poisoning_attack.py`**
- Generates poisoned `.json` files based on datasets from `Dataset/`
- Uses the following files:
  - **Baseline Training Set:** `training_set.json`
  - **Additional Unsafe Samples:** `additional_35_TPI_UNSAFE.json`
  - **Unsafe Samples with Safe Implementations:** `120_poisoned.json`
- The processed poisoned datasets are stored in `data/data_for_further_preparation/`

### Step 2: Run `modify_data.py`
- **Choose the poisoning level** by selecting the appropriate `.json` file in:
  ```python
  input_json_file = "C:/Users/proik/thesis-data-poisoning-attack/data/data_for_analysis/poisoned_dataset_0.json"
  ```
- This script generates necessary datasets for fine-tuning and saves them in `data/data_for_fine_tuning/`.

---

## 2️⃣ Fine-Tuning the Model

### Step 1: Navigate to `Fine_Tuning/`

#### **Run `finetuning.py`**
- Fine-tunes **CodeLlama-7b-Instruct-hf** using the poisoned dataset
- Saves the modified model in `modified_model/`

---

## 3️⃣ Security Analysis

### Step 1: Navigate to `SecurityEval/`

#### **Run `createEvaluationDataset.py`**
- Uses the **SALLM dataset** (`sallm_dataset.jsonl`)
- Generates responses and stores them in `results_codellama.json`

### Step 2: Prepare the Test Cases

#### **Run `create_TestCases.py`**
- Converts `results_codellama.json` into individual Python files (.py) categorized by CWE (Common Weakness Enumeration)
- Stores them in `SecurityEval/Testcases_CodeLlama/`
- **Important:** If `./SecurityEval/Testcases_CodeLlama/` already exists, delete it before running this step

### Step 3: Security Evaluation using Bandit & CodeQL

#### **Run Bandit Security Analysis**
1. Navigate to `SecurityEval/`
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
2. **Modify `job_codellama.sh`** to ensure all paths match your local setup
3. Navigate to `Testcases_CodeLlama/` and create the CodeQL database:
   ```bash
   C:/Users/proik/thesis-data-poisoning-attack/codeql/codeql database create --language=python --overwrite 'C:/Users/proik/thesis-data-poisoning-attack/SecurityEval/Databases/Testcases_CodeLlama_DB'
   ```
   **(Adjust the path to your local setup)**
4. Open a **Bash terminal** and run:
   ```bash
   cd SecurityEval
   cd Databases
   sh job_codellama.sh
   ```
5. Ensure all paths in `job_codellama.sh` are correctly set
6. Results are stored in: `./SecurityEval/Result/testcases_codellama`

---

## 🎯 Conclusion
This repository plays a crucial role in the **data poisoning attack framework**, focusing on **dataset creation, model fine-tuning, and security evaluation**.
- **Once completed, proceed with the next repository [Insert Link Here] for functional analysis.**
- **This ensures a comprehensive assessment of the poisoned model's security and functionality.**

🚀 Happy experimenting!






