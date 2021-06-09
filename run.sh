#!/bin/bash

echo "Starting script to get data"
python index.py

echo "Starting server for UI"
python -m http.server 8000
