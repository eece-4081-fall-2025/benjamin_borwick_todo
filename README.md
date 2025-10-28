# ToDo MVP – Django TDD Project

### Author  
Benjamin Borwick  

### Course  
EECE 4081 – Software Engineering  
Fall 2025  

---

### Epic (User Story)  
As a user, I want to create a task with a title and notes so that I can remember what to do.

This feature allows users to record and view tasks using a simple web interface.

---

### Task Breakdown  
| Task | Description |
|------|--------------|
| Task 1 | Initialize Django project and `todos` app |
| Task 2 | Create `Task` model with title and notes |
| Task 3 | Write tests for `Task` model (title required) |
| Task 4 | Create task form, views, URLs, and templates |
| Task 5 | Write tests for `task_create` and `task_list` views |
| Task 6 | Run and pass all tests using Test-Driven Development (TDD) |

---

### Test-Driven Development (TDD) Evidence  
| Cycle | Phase | Commit Message | Description |
|--------|--------|----------------|--------------|
| 1 | RED | TDD Cycle 1 (RED): failing test for Task model (title required) | Added test for missing title validation |
| 1 | GREEN | TDD Cycle 1 (GREEN): implement Task model to satisfy title-required test | Implemented Task model and passed test |
| 2 | RED | TDD Cycle 2 (RED): tests for task create view (GET + POST valid/invalid) | Added failing view tests |
| 2 | GREEN | TDD Cycle 2 (GREEN): implement form/view/urls/templates to pass create-task tests | Implemented TaskForm, views, URLs, and templates |
| Fix | - | Fix template lookup: add BASE_DIR/templates to TEMPLATES.DIRS | Updated settings to correctly load templates |

Each RED → GREEN cycle represents one full test-driven development iteration.  
All tests pass successfully.

---

### How to Run Locally  

# Clone the repository
git clone https://github.com/eece-4081-fall-2025/benjamin_borwick_todo.git
cd benjamin_borwick_todo

# Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the automated tests
python manage.py test

# Start the development server
python manage.py runserver

Then open a browser and go to:
http://127.0.0.1:8000/
