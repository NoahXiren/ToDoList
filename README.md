![Python](https://img.shields.io/badge/python-3.12.4-blue
)
![django](https://img.shields.io/badge/django-5.0.7-green
)
![HTML](https://img.shields.io/badge/HTML-ff2700)
![CSS](https://img.shields.io/badge/CSS-ffff00)
![Bootstrap](https://img.shields.io/badge/Bootstrap-8A2BE2)


# ToDo Application
**Description**

This is a simple ToDo application built with Django and Bootstrap. It allows users to manage their tasks by adding, editing, and deleting them.


## screenshots
<div align="center">
  <img src="data/screenshot.png" alt="screenshot_1">
  <h3><em><u>How the todo list works?</u></em></h3>
  <img src="data/1.gif" alt= "gif_1">
</div>
<br>

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as complete or incomplete
  

## Prerequisites

Make sure you have the following installed:

- A modern web browser (e.g., Chrome, Firefox, Safari)
- An internet connection (for fetching external dependencies)


## Installation

**1. Clone the repository:**

``` bash
git clone https://github.com/yourusername/todo-app.git
cd TodoApp
``` 

**2. Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install the dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the development server:**

```bash
python manage.py runserver
```
**5. Open the application in your browser**
```
http://127.0.0.1:8000
```

## Usage

- Add new tasks using the form provided.
- Edit or delete tasks as needed.
- Mark tasks as complete or incomplete.

## Folder Structure
```bash
TODO_APP/
├── Data/
├── manage.py
├── requirements.txt
├── Task/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── Task/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── task_form.html
│   │       ├── task_confirm_delete.html
|   |       └── task_detail.html
│   └── static/
│       └── Task/
│           └──start.css
└── TodoApp/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.