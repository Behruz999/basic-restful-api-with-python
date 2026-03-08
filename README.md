# RestPy

## Description

Basic fast api setup for web app, can be customized for any needs

## Tech Stack

- Python 3.12
- FastAPI

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements/dev.txt
```

✅ Recommended Architecture (Scalable, Versioned API)
```
project_root/
├── app/
│   ├── __init__.py
│   ├── main.py              # App entrypoint
│   │
│   ├── core/                # Core configuration
│   │   ├── config.py        # Settings management
│   │   ├── security.py
│   │   └── constants.py
│   │
│   ├── api/
│   │   ├── deps.py          # Shared dependencies
│   │   └── v1/
│   │       ├── router.py
│   │       ├── endpoints/
│   │       │   ├── users.py
│   │       │   └── items.py
│   │       └── schemas/
│   │           ├── user.py
│   │           └── item.py
│   │
│   ├── services/            # Business logic layer
│   │   ├── user_service.py
│   │   └── item_service.py
│   │
│   ├── models/              # Database models (ORM)
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── repositories/        # Data access layer (optional but ideal)
│   │   ├── user_repo.py
│   │   └── item_repo.py
│   │
│   └── db/
│       ├── base.py
│       ├── session.py
│       └── migrations/
│
├── tests/
│   ├── test_users.py
│   └── test_items.py
│
├── .env
├── pyproject.toml
├── requirements.txt
└── README.md
```