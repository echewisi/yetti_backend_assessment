# YETTI BACKEND TEST

A brief description of your project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)


## Installation

Follow these steps to set up and run the project locally.

1. Clone the repository:

   ```bash
   git clone https://github.com/echewisi/yetti_backend_assessment
   cd yetti_backend_assessment

2. Create a virtual environment (optional but recommended):
    python -m venv venv

3. activate the virtual environment:
    windows:
        venv\Scripts\activate
    macos and linux:
        source venv/bin/activate

4. Install project dependencies:
    pip install -r requirements.txt

## Usage

1. Apply migrations to set up the database:
   py manage.py makemigrations
   python manage.py migrate

2. create superuser(admin) account:
    python manage.py createsuperuser

3. run development server:
    python manage.py runserver

4. Access the application in your web browser at http://localhost:8000.

## Testing
1. Ensure that you are in the project's root directory and your virtual environment is activated.
2. Run the tests using the following command:
   python manage.py test




