## API Endpoints

This section documents all available **Quizly REST API endpoints**, grouped by domain.
Authentication is handled via **JWT tokens stored in HttpOnly cookies**.

---

### Authentication

#### Register

**POST** `/api/register/`

Registers a new user account.

**Request Body**

```json
{
  "username": "your_username",
  "password": "your_password",
  "confirmed_password": "your_confirmed_password",
  "email": "your_email@example.com"
}
```

**Success Response** – _201 Created_

```json
{
  "detail": "User created successfully!"
}
```

**Status Codes**

- 201 – User successfully created
- 400 – Invalid request data
- 500 – Internal server error

**Permissions:** None  
**Rate Limit:** None

---

#### Login

**POST** `/api/login/`

Authenticates the user and sets `access_token` and `refresh_token` as **HttpOnly cookies**.

**Request Body**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Success Response** – _200 OK_

```json
{
  "detail": "Login successfully!",
  "user": {
    "id": 1,
    "username": "your_username",
    "email": "your_email@example.com"
  }
}
```

**Status Codes**

- 200 – Login successful
- 401 – Invalid credentials
- 500 – Internal server error

**Permissions:** None  
**Rate Limit:** None  
**Notes:** Sets authentication cookies.

---

#### Logout

**POST** `/api/logout/`

Logs out the user and invalidates all authentication tokens.

**Request Body**

```json
{}
```

**Success Response** – _200 OK_

```json
{
  "detail": "Log-Out successfully! All Tokens will be deleted. Refresh token is now invalid."
}
```

**Status Codes**

- 200 – Logout successful
- 401 – Not authenticated
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None  
**Notes:** Deletes `access_token` and `refresh_token` cookies.

---

#### Refresh Token

**POST** `/api/token/refresh/`

Renews the access token using the refresh token stored in cookies.

**Request Body**

```json
{}
```

**Success Response** – _200 OK_

```json
{
  "detail": "Token refreshed",
  "access": "new_access_token"
}
```

**Status Codes**

- 200 – Token refreshed
- 401 – Missing or invalid refresh token
- 500 – Internal server error

**Permissions:** Refresh-token cookie required  
**Rate Limit:** None  
**Notes:** Sets a new `access_token` cookie.

---

### Quiz Management

Endpoints for creating, managing and retrieving quizzes.
All routes require **authentication**.

---

#### Create Quiz

**POST** `/api/createQuiz/`

Creates a new quiz based on a YouTube video URL.

**Request Body**

```json
{
  "url": "https://www.youtube.com/watch?v=example"
}
```

**Success Response** – _201 Created_

```json
{
  "id": 1,
  "title": "Quiz Title",
  "description": "Quiz Description",
  "video_url": "https://www.youtube.com/watch?v=example",
  "questions": [
    {
      "id": 1,
      "question_title": "Question 1",
      "question_options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Option A"
    }
  ]
}
```

**Status Codes**

- 201 – Quiz created
- 400 – Invalid URL or request data
- 401 – Not authenticated
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None

---

#### Get All Quizzes

**GET** `/api/quizzes/`

Returns all quizzes belonging to the authenticated user.

**Success Response** – _200 OK_

```json
[
  {
    "id": 1,
    "title": "Quiz Title",
    "video_url": "https://www.youtube.com/watch?v=example",
    "questions": []
  }
]
```

**Status Codes**

- 200 – Success
- 401 – Not authenticated
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None

---

#### Get Quiz by ID

**GET** `/api/quizzes/{id}/`

Retrieves a specific quiz owned by the authenticated user.

**Status Codes**

- 200 – Quiz retrieved
- 401 – Not authenticated
- 403 – Access denied (not owner)
- 404 – Quiz not found
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None

---

#### Update Quiz (Partial)

**PATCH** `/api/quizzes/{id}/`

Updates one or more fields of a quiz.

**Request Body**

```json
{
  "title": "Updated Title"
}
```

**Status Codes**

- 200 – Quiz updated
- 400 – Invalid data
- 401 – Not authenticated
- 403 – Access denied
- 404 – Quiz not found
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None

---

#### Delete Quiz

**DELETE** `/api/quizzes/{id}/`

Deletes a quiz and all related questions permanently.

**Success Response** – _204 No Content_

**Status Codes**

- 204 – Quiz deleted
- 401 – Not authenticated
- 403 – Access denied
- 404 – Quiz not found
- 500 – Internal server error

**Permissions:** Authenticated user  
**Rate Limit:** None  
**Warning:** This action is irreversible.
