# Fast API Rest Server for Raspberry Pi

This is a simple REST server for Raspberry Pi that uses FastAPI and Uvicorn.

## Requirements

- Python 3.8 or higher
- Raspberry Pi
- FastAPI

## Installation

```bash
pip install -r requirements.txt
```

## Run Server(Development)

```bash
fastapi dev main.py
```

## Run Server(Production)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```