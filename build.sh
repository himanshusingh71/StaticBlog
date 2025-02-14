#!/bin/bash

# Iterate over all directories in the current directory
#!/bin/bash

# Path to create.py in the current directory
SOURCE_FILE="create.py"

python3 ol.py "$1"

# Check if create.py exists in the current directory
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: $SOURCE_FILE not found in the current directory!"
    exit 1
fi

# Iterate over all subdirectories
for dir in */ ; do
    # Check if it's a directory and contains create.py
    if [ -d "$dir" ]; then
        DEST_FILE="$dir/create.py"
        
        # Copy create.py to the subdirectory
        cp "$SOURCE_FILE" "$DEST_FILE"
        echo "Replaced $DEST_FILE"
    fi
done

echo "Replacement completed!"



for dir in */ ; do
    # Check if it's a directory and contains create.py
    if [ -d "$dir" ] && [ -f "$dir/create.py" ]; then
        echo "Running create.py inside $dir..."
        (cd "$dir" && python3 create.py)
    fi
done

# Run generate.py in the current directory
if [ -f "generate.py" ]; then
    echo "Running generate.py..."
    python3 generate.py
else
    echo "generate.py not found!"
fi



echo "✅ All scripts executed."

echo "pushing code to main branch"

git add .
git commit -m "code changes"
git push origin main
echo "pushed code successfully"
