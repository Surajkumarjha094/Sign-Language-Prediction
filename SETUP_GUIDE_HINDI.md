# 🚀 दूसरे Laptop पर Project Setup करने के Steps

## 📋 COMPLETE SETUP GUIDE (Hindi + English)

---

## **Step 1: Git Install करो**

### Windows पर:
1. Download करो: https://git-scm.com/download/win
2. Install करो (सभी defaults accept करो)
3. Verify करो:
```bash
git --version
```

---

## **Step 2: Python Install करो**

### Windows पर:
1. Download करो: https://www.python.org/downloads/ (Python 3.10 या 3.12)
2. Install करते समय **"Add Python to PATH"** ✅ CHECK करो
3. Verify करो:
```bash
python --version
```

---

## **Step 3: Project Clone करो**

किसी भी folder में जाकर चलाओ:

```bash
git clone https://github.com/Surajkumarjha094/Sign-Language-Prediction.git
cd Sign-Language-Prediction
cd Sign-Language-Translator-to-Text-and-Speech
```

---

## **Step 4: Dependencies Install करो**

सभी required packages install करो:

```bash
pip install -r requirements.txt
```

**या अगर requirements.txt नहीं है तो manually:**

```bash
pip install numpy==1.26.4
pip install keras==3.9.1
pip install tensorflow==2.16.1
pip install opencv-python==4.11.0.86
pip install cvzone==1.5.6
pip install pillow==10.4.0
pip install pyttsx3==2.91
pip install pyenchant==3.2.2
```

⚠️ **Important**: NumPy version सही करो (1.26.4, NOT 2.x)

---

## **Step 5: Model Download करो**

Model file already है repository में:
- `cnn8grps_rad1_model.h5` (12.9 MB)

Check करो कि यह file है:
```bash
dir cnn8grps_rad1_model.h5
```

---

## **Step 6: Project Run करो**

```bash
python final_pred.py
```

**Expected Output:**
- ✅ TensorFlow loading logs
- ✅ GUI window खुले (1280×720)
- ✅ Live camera feed दिखे
- ✅ Hand detection काम करे

---

## **🎯 अगर कोई Error आए तो:**

### **Error 1: "No module named keras"**
```bash
pip install keras tensorflow
```

### **Error 2: "Camera not found"**
- Camera सही connect है check करो
- या अलग camera port try करो

### **Error 3: "Model not found"**
- `cnn8grps_rad1_model.h5` file same folder में होनी चाहिए
- या absolute path देना पड़ेगा

### **Error 4: "Access is denied"**
```bash
# Administrator mode में PowerShell खोलो और फिर से करो
python final_pred.py
```

### **Error 5: NumPy version conflict**
```bash
pip install --upgrade numpy==1.26.4
```

---

## **🔧 Troubleshooting Checklist**

अगर camera नहीं काम कर रहा:

```bash
# Check करो कि OpenCV camera detect कर रहा है
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

अगर True नहीं आता तो:
1. Camera driver update करो
2. Another USB port में लगाओ
3. या built-in camera use करो

---

## **📊 Step-by-Step Quick Version**

```bash
# 1. Clone करो
git clone https://github.com/Surajkumarjha094/Sign-Language-Prediction.git

# 2. Project folder में जाओ
cd Sign-Language-Prediction
cd Sign-Language-Translator-to-Text-and-Speech

# 3. Dependencies install करो
pip install numpy==1.26.4 keras tensorflow opencv-python cvzone pillow pyttsx3 pyenchant

# 4. Run करो
python final_pred.py
```

**बस! 🎉 आपका project चल जाएगा!**

---

## **🎮 Features जो काम करेंगे**

✅ Real-time gesture recognition (A-Z)
✅ Hand skeleton visualization
✅ Sentence accumulation
✅ Spell suggestions (with corrections)
✅ Text-to-speech (सुनो output)
✅ Performance metrics (FPS, Chars, Hand, Conf)
✅ Delete Word button
✅ On-screen tips

---

## **💾 Data Files Needed**

```
Required files in folder:
├─ final_pred.py ✅ (code)
├─ cnn8grps_rad1_model.h5 ✅ (model - 12.9 MB)
└─ AtoZ_3.1/ ✅ (training data - already included)
```

---

## **⚡ Performance Tips**

Laptop पर अगर slow चल रहा है:

1. **अच्छी lighting रखो** (सबसे important!)
2. **कोई background app बंद करो**
3. **Camera को face करो** (directly)
4. **Gestures slow करो** (बहुत fast नहीं)
5. **Clear background रखो**

---

## **📱 System Requirements**

```
Minimum:
- Windows 10/11 या Linux
- Python 3.10+
- 4 GB RAM
- Webcam (built-in या external)
- 500 MB free space (+ 13 MB model)

Recommended:
- Windows 11
- Python 3.12
- 8+ GB RAM
- Dedicated GPU (NVIDIA preferred)
- 1+ GB free space
```

---

## **🎓 Development के लिए**

अगर code modify करना है:

```bash
# Code editor खोलो
code .

# या Python IDE
# PyCharm, VS Code, Jupyter Notebook - कोई भी use कर सकते हो
```

---

## **🐛 Debug Mode**

अगर issue debug करना है:

```bash
# Verbose output के साथ
python -u final_pred.py

# या Python debugger use करो
python -m pdb final_pred.py
```

---

## **✅ Full Setup Example (Complete)**

```bash
# 1. Folder बनाओ
mkdir sign-language-project
cd sign-language-project

# 2. Clone करो
git clone https://github.com/Surajkumarjha094/Sign-Language-Prediction.git
cd Sign-Language-Prediction/Sign-Language-Translator-to-Text-and-Speech

# 3. Virtual environment बनाओ (optional but recommended)
python -m venv venv
venv\Scripts\activate  # Windows के लिए

# 4. Dependencies install करो
pip install --upgrade pip
pip install numpy==1.26.4 keras==3.9.1 tensorflow==2.16.1 opencv-python==4.11.0.86 cvzone==1.5.6 pillow==10.4.0 pyttsx3==2.91 pyenchant==3.2.2

# 5. Test करो
python -c "import keras, tensorflow, cv2, cvzone; print('✅ All imports successful')"

# 6. Run करो
python final_pred.py
```

---

## **📞 Common Issues & Fixes**

| Problem | Solution |
|---------|----------|
| Camera नहीं दिख रहा | Camera permission दो, driver update करो |
| Model नहीं मिल रहा | Model file same folder में रखो |
| Slow performance | Lighting improve करो, apps बंद करो |
| NumPy error | `pip install numpy==1.26.4` करो |
| Keras error | `pip install keras tensorflow` करो |
| PyTTSx3 error | `pip install pyttsx3` करो |

---

## **🎬 Final Steps**

1. ✅ Python install करो
2. ✅ Git install करो
3. ✅ Repository clone करो
4. ✅ Dependencies install करो
5. ✅ `python final_pred.py` run करो
6. ✅ Hand gestures करो और enjoy करो! 🎉

---

## **📖 Documentation Files**

GitHub repo में सभी documentation है:

- **README.md** - Project overview
- **ENHANCEMENTS_GUIDE.md** - Feature explanation
- **QUICK_REFERENCE.md** - Quick tips
- **VERIFICATION_CHECKLIST.md** - Testing guide
- **IMPROVEMENTS_INDEX.md** - All improvements list

---

## **🚀 Ready?**

```bash
git clone https://github.com/Surajkumarjha094/Sign-Language-Prediction.git
cd Sign-Language-Prediction/Sign-Language-Translator-to-Text-and-Speech
pip install numpy==1.26.4 keras tensorflow opencv-python cvzone pillow pyttsx3 pyenchant
python final_pred.py
```

**That's it! Happy coding! 💻🎉**
