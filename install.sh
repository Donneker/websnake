#!/usr/bin/env bash

# a) Install dependencies
set -e
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
