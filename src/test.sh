#!/bin/bash

# Activate virtual environment
# source /path/to/activate/myenv/bin/activate

# Hide cursor
tput civis

# Show cursor when you exit
trap 'tput cnorm' EXIT

# Run python script to show clock
python main.py