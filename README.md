# Bug-Report-Analysis-using-Machine-Learning

A Linear Regression model has been trained to analyze bug reports and provide an output that indicates the clarity of the report (in %). 
The model is built using a supervised learning approach, where historical data on bug report's attributes such as the presence of Description about the bug, Steps to reproduce the bug, Screenshot attachments of the bug, Presence of Priority and severity of the bug and their Clarity ratings are used to train the model.

The model takes a PDF file(Bug Report) as input and looks for the presence/absence of various attributes of a bug report, such as the description of the bug, the severity level, the priority, and the category of the bug. These attributes can be used to build a feature set that represents the bug report.

The output of the model can be a numerical value that represents the clarity of the bug report (in % ranging from 0 to 100 where 0 % indicates complete lack of clarity and 100 % indicates perfect clarity so that the Developer on seeing the Bug Report can quickly identify the issue and fix it asap. This score can be used by Developers and testers to prioritize bug fixes and improve the overall quality of the software.

In addition, the model also provides pre-defined suggestions to the Tester who has created the Report in improvising the Bug Report.
