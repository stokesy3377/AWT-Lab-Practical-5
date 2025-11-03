# Django Bookstore & Sentiment Analysis

This is a simple, beginner-friendly Django project built for an Advanced Web Technologies Lab File (Practical 5). It demonstrates two key concepts within a single Django project:

1.  **Aim A:** A full CRUD (Create, Read, Update, Delete) application for a Bookstore.
2.  **Aim B:** A simple web app that performs sentiment analysis on user input using the `textblob` library as a local substitute for an external AI/ML API.

## Project Structure
This repository contains a root folder (`AWT-Lab-Practical-5`) which holds the virtual environment (`.venv`) and the Django project (`practical_project`).

```
.
├── .venv/
├── practical_project/
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── manage.py
│   ├── bookstore/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── bookstore/
│   │   │       ├── base.html
│   │   │       ├── book_confirm_delete.html
│   │   │       ├── book_form.html
│   │   │       └── book_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── practical_project/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── sentiment/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── migrations/
│       ├── models.py
│       ├── templates/
│       │   └── sentiment/
│       │       └── analyze.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
└── readme.md
```


## Features
* **Bookstore App:** Add, edit, view, and delete books from a SQLite database.
* **Sentiment App:** Input any text and get a "Positive," "Negative," or "Neutral" result.

## Screenshots

### Bookstore (CRUD)
*The main page showing the **Read** operation, with links for **Create**, **Update**, and **Delete**.*
<img width="530" height="297" alt="image" src="https://github.com/user-attachments/assets/1626655c-cdfb-48fe-a57e-64212029c771" />


### Sentiment Analysis
*Demonstrating the three logic branches of the sentiment analysis model.*


**Positive Test:**

<img width="488" height="458" alt="image" src="https://github.com/user-attachments/assets/66dde8a0-d579-459d-be31-f5f6c7f494ae" />



**Negative Test:**

<img width="554" height="477" alt="image" src="https://github.com/user-attachments/assets/9d6383f2-3c04-4bf2-9a7b-0938ab682796" />



**Neutral Test:**

<img width="557" height="470" alt="image" src="https://github.com/user-attachments/assets/bb0d4a54-e311-4fc3-8e18-9584e6290fd7" />





## Prerequisites
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

## Local Installation and Setup

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**
Open your terminal and clone this repository:
```bash
git clone [https://github.com/stokesy3377/AWT-Lab-Practical-5.git](https://github.com/stokesy3377/AWT-Lab-Practical-5.git)
cd AWT-Lab-Practical-5
```

**2. Create and Activate a Virtual Environment**
It is essential to use a virtual environment to manage dependencies and avoid conflicts.

*On Windows (PowerShell):*
```powershell
# Create the virtual environment (e.g., named ".venv")
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1
```

*On macOS/Linux (Bash/Zsh):*
```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

**3. Install Dependencies**
This project's dependencies are `django` (for the framework) and `textblob` (for sentiment analysis).

*(Note: If a `requirements.txt` file is present, you can just run `pip install -r requirements.txt`. Otherwise, install them manually as shown below.)*
```bash
pip install django textblob
```

**4. Set Up the Database (Crucial Step!)**
This project uses the default `db.sqlite3`. Before you can run the app, you must create the database tables from the models defined in `bookstore/models.py`.

```bash
# First, create the migration file for the bookstore app
python manage.py makemigrations bookstore

# Second, apply all migrations to create the database tables
python manage.py migrate
```
*(Failure to run this step will result in an `OperationalError: no such table: bookstore_book`.)*

**5. Run the Server**
You're all set! Run the Django development server:
```bash
python manage.py runserver
```

**6. View the Project**
Open your browser and navigate to the two app URLs:

* **Bookstore App:** `http://127.0.0.1:8000/bookstore/`
* **Sentiment App:** `http://127.0.0.1:8000/sentiment/`
