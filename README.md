# Membership Management System

A FastAPI-based membership management system with PostgreSQL database, featuring automated attendance tracking with database triggers.

## Features

- Member Management
- Plan Management  
- Subscription Management
- Attendance Tracking with automatic `total_checkins` increment via PostgreSQL trigger

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL / SQLite
- **ORM**: SQLModel
- **Migrations**: Alembic
- **Python**: 3.10+

## Setup Instructions

### 1. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -e .
```

### 3. Configure Database

Create a `.env` file in the project root:

**For PostgreSQL:**
```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/dbname
```

**For SQLite (Development):**
```env
DATABASE_URL=sqlite+aiosqlite:///./membership.db
```

### 4. Create Tables & Apply Trigger

Run Alembic migrations to create all tables and apply the database trigger:

```bash
alembic upgrade head
```

This will:
- Create all database tables (`members`, `plans`, `subscriptions`, `attendance`)
- Create the PostgreSQL trigger that auto-increments `total_checkins`

**Trigger Location:** `alembic/versions/333bdd934768_add_attendance_trigger.py`

### 5. Start the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs

## Example Requests

### 1. Create a Member

```bash
curl -X POST "http://localhost:8000/members/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "1234567890"
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "join_date": "2025-11-27T16:58:50.135544",
  "status": "active",
  "total_checkins": 0
}
```

### 2. Create a Plan

```bash
curl -X POST "http://localhost:8000/plans/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Monthly Premium",
    "price": 1500,
    "duration_days": 30
  }'
```

### 3. Create a Subscription

```bash
curl -X POST "http://localhost:8000/subscriptions/" \
  -H "Content-Type: application/json" \
  -d '{
    "member_id": 1,
    "plan_id": 1
  }'
```

### 4. Create Attendance (Triggers Auto-Increment!)

```bash
curl -X POST "http://localhost:8000/attendance/" \
  -H "Content-Type: application/json" \
  -d '{
    "member_id": 1
  }'
```

**Response:**
```json
{
  "id": 1,
  "member_id": 1,
  "check_in": "2025-11-27T17:30:15.500000"
}
```

**What happens:** The database trigger automatically increments `total_checkins` for member #1!

### 5. Verify Trigger - Get Member

```bash
curl -X GET "http://localhost:8000/members/1"
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "join_date": "2025-11-27T16:58:50.135544",
  "status": "active",
  "total_checkins": 1  ← Automatically incremented!
}
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/members/` | Create member |
| `GET` | `/members/` | Get all members |
| `POST` | `/plans/` | Create plan |
| `GET` | `/plans/` | Get all plans |
| `POST` | `/subscriptions/` | Create subscription |
| `GET` | `/subscriptions/member/{member_id}/current-subscriptions` | Get current subscriptions by member |
| `POST` | `/attendance/` | Create attendance (check-in) |
| `GET` | `/attendance/{member_id}` | Get attendance by member |

## Database Trigger

The PostgreSQL trigger is located in: `alembic/versions/333bdd934768_add_attendance_trigger.py`

It automatically increments the `total_checkins` column in the `members` table whenever a new attendance record is inserted.

## Optional: Seed Database

To populate the database with sample data:

```bash
python -m app.lib.seed
```

This creates sample members, plans, and subscriptions for testing.
