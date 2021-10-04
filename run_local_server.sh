#!/usr/bin/env bash

cd src
uvicorn app.main:app --reload --host 0.0.0.0
cd ..