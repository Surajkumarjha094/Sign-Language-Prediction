#!/bin/bash

# Sign Language Translator - Mac Run Script
# This script activates the virtual environment and runs the application

echo "🍎 Sign Language Translator - Mac Edition"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Check if model file exists
if [ ! -f "cnn8grps_rad1_model.h5" ]; then
    echo "❌ ERROR: Model file 'cnn8grps_rad1_model.h5' not found!"
    echo "Please ensure you're in the correct directory with the model file."
    deactivate
    exit 1
fi

# Check if AtoZ_3.1 folder exists
if [ ! -d "AtoZ_3.1" ]; then
    echo "⚠️  Warning: Training data folder 'AtoZ_3.1' not found."
    echo "Application will still work, but can't generate new training data."
fi

# Display startup information
echo ""
echo "📊 System Information:"
echo "Python Version: $(python3 --version)"
echo "Virtual Environment: venv"
echo ""

# Run the application
echo "🚀 Starting Sign Language Translator..."
echo "=========================================="
echo ""
echo "💡 Tips:"
echo "  - Good lighting is important for accurate hand detection"
echo "  - Keep camera 30-50cm away from your hand"
echo "  - Make distinct hand gestures for letters"
echo ""
echo "Ctrl+C to exit"
echo "=========================================="
echo ""

python3 final_pred.py

# Deactivate virtual environment on exit
deactivate
