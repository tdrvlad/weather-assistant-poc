#!/bin/bash

# Start the database that holds the chat histories
./start_db.sh
sleep 5

# Start the Assistant API
export PYTHONPATH=${PYTHONPATH}:$cwd
python3 ./api/api.py &
streamlit run ./ui/ui.py &
