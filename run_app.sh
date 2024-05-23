#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install it from https://www.python.org/ and try again."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi

# Run the application
echo "Running the application..."
nohup python3 main.py > /dev/null 2>&1 &
if [ $? -ne 0 ]; then
    echo "Failed to start the application."
    exit 1
fi

echo "Application started successfully."
exit 0
