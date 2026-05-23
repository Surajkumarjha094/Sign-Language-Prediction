# 🚀 HOW TO RUN THE APPLICATION

## Quick Start Methods

### Method 1: Using Batch File (EASIEST) ✅
Simply double-click:
```
run_app.bat
```
- Handles all checks automatically
- Shows error messages clearly
- Best for Windows users

### Method 2: Using PowerShell
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy Bypass -File run_app.ps1
```
- More detailed feedback
- Better error handling
- Cross-platform compatible

### Method 3: Direct Python Command
Open Command Prompt and run:
```bash
python final_pred.py
```
- Direct method
- Shows all output
- Good for debugging

### Method 4: From Any Directory
```bash
python "path\to\Sign-Language-Translator-to-Text-and-Speech\final_pred.py"
```

---

## Troubleshooting "Access Denied" Error

### If you still see "Access is denied":

**Option A: Reset File Permissions**
```bash
icacls final_pred.py /reset
```

**Option B: Run as Administrator**
- Right-click `run_app.bat`
- Select "Run as administrator"

**Option C: Try Alternative Location**
```bash
# Copy file to temp location
copy final_pred.py "%temp%\final_pred.py"
python "%temp%\final_pred.py"
```

**Option D: Clear Python Cache**
```bash
# Remove Python cache
rmdir /s __pycache__
python final_pred.py
```

---

## What to Expect When Running

1. **Initialization (5-10 seconds)**
   - TensorFlow loading messages (normal)
   - Model loading
   - GUI framework initialization

2. **GUI Window Opens (1280x720)**
   - Dark background with title
   - Camera feed on left (480x360)
   - Hand skeleton visualization on right (400x400)
   - Text display and buttons at bottom

3. **Camera Activation**
   - Green camera indicator (if visible)
   - Live feed updates at ~30 FPS
   - Position hand in front of camera

4. **Gesture Recognition**
   - Make sign language gestures
   - Characters appear in real-time
   - Spell suggestions shown
   - Sentence accumulates

---

## File Locations

```
Sign-Language-Translator-to-Text-and-Speech\
├─ run_app.bat ⭐ (Double-click to run)
├─ run_app.ps1 (PowerShell version)
├─ final_pred.py (Main application)
├─ cnn8grps_rad1_model.h5 (12.9 MB model)
└─ AtoZ_3.1\ (Training data)
```

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Access denied | Try `run_app.bat` or right-click → Run as admin |
| Slow startup | Normal - TensorFlow initialization takes time |
| GUI not visible | Try alt-tab or check for window behind |
| Camera not working | Check camera permissions, try Camera app first |
| No sound | Check system volume, restart app |
| Performance lag | Close other apps, ensure good lighting |

---

## Keyboard Controls

- **Make gestures** - Position hand in camera
- **Continue** - Hold gesture ~1 second to register
- **Click suggestions** - Replace misspelled words
- **Click "Speak"** - Hear text read aloud
- **Click "Clear"** - Reset sentence
- **Close app** - Click X button on window

---

## Advanced Options

### Run with Environment Variables
```bash
set TF_CPP_MIN_LOG_LEVEL=2
python final_pred.py
```
(Reduces verbose logging)

### Run in Windowed Mode (if fullscreen issues)
Edit final_pred.py line with `geometry`:
```python
self.root.geometry("1280x720+100+100")
```

### Adjust Display Scale
```python
# In final_pred.py, adjust font sizes:
font=("Helvetica", 28, "bold")  # Change 28 to larger/smaller
```

---

## Version Info

- **Application:** Sign Language Translator v1.0
- **Python:** 3.12.3
- **Framework:** Tkinter + Keras + OpenCV
- **Status:** Production Ready ✅
- **License:** Team Elite Hackathon Project

---

**Need help?** Check the documentation files:
- README.md (Start here)
- QUICK_REFERENCE.md (Quick start)
- EXECUTION_GUIDE.md (Detailed guide)
- CODE_WALKTHROUGH.md (Technical details)
