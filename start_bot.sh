#!/bin/bash
pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 python_scripts/bot.py
deactivate
