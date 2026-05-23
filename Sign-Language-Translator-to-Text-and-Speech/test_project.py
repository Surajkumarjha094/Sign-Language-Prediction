#!/usr/bin/env python
"""
Sign Language Translator - Comprehensive Test & Execution Suite
Tests all components and validates the project setup
"""

import os
import sys
import subprocess
import importlib
import platform

class SignLanguageProjectTester:
    def __init__(self):
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_file = os.path.join(self.project_dir, 'cnn8grps_rad1_model.h5')
        self.data_dir = os.path.join(self.project_dir, 'AtoZ_3.1')
        self.results = {
            'passed': [],
            'failed': [],
            'warnings': []
        }
    
    def print_header(self, text):
        """Print formatted header"""
        print(f"\n{'='*70}")
        print(f"  {text}")
        print(f"{'='*70}\n")
    
    def test_python_version(self):
        """Test Python version compatibility"""
        print("1. Testing Python Version...")
        version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        print(f"   ✓ Python {version}")
        
        if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
            print("   ✓ Version is compatible (3.8+)")
            self.results['passed'].append("Python version")
        else:
            print("   ✗ Requires Python 3.8 or higher")
            self.results['failed'].append("Python version")
    
    def test_dependencies(self):
        """Test all required dependencies"""
        print("2. Testing Dependencies...")
        
        dependencies = {
            'numpy': 'Numerical computations',
            'cv2': 'OpenCV - Image processing',
            'keras': 'Keras - Deep learning model loading',
            'tensorflow': 'TensorFlow - Backend for Keras',
            'cvzone': 'CVZone - Hand detection module',
            'pyttsx3': 'PyTTSx3 - Text-to-speech',
            'enchant': 'Enchant - Spell checking',
            'PIL': 'Pillow - Image processing for GUI',
            'tkinter': 'Tkinter - GUI framework'
        }
        
        for pkg, description in dependencies.items():
            try:
                if pkg == 'cv2':
                    import cv2
                    version = cv2.__version__
                elif pkg == 'PIL':
                    from PIL import Image
                    import PIL
                    version = PIL.__version__
                elif pkg == 'keras':
                    import keras
                    version = keras.__version__
                elif pkg == 'tensorflow':
                    import tensorflow
                    version = tensorflow.__version__
                elif pkg == 'tkinter':
                    import tkinter
                    version = "3.x"
                else:
                    mod = importlib.import_module(pkg)
                    version = getattr(mod, '__version__', 'unknown')
                
                print(f"   ✓ {pkg:15} v{version:10} - {description}")
                self.results['passed'].append(f"Dependency: {pkg}")
            except ImportError as e:
                print(f"   ✗ {pkg:15} NOT FOUND   - {description}")
                print(f"      Error: {str(e)}")
                self.results['failed'].append(f"Dependency: {pkg}")
    
    def test_model_file(self):
        """Test if model file exists"""
        print("3. Testing Model File...")
        
        if os.path.exists(self.model_file):
            size_mb = os.path.getsize(self.model_file) / (1024 * 1024)
            print(f"   ✓ Model file found: {os.path.basename(self.model_file)}")
            print(f"   ✓ Size: {size_mb:.2f} MB")
            self.results['passed'].append("Model file")
        else:
            print(f"   ✗ Model file NOT FOUND: {self.model_file}")
            self.results['failed'].append("Model file")
    
    def test_data_directory(self):
        """Test if training data exists"""
        print("4. Testing Training Data...")
        
        if os.path.exists(self.data_dir):
            # Count subdirectories (should be A-Z)
            letters = [d for d in os.listdir(self.data_dir) if os.path.isdir(os.path.join(self.data_dir, d))]
            print(f"   ✓ Data directory found: {os.path.basename(self.data_dir)}")
            print(f"   ✓ Contains {len(letters)} letter directories")
            
            # List them
            letters_sorted = sorted(letters)
            print(f"   ✓ Letters: {', '.join(letters_sorted[:5])}... and more")
            self.results['passed'].append("Training data")
        else:
            print(f"   ✗ Data directory NOT FOUND: {self.data_dir}")
            self.results['failed'].append("Training data")
    
    def test_python_files(self):
        """Test if all Python files exist"""
        print("5. Testing Python Files...")
        
        files = {
            'final_pred.py': 'GUI application (MAIN)',
            'prediction_wo_gui.py': 'CLI version without GUI',
            'data_collection_final.py': 'Data collection script',
            'data_collection_binary.py': 'Binary data collection'
        }
        
        for filename, description in files.items():
            filepath = os.path.join(self.project_dir, filename)
            if os.path.exists(filepath):
                size_kb = os.path.getsize(filepath) / 1024
                print(f"   ✓ {filename:30} ({size_kb:6.1f} KB) - {description}")
                self.results['passed'].append(f"Python file: {filename}")
            else:
                print(f"   ✗ {filename:30} NOT FOUND - {description}")
                self.results['failed'].append(f"Python file: {filename}")
    
    def test_model_loading(self):
        """Test if model can be loaded"""
        print("6. Testing Model Loading...")
        
        try:
            from keras.models import load_model
            print("   ✓ Keras import successful")
            
            if os.path.exists(self.model_file):
                print(f"   ⏳ Loading model: {os.path.basename(self.model_file)}")
                model = load_model(self.model_file)
                print(f"   ✓ Model loaded successfully")
                print(f"   ✓ Model input shape: {model.input_shape}")
                print(f"   ✓ Model output shape: {model.output_shape}")
                self.results['passed'].append("Model loading")
            else:
                print(f"   ⚠ Model file not found, skipping load test")
                self.results['warnings'].append("Model file not found for load test")
        
        except Exception as e:
            print(f"   ✗ Model loading failed: {str(e)}")
            self.results['failed'].append("Model loading")
    
    def test_camera_availability(self):
        """Test if camera is available"""
        print("7. Testing Camera Availability...")
        
        try:
            import cv2
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                print("   ✓ Camera detected and accessible")
                ret, frame = cap.read()
                if ret:
                    print(f"   ✓ Camera can capture frames (resolution: {frame.shape})")
                    self.results['passed'].append("Camera availability")
                else:
                    print("   ⚠ Camera detected but cannot capture frames")
                    self.results['warnings'].append("Camera frame capture failed")
                cap.release()
            else:
                print("   ⚠ No camera detected (may not be available in this environment)")
                self.results['warnings'].append("Camera not available")
        
        except Exception as e:
            print(f"   ⚠ Camera test inconclusive: {str(e)}")
            self.results['warnings'].append(f"Camera test error: {str(e)}")
    
    def test_gui_support(self):
        """Test if GUI can be initialized"""
        print("8. Testing GUI Support (Tkinter)...")
        
        try:
            import tkinter as tk
            root = tk.Tk()
            print("   ✓ Tkinter initialized successfully")
            
            # Check display availability
            try:
                root.update_idletasks()
                print("   ✓ GUI display is available")
                self.results['passed'].append("GUI support")
            except Exception as e:
                if "no display" in str(e).lower() or "winsysexe" in str(e).lower():
                    print("   ⚠ No display available (headless environment)")
                    self.results['warnings'].append("GUI: Headless environment detected")
                else:
                    raise
            finally:
                root.destroy()
        
        except Exception as e:
            print(f"   ⚠ GUI support limited: {str(e)}")
            self.results['warnings'].append(f"GUI support: {str(e)}")
    
    def test_spell_checker(self):
        """Test spell checker functionality"""
        print("9. Testing Spell Checker (Enchant)...")
        
        try:
            import enchant
            checker = enchant.Dict("en-US")
            print("   ✓ Enchant dictionary loaded")
            
            # Test spell checking
            test_word = "hello"
            if checker.check(test_word):
                print(f"   ✓ Spell check works: '{test_word}' is correct")
            
            # Test suggestions
            misspelled = "wrld"
            suggestions = checker.suggest(misspelled)
            print(f"   ✓ Suggestions work: '{misspelled}' → {suggestions[:3]}")
            self.results['passed'].append("Spell checker")
        
        except Exception as e:
            print(f"   ✗ Spell checker failed: {str(e)}")
            self.results['failed'].append("Spell checker")
    
    def test_tts_engine(self):
        """Test text-to-speech engine"""
        print("10. Testing Text-to-Speech (pyttsx3)...")
        
        try:
            import pyttsx3
            engine = pyttsx3.init()
            print("   ✓ TTS engine initialized")
            
            # Get properties
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            print(f"   ✓ Available voices: {len(voices)}")
            print(f"   ✓ Speech rate: {rate} WPM")
            self.results['passed'].append("Text-to-speech")
        
        except Exception as e:
            print(f"   ⚠ TTS warning: {str(e)}")
            self.results['warnings'].append(f"TTS: {str(e)}")
    
    def run_all_tests(self):
        """Run all tests"""
        self.print_header("SIGN LANGUAGE TRANSLATOR - PROJECT VALIDATION")
        
        print(f"Project Directory: {self.project_dir}")
        print(f"Python Version: {sys.version}")
        print(f"Platform: {platform.platform()}\n")
        
        self.test_python_version()
        self.test_dependencies()
        self.test_model_file()
        self.test_data_directory()
        self.test_python_files()
        
        try:
            self.test_model_loading()
        except Exception as e:
            print(f"   Note: Model loading test skipped ({str(e)})")
        
        self.test_camera_availability()
        self.test_gui_support()
        self.test_spell_checker()
        self.test_tts_engine()
        
        self.print_summary()
    
    def print_summary(self):
        """Print test summary"""
        self.print_header("TEST SUMMARY")
        
        passed_count = len(self.results['passed'])
        failed_count = len(self.results['failed'])
        warning_count = len(self.results['warnings'])
        
        print(f"✓ PASSED:  {passed_count:3d} tests")
        print(f"✗ FAILED:  {failed_count:3d} tests")
        print(f"⚠ WARNINGS: {warning_count:3d} issues\n")
        
        if self.results['failed']:
            print("FAILED TESTS:")
            for item in self.results['failed']:
                print(f"  ✗ {item}")
        
        if self.results['warnings']:
            print("\nWARNINGS:")
            for item in self.results['warnings']:
                print(f"  ⚠ {item}")
        
        if not self.results['failed']:
            print("✓ All critical tests passed!")
        else:
            print(f"\n✗ {failed_count} test(s) failed. Fix these before running the application.")
        
        print("\n" + "="*70)
        print("NEXT STEPS:")
        print("="*70)
        print("\n1. RUN GUI APPLICATION (Recommended):")
        print("   python final_pred.py")
        print("\n2. RUN CLI VERSION (Lightweight):")
        print("   python prediction_wo_gui.py")
        print("\n3. COLLECT NEW DATA:")
        print("   python data_collection_final.py")
        print("\n" + "="*70)


if __name__ == "__main__":
    tester = SignLanguageProjectTester()
    tester.run_all_tests()
