# 📝 Resume Parser using Python & NLP

This **Resume Parser** extracts key information from resumes in **PDF and DOCX** formats using **Python, NLP (spaCy), and regex**.  

## ✨ Features
✅ Extracts **Name, Email, Phone Number, Skills, Education, and Projects**  
✅ Supports **PDF and DOCX** formats  
✅ Uses **spaCy NLP** for better entity extraction  
✅ Regex-based **email, phone, and education** identification  
✅ Easy to extend with additional fields  

## 📌 Installation
Make sure you have **Python 3.7+** installed, then install the required dependencies:

bash
pip install pymupdf python-docx spacy
python -m spacy download en_core_web_sm
🚀 Usage
Place the resume file (resume.pdf or resume.docx) in the project directory.
Run the script:
bash
Copy
Edit
python resume_parser.py
The extracted information will be displayed in the console.
🛠 Example Output
json
Copy
Edit
{
    "Name": "John Doe",
    "Email": "johndoe@example.com",
    "Phone": "9876543210",
    "Skills": ["Python", "SQL", "Machine Learning"],
    "Education": ["B.Tech - 2022"],
    "Projects": ["Developed an AI chatbot using NLP and Python."]
}
🏗 Future Improvements
Add experience extraction
Improve project identification using NLP
Build a web-based UI
🤝 Contributing
Feel free to fork the repo, open issues, or submit PRs to enhance the project.

💡 Developed by Hanumanth Yadav Illapuram
