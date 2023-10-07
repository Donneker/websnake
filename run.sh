#!/usr/bin/env bash

# a) Install dependencies
#python3 -m venv venv
#source venv/bin/activate
#pip install -r requirements.txt

# b) Run all necessary parts of the codebase
source venv/Scripts/activate
echo open browser to http://localhost:8000 and start playing
echo once the skript runs, stop it with CTRL+C

FLASK_APP=/c/local/git/gpt-engineer/projects/websnake/workspace/backend/server.py
export FLASK_APP
flask run &
flask_pid=$!
echo FLASK started with flask_pid=${flask_pid}

# stop flask, when python frontend_server.py is stopped with CTRL+C
trap "if ps -p ${flask_pid} > /dev/null; then
    echo Killing process with PID ${flask_pid}
    kill ${flask_pid}
  else
    echo FLASK Process is not more running.
  fi" EXIT

cd frontend
python frontend_server.py 8000
