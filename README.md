# Flask Note-Taking App

This is a simple **Flask**-based note-taking application using **SQLite** as the database, containerized using **Docker**. The application allows users to take and manage notes. It leverages Flask's SQLAlchemy extension to interact with an SQLite database, with persistence enabled through Docker volumes.

## Features

- Sign Up using email id and password .
- Login using account credentials.
- Create, view, update, and delete notes.
- Uses SQLite for local data storage.
- Development-ready setup using Docker for containerisation.

---

## Prerequisites

Ensure that the following are installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-note-taking-app.git
cd flask-note-taking-app
```

### 2. Set Up and Run with Docker

To build and run the application using Docker, follow these steps:

#### Build the Docker image

```bash
docker-compose build
```

#### Start the application

```bash
docker-compose up
```

This command will:
- Build the Docker image for the Flask app.
- Start the Flask app inside a container.
- Expose the app at [http://localhost:3000](http://localhost:3000).

You can now open your browser and visit `http://localhost:3000` to see the application.

### 3. Access the Application

Visit the following URL in your browser:

```
http://localhost:3000
```
---
## Persistent Data

- Your data is persisted even if the container is stopped or removed.

### 4. Close the Application
```bash
docker compose down
```
This will close the application. Visit `http://localhost:3000` to confirm.
