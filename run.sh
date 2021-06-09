#!/bin/bash

python index.py
cd www
python -m http.server 8000
