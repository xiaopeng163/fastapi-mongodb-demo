#!/bin/sh

uvicorn app:app --reload --host=0.0.0.0

#uvicorn app.main:app --reload --host=0.0.0.0 --log-level critical