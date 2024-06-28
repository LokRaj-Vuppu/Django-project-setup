# Django Project Setup Guide

This repository contains a Django project integrated with PostgreSQL, pgAdmin, Celery, Celery Beat, Redis, Flower and Nginx managed using Docker Compose for easy setup and deployment.

- Nginx as a reverse proxy for Dango app.
- Nginx to cache the static and media files using Nginx.
- Celery to offload tasks from the main request/response cycle within Django.
- Celery beat for scheduling periodic tasks.
- Flower to monitor the celery tasks.
- Redis as a message broker for celery and cache.
- Postgres and pgAdmin for database management.



## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (3.x recommended)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Run Docker

```bash
docker-compose build
docker-compose run
```
