# JANADEM

JANADEM is a digital platform aimed at increasing civic engagement and improving community life by connecting citizens with local governments. This platform allows citizens to report and solve problems related to damage to public spaces, garbage, and other issues in their cities by uploading/submitting pictures.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)


## About

JANADEM encourages civic engagement by empowering citizens to report community issues, interact with local representatives, and engage in meaningful discussions. The platform simplifies the issue-reporting process with user-friendly features such as photo attachments and real-time updates. It also enhances transparency by allowing users to track the progress of their reported issues and facilitates direct communication with local government representatives. Additionally, JANADEM introduces a points and rewards system to incentivize active participation, issue reporting, and community engagement among citizens.

## Features

- Citizen issue reporting with photo attachments
- Real-time updates on reported issues
- Direct communication with local government representatives
- Points and rewards system to incentivize participation
- Reporting of solved problems by local authorities

## Technologies Used

- Django: ~3.2
- Pillow: 10.0.0
- Django REST Framework: ~3.12.4
- Pandas: 2.1.3
- Django-phonenumber-field: ~5.1.0
- Django-extensions: ~3.1.3
- Django-crispy-forms: ~1.11.2
- Django-sequences: 2.6
- Django-cors-headers: ~3.7.0
- Django-environ: 0.9.0
- Gunicorn: 20.1.0
- Python-dotenv: ~0.21.0
- Requests: ~2.31.0

## Installation

To run the JANADEM backend locally, follow these steps:

### 1. Clone the Repository

First, clone the JANADEM repository to your local machine:

```bash
git clone https://github.com/yernurus/JanaDem.git

Navigate to the project directory and install the required Python dependencies using pip. It's recommended to use a virtual environment to keep your project dependencies isolated:

cd JanaDem
python -m venv vienv  # Create a virtual environment
source vienv/bin/activate  # Activate the virtual environment (for Unix-based systems)
vienv\Scripts\activate  # Activate the virtual environment (for Windows)
pip install -r requirements.txt #This will install all the necessary Python libraries listed in the requirements.txt file.

Run Migrations
Apply the database migrations to create the necessary database tables for JANADEM:
python manage.py migrate

Start the Server
Finally, start the Django development server to run the JANADEM backend:
python manage.py runserver

Access the Project
http://127.0.0.1:8000/
and
127.0.0.1:8000/api/v1/swagger/ui/#/

**Usage**

Once the backend server is running, you can use the JANADEM platform by accessing the provided API endpoints. Refer to the API documentation or project documentation for information on available endpoints and usage examples.

**API Documentation**

The API documentation for this project is available [here](http://janadem.kz/api/v1/swagger/ui/#/). It provides detailed information about the endpoints, request payloads, and responses of the JANADEM API.


Good Luck of using our project!
---

We hope you find JANADEM useful and valuable for improving your community! Thank you for your interest and support in our project. Good luck, and happy civic engagement!

If you have any questions, feedback, or suggestions, feel free to reach out to us via [email](mailto:janademsdu@gmail.com). We'd love to hear from you!

---

