# 🍎 Mac Setup Guide - Sign Language Translator

## ⚡ QUICK MAC SETUP (5 Minutes)

---

## **Step 1: Install Homebrew (Package Manager)**

Open Terminal and run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:
```bash
brew --version
```

---

## **Step 2: Install Required Tools**

```bash
# Install Python 3.12
brew install python@3.12

# Install Enchant (for spell checking)
brew install enchant

# Install XCode command line tools (needed for some packages)
xcode-select --install
```

Verify Python:
```bash
python3 --version
```

---

## **Step 3: Clone Project from GitHub**

```bash
# Choose a folder and navigate there
cd ~/Documents

# Clone repository
git clone https://github.com/Surajkumarjha094/Sign-Language-Prediction.git

# Enter project folder
cd Sign-Language-Prediction/Sign-Language-Translator-to-Text-and-Speech
```

---

## **Step 4: Create Virtual Environment (RECOMMENDED)**

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) at the start of terminal
```

---

## **Step 5: Install Python Dependencies**

```bash
# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

If you get errors with TensorFlow on Apple Silicon (M1/M2/M3):
```bash
pip install tensorflow-macos
pip install tensorflow-metal  # GPU acceleration
```

---

## **Step 6: Fix Camera Permission (IMPORTANT! ⚠️)**

1. Open **System Preferences** → **Security & Privacy** → **Camera**
2. Make sure **Terminal** (or your Python IDE) is listed and allowed
3. Or run this in Terminal:
```bash
# Run the app once, it will ask for permission
python3 final_pred.py
```

---

## **Step 7: Run the Application!**

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the application
python3 final_pred.py
```

---

## ✅ **Expected Output**

You should see:
- ✓ Loading model message in terminal
- ✓ Tkinter window opens (1280×720)
- ✓ Camera feed shows live video
- ✓ Hand skeleton draws in real-time
- ✓ Text accumulates as you make gestures

---

## 🔧 **Troubleshooting**

### Problem: `ModuleNotFoundError: No module named 'keras'`
```bash
pip install --upgrade tensorflow keras
```

### Problem: Camera not working
```bash
# Reset camera permissions
# System Preferences → Security & Privacy → Camera → Remove and re-add Terminal
```

### Problem: Enchant dictionary error
```bash
brew reinstall enchant
```

### Problem: OpenCV (cv2) error
```bash
pip install --upgrade opencv-python
```

### Problem: PyTTSx3 not working
```bash
pip uninstall pyttsx3
pip install pyttsx3
```

### Problem: Very slow performance
- Check if other apps are using camera
- Close Chrome/other browsers
- Ensure good lighting for hand detection

---

## 📱 **For Apple Silicon (M1/M2/M3/M4)**

If you have an Apple Silicon Mac:

```bash
# Install TensorFlow with Metal support
pip install tensorflow-macos tensorflow-metal

# This enables GPU acceleration for faster hand detection
```

---

## 🎯 **Quick Reference Commands**

```bash
# Activate virtual environment
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Run application
python3 final_pred.py

# Update dependencies
pip install --upgrade -r requirements.txt

# Check installed packages
pip list
```

---

## ✨ **Features Working on Mac**

✅ Real-time hand gesture recognition (30 FPS)  
✅ Character accumulation into sentences  
✅ Text-to-speech audio output  
✅ Spell checking with suggestions  
✅ Delete word button  
✅ Confidence score display  
✅ Hand detection indicator  
✅ Live FPS counter  

---

## 💡 **Tips for Best Performance**

1. **Good Lighting**: Ensure well-lit environment for accurate hand detection
2. **Camera Position**: Keep camera 30-50cm away from your hand
3. **Clear Gestures**: Make distinct hand shapes for letter recognition
4. **Close Apps**: Close browser/Zoom if running slowly
5. **Use Wired Keyboard**: For smooth text input

---

## 🆘 **Still Having Issues?**

1. Check Python version: `python3 --version` (should be 3.10+)
2. Check pip packages: `pip list | grep -i tensorflow`
3. Test camera: Open Photo Booth to verify camera works
4. Check permissions: System Settings → Security & Privacy → Camera

---

**Made with ❤️ for Mac Users | Ready to deploy on other Macs!**
