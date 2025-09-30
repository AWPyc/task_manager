# Task Manager API 🚀

A simple project management and task tracking API built with **Django + DRF**, using **PostgreSQL** and containerized with **Docker**.
Supports JWT & session authentication, role-based permissions, project visibility, task assignment, pagination, throttling, and CI/CD integration.

---

## ⚙️ Features

* User registration & authentication (JWT + Session)
* Projects with visibility rules (`restricted` / `no_restrictions`)
* Tasks with assignment, deadlines, and status updates
* Custom permissions:

  * Only project owners can modify projects
  * Tasks visible only to creators, assignees, or project members
* Filtering, search & ordering for tasks
* Pagination & request throttling
* PostgreSQL database
* Dockerized environment with **docker-compose**
* CI/CD pipeline (GitHub Actions)

---

## 🐳 Run with Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/AWPyc/task_manager.git
   cd task_manager
   ```

2. Copy example environment and adjust values:

   ```bash
   cp .env_example .env
   ```

   Adjust values in `.env`:

   ```
   DEBUG=true
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

   POSTGRES_USER=example_user
   POSTGRES_PASSWORD=example_passwd
   POSTGRES_DB=example_db
   ```

3. Build and run:

   ```bash
   docker-compose up --build
   ```

4. Migrations should be done automatically, if not run them manually (only needed first time if container didn’t do it):

   ```bash
   docker-compose run migrate
   ```

5. Access API at:

   * `http://localhost:8000/`
   * Admin panel: `http://localhost:8000/admin/`

---

## 🔑 Authentication

* **JWT**:

  * Obtain: `POST /api/token/ { "username": "...", "password": "..." }`
  * Refresh: `POST /api/token/refresh/`
  * Use: add `Authorization: Bearer <your_token>` header

* **Session auth** works for browsing API in Django templates.

---

## 📂 Project Structure

```
.github/            # CI file
core/               # Main Django project
projects/           # Projects app
tasks/              # Tasks app
users/              # Users app
entrypoints/        # Entrypoint scripts for Docker
Dockerfile
docker-compose.yml
.env_example
requirements.txt
```

---

## 🧪 Tests

To run tests locally:

Enter the container:

`docker exec -it django-backend bash`

Run tests:

`pytest`

---
