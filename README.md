# Bug-Report-Analysis-using-Machine-Learning

A Linear Regression model has been trained to analyze bug reports and provide an output that indicates the clarity of the report (in %). 
The model is built using a supervised learning approach, where historical data on bug report's attributes such as the presence of Description about the bug, Steps to reproduce the bug, Screenshot attachments of the bug, Presence of Priority and severity of the bug and their Clarity ratings are used to train the model.

The model takes a PDF file(Bug Report) as input and looks for the presence/absence of various attributes of a bug report, such as the description of the bug, the severity level, the priority, and the category of the bug. These attributes can be used to build a feature set that represents the bug report.

The output of the model can be a numerical value that represents the clarity of the bug report (in % ranging from 0 to 100 where 0 % indicates complete lack of clarity and 100 % indicates perfect clarity so that the Developer on seeing the Bug Report can quickly identify the issue and fix it asap. This score can be used by Developers and testers to prioritize bug fixes and improve the overall quality of the software. The trained Linear regression model provided **94% Regression score** with just **0.006 Error**.

In addition, the model also provides pre-defined suggestions to the Tester who has created the Report in improvising the Bug Report.

# Workflow of the entire process
1) The Tester uploads his/her Bug Report in the website (which only accepts PDF files).
2) The PDF file is taken as input and the presence/absence of each Topics and subtopics such as 'Description', 'Steps to Reproduce the bug', 'Priority', 'Severity', 'Test Environment' and the presence/absence of Screenshot of the bug are analysed by iterating to each word present in each page of the PDF file using PyPDF2 Library.
3) These attributes are updated to an array in which array[0] corresponds to Steps to Reproduce the bug, array[1] corresponds to Specificity of the bug and so on. The values in this array takes either 0 or 1 where 0 indicates that the respective attribute is not present in the uploaded PDF file and 1 indicates that the respective attribute is present in the uploaded PDF file.
4) The array is taken as a test data and it is passed on the Linear Regression Model which is trained on 2^n rows of data where 'n' is the number of possible attributes and the ML model predicts the % of Clarity in the uploaded PDF file and sends the value to the FrontEnd using Flask. 

# Results
![image](https://github.com/Vimalan-S/Bug-Report-Analysis-using-Machine-Learning/assets/105377221/fe2f3681-9e6f-48dc-8641-054e6f7124d5)
<br> After uploading the Bug report file to the site, it displays the Clarity of the bug report along with a suggestion to further improve the Clarity of the Bug report.


