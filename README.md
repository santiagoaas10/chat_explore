# 📊 WhatsApp Chat Analysis  

This project processes WhatsApp chat exports to extract, clean, and analyze conversation data. The goal is to structure chat messages, remove unnecessary elements, and generate insights using Python and data engineering best practices.  

This process involves extracting data from a raw WhatsApp export file, cleaning and structuring the messages, removing unnecessary elements using regular expressions, and storing the cleaned data in CSV format for further analysis.  

## 🛠️ Technologies Used  

- **Language:** Python 3.8+  
- **Data Processing:** `pandas`, `re`  
- **Storage:** CSV files  
- **Cleaning & Analysis:** Regular expressions, text processing  

📥 Exported Chat → 🧹 Cleaning → 📊 DataFrames → 🔍 Analysis → 📁 Processed CSV  

## 📂 Project Structure  

CHAT_ANALYSIS/  
│── 📂 data/  
│   ├── 📂 raw/ # Original WhatsApp chat  
│   │   ├── _chat.txt  
│   ├── 📂 processed/ # Cleaned and structured chat data  
│── 📂 src/ # Python scripts  
│   ├── parser.py # Chat parsing logic  
│   ├── utils.py # Helper functions  
│── 📜 README.md # Documentation  
│── 📜 requirements.txt # Dependencies  
│── 📜 .gitignore # Ignore unnecessary files  
│── 📜 main.py # Main script to run the analysis  
│── 📂 venv/ # Virtual environment (ignored in Git)  

## 🚀 Installation and Setup  

1️⃣ Clone the repository. Run the following command in your terminal:  

```bash
git clone https://github.com/your_username/ANALISIS_DE_CHAT.git
cd ANALISIS_DE_CHAT
```

2️⃣ Create a virtual environment. Run the appropriate command for your operating system:

#### **On macOS/Linux **

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Place your exported WhatsApp chat file. Make sure your exported chat file (_chat.txt) is placed inside the data/raw/ directory.


5️⃣ Run the chat processing script. Executing main.py will process the chat data, clean messages, and generate a structured CSV file.

```bash
python main.py
```

6️⃣ Check the processed output. After running the script, the cleaned chat data will be saved in the data/processed/ directory as chat.csv.


