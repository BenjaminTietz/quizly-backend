# Quizly Backend – Django REST API

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Quickstart](#quickstart)
4. [Usage](#usage)
5. [Tech Stack](#tech-stack)
6. [Architecture Overview](#architecture-overview)
7. [Authentication Concept](#authentication-concept)
8. [API Documentation](#api-documentation)
9. [CORS & CSRF Configuration](#cors--csrf-configuration)
10. [Local Development Setup](#local-development-setup)
11. [Requirements](#requirements)
12. [Checklist](checklist.pdf)
13. [Contact](#contact)

---

## Introduction

This repository contains the **Django REST backend** for **Quizly**, an educational quiz application that allows users to generate quizzes from YouTube videos.

The backend is responsible for:

- User registration and authentication
- Secure session handling using JWT and HttpOnly cookies
- Quiz creation, storage, and management
- Integration with AI services for transcription and quiz generation
- Providing a REST API consumed by a separate frontend application

The frontend is **not included** in this repository and communicates exclusively via HTTP requests.

---

## Prerequisites

- A V-Server running Ubuntu/Debian
- Docker

Ensure your system is up to date:

```sh
sudo apt update && sudo apt install -y docker.io
```

---

## Quickstart

1. **Install dependencies:**
   ```sh
   sudo apt update && sudo apt install -y docker.io docker-compose git
   ```
2. **Clone the repository:**
   ```sh
   git clone git@github.com:BenjaminTietz/quizzly-backend.git
   cd quizzly-backend
   ```
3. **Generate and configure the .env file:** <br>
   The environment file will be created automatically from env.template.
   Adjust the values to match your setup (optional):
   ```sh
   cp .env.template .env
   nano .env (optional)
   ```
4. **Build the Docker image:**
   ```sh
   docker build -t quizzly-app .
   ```
5. **Create Dockernetwork**
   ```sh
   docker network create quizzly-net
   ```
6. **Start the database container: (optional adjust values to match your setup)**

   ```sh

   postgres
   ```

   💡 On your local development machine, you can add -p 5432:5432 if needed (e.g., for DBeaver).
   ❗ On a public server, do not expose port 5432 to the internet!

7. **Start the app container:(optional adujust values to match your setup)**

   ```sh

   ```

8. **Log in to the admin panel:**
   ```sh
   http://<your-server-ip>:8020/admin
   ```

---

## Tech Stack

- Python 3.1a
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- HttpOnly Cookies
- django-cors-headers
- SQLite (development)
- PostgreSQL (production)

---

## Architecture Overview

The backend follows a **clean and modular architecture**:

- `views.py` – Handles HTTP requests and responses only
- `serializers.py` – Input validation and data transformation
- `utils.py` / `services.py` – Business logic and helpers
- `models.py` – Database models
- `urls.py` – API routing

This separation ensures readability, testability, and maintainability.

---

## Authentication Concept

Authentication is implemented using **JWT tokens stored in HttpOnly cookies**.

### Key principles

- No tokens are stored in localStorage or sessionStorage
- No Authorization headers are used by the frontend
- Tokens are inaccessible to JavaScript (HttpOnly)
- Cross-origin authentication via proper CORS configuration

### Token types

- **Access Token** – short-lived, protects API routes
- **Refresh Token** – long-lived, used to renew access tokens

---

## API Documentation

Detailed API documentation is available in a separate file:

➡️ [API.md](./API.md)

---

## CORS & CSRF Configuration

- `django-cors-headers`
- Explicit allowed origins (including ports)
- `CORS_ALLOW_CREDENTIALS = True`
- Trusted CSRF origins

Correct middleware order is mandatory.

---

## Local Development Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at `http://127.0.0.1:8000`

---

## Requirements

- Python 3.11
- FFmpeg (for audio processing)
- Internet access for external AI services (Gemini API)

---

## Contact

### 👤 Contributors

**Ahmet-Nafi Müftüoglu**

- Portfolio: https://nafi.com
- Mail: mail@nafi.com
- LinkedIn: https://www.linkedin.com/in/ahmet-nafi-m%C3%BCft%C3%BCoglu-9602aa398/

**Benjamin Tietz**

- Portfolio: https://benjamin-tietz.com
- Mail: mail@benjamin-tietz.com
- LinkedIn: https://www.linkedin.com/in/benjamin-tietz/
