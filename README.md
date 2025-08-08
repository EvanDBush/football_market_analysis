#Football Market Analysis


### Setup Instructions:

1. In the command terminal, navigate to the folder you want to download the project.
2. run the command:
``` git clone https://github.com/EvanDBush/football_market_analysis.git ```
to download from github [here] (https://github.com/EvanDBush/football_market_analysis) 
3. Open the folder in your IDE of choice to run and review the project files.
4. In the terminal, create a virtual environment by running the command:
``` python -m venv myenv ``` you can replace 'myenv' with the name of your choice. 
5. Activate the envirionment according to your command shell. For windows use the command:
```myenv\Scripts\activate``` For macOS/linux use:
```source myenv/bin/activate ``` When activated, most command shells will indicate the virtual environment name in parenthesis.
6. Install the project dependencies using the command: 
```pip install -r requirements.txt``` The project is ready to be run.

### Project Overview

    This project uses data tables on individual players and clubs to calculate the market value of football (soccer) clubs across Europe.

    Once running, please check out:
    ```project_summary.ipynb``` for data analysis and insights.

### Technologies Used:
    This
    2. Pandas
    3. Seaborn





    





README.md Requirements
Your README.md should serve as a user guide for your project and must include:
Project Setup Instructions
Step-by-step directions on how to download, install, and run your project
Instructions for setting up the virtual environment
You should test this process by cloning your repo into a new folder or onto a different machine
Have others test your project and test theirs. 


Project Overview
A description of what the user should expect from the project once it's running
Assume the reviewer has no coding background, so keep language clear and simple


Technologies Used
List all key tools/libraries used and explain their role in the project
Example: “Pandas was used to clean and manipulate the dataset to identify trends in customer behavior.”
Example: “The project was developed in Jupyter Notebooks to allow for clean, narrative-driven presentation of both code and results.”

Data Handling Requirements
All data must be imported from a public API or using a relative file path (e.g., ./data/file.csv)
Do not use absolute file paths (e.g., C:/Users/YourName/...), as these will not work on other systems
Version Control and GitHub Practices
Your GitHub repository must include at least 10 separate commits
It's best practice to commit every time you complete a work session to avoid data loss
All commits must be made using the command line
Do not use the file uploader, as this will result in project failure

Notebook Guidelines
Use Markdown cells to explain the objective or logic of your code. This doesn't mean annotating every code block, but the narrative should clearly walk the reviewer through your process.
Organize your notebook to be visually appealing and easy to follow:
Remove unused or test code
Present finalized code cleanly and professionally
Use consistent formatting and correct spelling throughout
Apply a cohesive color palette to any visualizations for a polished cohesive appearance.



Environment & Dependencies
Use a virtual environment for your project.
Include a requirements.txt file in your repository.
Only list the libraries required to run your project.
Data Ingestion & Cleaning
 Read your data using one of the following methods:
From a local file
Using a public API
Through web scraping
Perform thorough data cleaning, including:
Handling null or missing values
Normalizing data where applicable
Renaming columns for clarity
Verifying that column data types accurately represent the data
Feature Engineering & Functions
Perform feature engineering by creating at least one new column based on existing data.


Implement at least three custom functions in your code.
Use best practices, including:
Type hinting
Docstrings to explain function purpose and parameters
Database Integration
Store your cleaned data in a SQLite database.
Create at least two tables
Define a primary key for each table to allow joins
Perform a SQL join between your tables to retrieve only the data needed for your visualizations



Visualizations
Create three different plots to illustrate your analysis.
Each plot must be a different type (e.g., bar, line, scatter, etc.)
All plots must include:
A title
Clearly labeled axes
A unified color theme (avoid using default colors)
Optional Enhancements (For Going Above and Beyond)
If you'd like to further showcase your skills and stand out, consider adding one or more of the following optional features to your project. These are not required to pass, but they demonstrate initiative, creativity, and real-world application.
Interactive Dashboard
Build a dashboard to present your findings in an interactive and visually engaging way.
Recommended tool: Tableau (easy to use and great for storytelling)
Alternatives: Power BI, Plotly Dash, or Streamlit (for more technical control)
Project Website
Create a simple website to display your project summary, visualizations, and conclusions.
Basic (Front-End Only): Use HTML/CSS to design a static site showcasing your results.
Advanced (Full Stack): Build a dynamic web app using:
Flask or Django (Python web frameworks)
Combine with your existing data processing scripts
Note: Your project must still meet all required components. Any additional features should use your existing codebase, organized in a way that separates core logic from interface code (e.g., functions and models in reusable modules).
User Interface (UI)
Build a simple user interface for interacting with your analysis or visualizations.
Input fields for user-defined filters (e.g., selecting a region or category)
Buttons to trigger analysis or update graphs
Frameworks: Tkinter, PyQt, Streamlit, or front-end tools like JavaScript with D3.js
Bonus Feature Ideas
Model Deployment: Train and deploy a basic ML model (if applicable) using tools like scikit-learn, TensorFlow, or FastAPI
API Creation: Wrap your cleaned data or analysis in a REST API using Flask or FastAPI
Export Options: Allow users to download visualizations or filtered data as CSV/PDF
Mobile-Friendly Design: If building a web app, ensure it's responsive on mobile devices

Project Summary
You are required to write a clear and concise project summary focused solely on your problem and findings. Avoid detailing the development process—this summary should be written for a non-technical audience and should clearly communicate the insights from your analysis.
Your summary should include:
A description of the problem or question you aimed to solve.
A summary of the key findings from your data analysis.
Any data inconsistencies, limitations, or issues that could have influenced your results.


Helpful references for writing your summary:
DashThis: Analytical Report Guide
Carnegie Mellon Paper Structure Guide (PDF)







https://www.kaggle.com/datasets/davidcariboo/player-scores/data

Installation Instructions:
1. clone the repository

2. download csvs and place in projects data/raw folder

3. set up virtual environment.

4. install dependencies from requirement.txt

5. run cleaning script

6. run uploading script

Project Goals:
    Provide market value overview of clubs in the data available.
        a. Separate by league 
        b. identify top 4 clubs in each league for transfers and  
    Compare top 5 european leagues in player value, club market value and transfer expenditures. 
    explore and prepare entire dataset for a range of future personal projects
    clean the dataset
    create a local db of cleaned data
    prepare sql queries to use on db
    *use kaggle api to download project data automatically

    calculate club market value column in clubs
    find top selling clubs
    find top buying clubs

    find club selling totals by league
    find club buying totals by league

    calculate most valued players by league
    find players total selling fees over career