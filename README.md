# API Documentation

This document provides information on the API endpoints and their usage for the provided Django application. The application exposes several endpoints to manage student assignments and report on their progress.

## Table of Contents

- [Endpoints](#endpoints)
  - [Create or Update Student Attempt](#create-or-update-student-attempt)
  - [Get Student Assignment Report](#get-student-assignment-report)
  - [Get Student Assignment Report by Group](#get-student-assignment-report-by-group)

## Endpoints

### Create or Update Student Attempt

**Endpoint:** `POST /reporter/attempt/`

#### Description

This endpoint allows you to create or update a student's attempt for a specific assignment task.

#### Request

- `github` (string, required): The GitHub username of the student.
- `task` (string, required): The name of the task within the assignment.
- `assignment` (string, required): The name of the assignment.
- `is_correct` (boolean, required): Indicates whether the student's attempt is correct.

#### Response

- `success` (boolean): Indicates whether the attempt was successfully created or updated.

#### Example

```json
Request:
POST /attempt/
{
  "github": "student_username",
  "task": "task_name",
  "assignment": "assignment_name",
  "is_correct": true
}

Response:
HTTP 201 Created
{
  "success": true
}
```

### Get Student Assignment Report by Group

**Endpoint:** `GET /reporter/by-group/`

#### Description

This endpoint retrieves a report on student assignment progress for a specific assignment within a specified group.

#### Request

- `assignment_name` (string, required): The name of the assignment for which you want to retrieve the report.
- `group_name` (string, required): The name of the group for which you want to retrieve the report.

#### Response

An array of objects, each containing the following information:

- `first_name` (string): The first name of the student.
- `last_name` (string): The last name of the student.
- `github` (string): The GitHub username of the student.
- `tasks` (array): An array of objects, each containing task-related information:
  - `name` (string): The name of the task.
  - `attempts` (integer): The total number of attempts made by the student for the task.
  - `is_correct` (boolean): Indicates whether the student's latest attempt is correct.

#### Example

```json
Request:
GET /by-group/?assignment_name=assignment_name&group_name=group_name

Response:
HTTP 200 OK
[
  {
    "first_name": "John",
    "last_name": "Doe",
    "github": "johndoe",
    "tasks": [
      {
        "name": "Task 1",
        "attempts": 2,
        "is_correct": true
      },
      {
        "name": "Task 2",
        "attempts": 1,
        "is_correct": false
      }
    ]
  },
  // ... (more student reports within the group)
]
```

Please note that you should replace `assignment_name` and `group_name` with the actual assignment and group names in your requests.