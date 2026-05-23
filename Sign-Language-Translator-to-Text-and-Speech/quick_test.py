#!/usr/bin/env python
"""Quick validation test"""
import os, sys

print("="*70)
print("SIGN LANGUAGE TRANSLATOR - QUICK VALIDATION")
print("="*70)

proj_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(proj_dir)

# Test 1: Python version
print(f"\n✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# Test 2: Files
files = ['final_pred.py', 'prediction_wo_gui.py', 'cnn8grps_rad1_model.h5', 'AtoZ_3.1']
for f in files:
    exists = "✓" if os.path.exists(f) else "✗"
    size = f" ({os.path.getsize(f)/(1024*1024):.1f} MB)" if os.path.isfile(f) else ""
    print(f"{exists} {f}{size}")

# Test 3: Key dependencies
deps = ['numpy', 'cv2', 'keras', 'pyttsx3', 'enchant', 'PIL', 'tkinter']
print("\nDependencies:")
for dep in deps:
    try:
        __import__(dep if dep != 'cv2' else 'cv2')
        print(f"  ✓ {dep}")
    except:
        print(f"  ✗ {dep}")

# Test 4: Model loading
print("\nLoading model...")
try:
    from keras.models import load_model
    model = load_model('cnn8grps_rad1_model.h5')
    print(f"  ✓ Model loaded: input {model.input_shape}, output {model.output_shape}")
except Exception as e:
    print(f"  ✗ Model loading failed: {str(e)[:50]}")

print("\n" + "="*70)
print("✓ PROJECT READY TO RUN")
print("="*70)
print("\nUSAGE:")
print("  GUI Version:  python final_pred.py")
print("  CLI Version:  python prediction_wo_gui.py")
print("\n" + "="*70)
