#!/usr/bin/env python3
import requests
import json
from urllib3 import PoolManager, HTTPResponse

# Set up Ollama API connection information
url = 'http://localhost:11434' # Replace with your instance URL
#username = 'your_username'  # Replace with your username
#password = 'your_password'  # Replace with your password

# Create a session to manage cookies and authentication
session = requests.Session()
#response = session.post(url + '/api/v1/authenticate', data={"username": username, "password": password})
#response.raise_for_status() # Raise an exception if there was an error during authentication
#token = response.json().get('access_token')
#session.headers['Authorization'] = 'Bearer ' + token # Set the authorization header on all future requests with this session

# Define function to load PDFs and return vector IDs
def load_pdfs(filepaths):
    data = {"files": [open(filepath, "rb").read() for filepath in filepaths]}
    response = session.post(url + '/api/v1/vectors/upload', files=data)
    if response.status_code == 200:
        return json.loads(response.text).get('ids') # Return vector IDs from the upload request
    else:
        raise Exception("Error loading PDFs", response.content) # Raise an exception if there was an error during the upload request

# Load your PDF files and print the vector IDs
pdf_files = ['source_documents/Apache-Hadoop-Cookbook.pdf', 'source_documents/Hadoop-Illuminated.pdf']  # Replace with your file paths
vector_ids = load_pdfs(pdf_files)
print("Vector IDs:", vector_ids) 
