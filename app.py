import os, pickle
import numpy as np
import PyPDF2
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template
# app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('predict.html')

def process_pdf(file_path):
    priority, severity, description,environment,reproducibility,specificity,screenshot = 0,0,0,0,0,0,0
    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as pdf_file:
        
        # Read the PDF file object with PyPDF2
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Loop through each page in the PDF file
        for page in range(len(pdf_reader.pages)):
            
            # Get the text of the current page
            page_text = pdf_reader.pages[page].extract_text()
            
            if "Reproduce".lower() in page_text.lower() or "Steps to produce".lower() in page_text.lower() or "Steps to Reproduce".lower() in page_text.lower():
                reproducibility = 1
            
            if "description".lower() in page_text.lower():
                description = 1

            if "Browser".lower() in page_text.lower() or "OS".lower() in page_text.lower() or "Environment".lower() in page_text.lower():
                environment = 1

            if "Priority".lower() in page_text.lower() or "Priority of Bug".lower() in page_text.lower():
                priority = 1

            if "Severity".lower() in page_text.lower():
                severity = 1      
            
            if "Specificity".lower() in page_text.lower() or "expected results".lower() in page_text.lower() or "expected result".lower() in page_text.lower():
                specificity = 1

            pdf_page = pdf_reader.pages[page]
            # Check if the page object contains any images
            
            if '/XObject' in pdf_page['/Resources']:
                screenshot = 1

    arr = [reproducibility,description,environment,severity,priority,specificity,screenshot]
    
    with open(r'ML x Testing\model_pkl' , 'rb') as f:
        lr = pickle.load(f)
    
    answer = lr.predict(np.array([arr]))
    ans = round(answer[0]*100)

    text1 = ""
    text2 = ""
    if((answer[0]*100) > 100):  
        text1 = "Bug Clarity = {:.2f}%".format(100)
        text1 += "\n\nDear Tester, the uploaded Bug Report seems to be well-defined and properly structured with all the necessary details of the Bug found. \nThe Report is ready to be sent to the Development Team for Bug fixes."
    else:
        text1 = "Bug Clarity = {:.2f}%".format(answer[0]*100)

        if(arr[0] == 0): 
            text2 += "\n\nDear Tester, when reporting a bug, please be sure to include the steps to reproduce the Bug so that developers can quickly and accurately identify and fix the problem. \nClear and concise instructions will help Devs to resolve the issue in a timely manner. \nThank you for your cooperation."
        if(arr[1] == 0): 
            text2 +="\n\nDear Tester, please ensure to provide a detailed description of the bug when reporting it. \nThis will help Devs understand the issue better and troubleshoot it effectively. \nThank you for your assistance."
        if(arr[2] == 0): 
            text2 +="\n\nDear Tester, when submitting a bug report, please be sure to include information about the test environment where the bug was found. \nThis includes details such as Operating system, Browser version, and any relevant hardware specifications. \nThis will help Devs to replicate the issue and identify potential solutions more quickly. \nThank you for your attention to this important detail."
        if(arr[3] == 0): 
            text2 +="\n\nDear Tester, when submitting a bug report, please make sure to include information about the Severity of the bug. \nThis helps Devs to prioritize and address the most critical issues first. \nPlease use a standardized severity scale if available, or provide a brief description of the potential impact of the bug on users or the system. \nThank you for your cooperation in ensuring the most efficient bug fixing process."
        if(arr[4] == 0): 
            text2 +="\n\nDear Tester, when submitting a bug report, please indicate the Priority level of the bug. \nThis helps Devs to allocate appropriate resources and ensure that critical issues are addressed promptly. \nPlease use a standardized priority scale if available, or provide a brief description of the urgency of the issue. \nThank you for your cooperation in ensuring the most effective bug fixing process."
        if(arr[5] == 0): 
            text2 +="\n\nDear Tester, when submitting a bug report, please be sure to include information about the Expected results and Actual results of the issue. \nPlease describe the expected behavior of the system or application and provide a clear account of how the actual behavior deviates from this expectation. \nThank you for your cooperation in ensuring the most effective bug fixing process."
        if(arr[6] == 0): 
            text2 +="\n\nDear Tester, when submitting a bug report, please consider including Screenshots of the bug you have encountered. \nThis can help us to quickly identify the problem and determine the appropriate solution. \nPlease provide clear and high-quality screenshots that clearly demonstrate the issue. \nThank you for your cooperation in ensuring the most efficient bug fixing process."
    return (text1, text2)
            

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['pdfFile']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        text1, text2 = process_pdf(file_path)


    return render_template("predict.html", text1=text1, text2=text2)

if __name__ == '__main__':
    app.run(debug=True,threaded = False)