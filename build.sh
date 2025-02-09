#!/bin/bash

# Run generate.py in the current directory
if [ -f "generate.py" ]; then
    echo "Running generate.py..."
    python3 generate.py
else
    echo "generate.py not found!"
fi

# Iterate over all directories in the current directory
for dir in */ ; do
    # Check if it's a directory and contains create.py
    if [ -d "$dir" ] && [ -f "$dir/create.py" ]; then
        echo "Running create.py inside $dir..."
        (cd "$dir" && python3 create.py)
    fi
done

echo "✅ All scripts executed."

