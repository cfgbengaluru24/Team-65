# U&I Trust (CFG2024)-(BNG)

This project involves creating a web application using Django, designed to handle various functionalities such as user management, data processing, and more.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

This Django project involves handling various models like Timetable, Teacher, Course, Room, Society, and Booking using an SQLite3 database. The project features an upload page for handling data inputs and buttons for downloading templates and existing data. It is designed to be deployed on Vercel.

## Features

- Upload data to populate database
- Download templates and existing data
- User authentication and management
- Data processing and storage using SQLite3
- Deployable on Vercel

## Requirements

- Python 3.x
- Django 3.x or higher
- SQLite3 (default database for Django)
- Dependencies listed in `requirements.txt`

## Installation

Follow these steps to set up the project locally:

```bash
# Clone the repository
git clone https://github.com/cfgbengaluru24/Team-65.git

# Navigate to the project directory
cd Team-65

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
cd venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# write the migrations
python manage.py makemigrations

# Set up the database
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
 <br /> <br /> The code ("Code") in this repository was created solely by the student teams during a coding competition hosted by JPMorgan Chase Bank, N.A. ("JPMC"). JPMC did not create or contribute to the development of the Code. This Code is provided AS IS and JPMC makes no warranty of any kind, express or implied, as to the Code, including but not limited to, merchantability, satisfactory quality, non-infringement, title or fitness for a particular purpose or use.