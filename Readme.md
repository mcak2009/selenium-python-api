# Python BDD API Selenium Project

This project demonstrates Behavior Driven Development (BDD) for API testing using Python, Behave, and Selenium.

# Project Objectives

- Practice BDD with Python and Gherkin syntax.
- Automate REST API testing using `requests`.

## Tech Stack

- Python
- Behave
- Requests
- Selenium
- Pytest

## Project Structure

Selenium_Python_API_BDD_Project/
│
├── features/
│ ├── countries.feature
│ └── weather.feature
│ ├── steps/
│ │ ├── country_steps.py
│ │ └── weather_steps.py
│ └── environment.py
├── venv/ # Python virtual environment
├── requirements.txt
└── README.md

## Setup & Execution

# Clone the Repository

git clone https://github.com/your-username/python-bdd-api-selenium.git
cd python-bdd-api-selenium

# 2. Create & Activate Virtual Environment

python -m venv venv

Activate - On Windows PowerShell
.\venv\Scripts\Activate.ps1

Or on CMD
venv\Scripts\activate.bat

# 3. Install Dependencies

pip install -r requirements.txt

4. Run the Tests

# Run all tests with print statements visible
python -m behave --no-capture -v



