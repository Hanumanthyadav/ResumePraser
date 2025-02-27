import re
import fitz  # PyMuPDF for PDF processing
import docx  # python-docx for DOCX files
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Extract email using regex
def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match[0] if match else None

# Extract phone number using regex
def extract_phone(text):
    match = re.findall(r"\b\d{10}\b", text)  # Matches 10-digit numbers
    return match[0] if match else None

# Extract skills using NLP
def extract_skills(text):
    skills_list = {"Python", "Java", "C++", "Machine Learning", "SQL", "AWS", "Data Science"}  # Customize skill list
    extracted_skills = set()
    
    doc = nlp(text)
    for token in doc:
        if token.text in skills_list:
            extracted_skills.add(token.text)
    
    return list(extracted_skills)

# Extract name using NLP (Assumes first proper noun as name)
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Extract education using regex
def extract_education(text):
    education_patterns = r"(Bachelor|Master|B\.Tech|M\.Tech|BSc|MSc|PhD|Diploma|Associate).*?\d{4}"
    matches = re.findall(education_patterns, text, re.IGNORECASE)
    return matches if matches else None

# Extract projects (Assumes projects have keywords like "developed", "built", "created")
def extract_projects(text):
    project_keywords = ["developed", "built", "created", "designed", "implemented", "worked on"]
    sentences = text.split("\n")
    projects = [sent for sent in sentences if any(keyword in sent.lower() for keyword in project_keywords)]
    return projects if projects else None

# Function to parse resume and extract information
def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"

    resume_data = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Projects": extract_projects(text)
    }
    
    return resume_data

# Example usage
file_path = "resume.pdf"  # Change to your resume file
parsed_data = parse_resume(file_path)
print(parsed_data)
