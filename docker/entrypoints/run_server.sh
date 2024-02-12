#!/bin/bash
python -m uvicorn main:deposit_app --host 0.0.0.0 --port 8000 --reload