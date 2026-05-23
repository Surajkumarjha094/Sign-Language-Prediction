#!/bin/bash

# Sign Language Translator - Mac Automatic Setup Script
# This script handles all Mac setup automatically

echo "🍎 Sign Language Translator - Mac Automatic Setup"
echo "=================================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Check and install Homebrew
echo "${YELLOW}📦 Step 1: Checking Homebrew...${NC}"
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "${GREEN}✓ Homebrew already installed${NC}"
fi
echo ""

# Step 2: Install Python 3.12
echo "${YELLOW}🐍 Step 2: Checking Python 3.12...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "Installing Python 3.12 via Homebrew..."
    brew install python@3.12
    echo ""
    # Create symlink
    brew link python@3.12
else
    echo "${GREEN}✓ Python 3 already installed${NC}"
fi
python3 --version
echo ""

# Step 3: Install Enchant (spell checking)
echo "${YELLOW}📚 Step 3: Installing Enchant...${NC}"
if ! command -v enchant &> /dev/null; then
    echo "Installing Enchant..."
    brew install enchant
else
    echo "${GREEN}✓ Enchant already installed${NC}"
fi
echo ""

# Step 4: Create virtual environment
echo "${YELLOW}🔧 Step 4: Setting up virtual environment...${NC}"
if [ -d "venv" ]; then
    echo "${GREEN}✓ Virtual environment already exists${NC}"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "${GREEN}✓ Virtual environment created${NC}"
fi
echo ""

# Step 5: Activate and upgrade pip
echo "${YELLOW}⚡ Step 5: Upgrading pip...${NC}"
source venv/bin/activate
pip install --upgrade pip setuptools wheel
echo ""

# Step 6: Install dependencies
echo "${YELLOW}📥 Step 6: Installing Python packages...${NC}"
echo "This may take 3-5 minutes..."
pip install -r requirements.txt

# Check if Apple Silicon (M1/M2/M3/M4)
if [[ $(uname -m) == 'arm64' ]]; then
    echo ""
    echo "${YELLOW}🍎 Apple Silicon detected (M1/M2/M3/M4)${NC}"
    echo "Installing Metal GPU support for faster performance..."
    pip install tensorflow-macos tensorflow-metal
fi
echo ""

# Step 7: Verify installation
echo "${YELLOW}✅ Step 7: Verifying installation...${NC}"
python3 -c "import tensorflow; print(f'✓ TensorFlow {tensorflow.__version__}')"
python3 -c "import cv2; print(f'✓ OpenCV {cv2.__version__}')"
python3 -c "import keras; print(f'✓ Keras {keras.__version__}')"
python3 -c "import pyttsx3; print('✓ PyTTSx3')"
python3 -c "import enchant; print('✓ Enchant')"
python3 -c "import cvzone; print('✓ CVZone')"
echo ""

# Step 8: Check model file
echo "${YELLOW}🤖 Step 8: Checking model file...${NC}"
if [ -f "cnn8grps_rad1_model.h5" ]; then
    echo "${GREEN}✓ Model file found: cnn8grps_rad1_model.h5${NC}"
else
    echo "${RED}✗ Model file NOT found!${NC}"
fi
echo ""

# Complete
echo "${GREEN}=========================================="
echo "✅ Setup Complete! Ready to run!"
echo "==========================================${NC}"
echo ""
echo "📝 Next steps:"
echo ""
echo "1️⃣  CAMERA PERMISSION (Important!):"
echo "   System Settings → Security & Privacy → Camera"
echo "   Make sure Terminal is allowed to access camera"
echo ""
echo "2️⃣  Run the application:"
echo "   bash run_app.sh"
echo ""
echo "3️⃣  Or manually:"
echo "   source venv/bin/activate"
echo "   python3 final_pred.py"
echo ""
echo "💡 Tip: For best performance, keep good lighting"
echo "        and make clear hand gestures!"
echo ""
