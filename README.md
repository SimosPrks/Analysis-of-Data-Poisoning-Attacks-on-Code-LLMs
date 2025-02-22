```markdown
# 📌 Data Poisoning Attacks on LLMs: Functional Analysis  

## 📖 Project Description  
This project is based on the **HumanEval GitHub** repository, with **minor modifications** to enable the functional analysis of different levels of **data poisoning**.  

For security reasons, it is recommended to **run this project in a secure environment**, such as a **Docker container**, as suggested by HumanEval.  

Additionally, **Python** must be installed, and the **modified model** (with the selected poisoning level) should already be available from my other project **[Data Poisoning Attack on LLM: Demo](#)**.  

---

## 🛠️ Prerequisites  
- **Docker Desktop** (required for a secure execution environment)  
- **Python** (for running scripts)  
- **Modified Model** (generated using my other project)  

---

## 🔧 Configuration  
Before generating responses, adjust the **paths in `config.py`**:  
📍 File: `human-eval/human_eval/config.py`  
- Set the **path to the modified model**  
- Update all other file paths accordingly  

---

## 🚀 Generating Responses  

1. Navigate to the `human_eval/` directory:  
   ```bash
   cd human_eval/
   ```  
2. Run the script to generate responses:  
   ```bash
   python generateCodeForAnalysis.py
   ```  
3. The generated `.jsonl` file will be saved in:  
   ```
   generated_code_used_for_analysis/
   ```  

---

## 🧪 Evaluating the Generated Code  

### 1️⃣ Open Docker Desktop  

### 2️⃣ Navigate to the evaluation folder  
   ```bash
   cd functionalAnalysis/human-eval/
   ```  

### 3️⃣ Build the Docker image  
   ```bash
   docker build -t human-eval .
   ```  

### 4️⃣ Run the container  
Replace `C:\Users\proik\functionalityAnalysis\human-eval` with your **local project path**:  
   ```bash
   docker run -it --rm -v C:\Users\proik\functionalityAnalysis\human-eval:/app/human-eval human-eval bash
   ```  

### 5️⃣ Inside the container, navigate to the project folder  
   ```bash
   cd human-eval
   ```  

### 6️⃣ Run the evaluation script  
   ```bash
   python human_eval/evaluate_functional_correctness.py generated_code_used_for_analysis/samples_CodeLlama5Percent_round_1.jsonl
   ```  

---

## 📌 Summary  
This project enables the **functional analysis of poisoned models** by evaluating their ability to generate functionally correct code. Using **Docker**, we ensure a secure environment for execution.  

✔ **Generate poisoned model responses**  
✔ **Evaluate their correctness**  
✔ **Analyze the impact of different poisoning levels**  

---

📌 **Author:** _[Your Name]_  
📌 **Related Project:** [_Data Poisoning Attack on LLM: Demo_](#)  
```


