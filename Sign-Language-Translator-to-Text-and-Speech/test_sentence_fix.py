#!/usr/bin/env python
"""
Quick test to verify sentence formatting fix
"""

print("=" * 70)
print("SENTENCE FORMATTING TEST")
print("=" * 70)

# Simulate the sentence building logic
class TestApp:
    def __init__(self):
        self.str = ""  # Now starts empty (fixed)
        self.prev_char = ""
        self.count = 0
        
    def add_character(self, ch1):
        """Simulate character addition"""
        if ch1 == " " and self.prev_char != " ":
            # Add single space between words
            self.str = self.str + " "
            print(f"✓ Added space: '{self.str}'")
        elif ch1 == "  " and self.prev_char != "  ":
            # Double space handling
            self.str = self.str + "  "
            print(f"✓ Added double space: '{self.str}'")
        elif ch1 != "next" and ch1 != "Backspace" and ch1 != " " and ch1 != "  " and ch1 != self.prev_char:
            # Add regular characters (A-Z)
            if isinstance(ch1, str) and len(ch1) == 1 and ch1.isalpha():
                self.str = self.str + ch1
                print(f"✓ Added '{ch1}': '{self.str}'")
        
        self.prev_char = ch1
        self.count += 1

# Test the sentence building
app = TestApp()

print("\n📝 Building sentence: 'HELLO WORLD'\n")

gestures = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

for gesture in gestures:
    app.add_character(gesture)

print("\n" + "=" * 70)
print("RESULT:")
print("=" * 70)
print(f"Final Sentence: '{app.str}'")
print(f"Expected:      'HELLO WORLD'")

if app.str == "HELLO WORLD":
    print("\n✅ SUCCESS! Sentence formatting is working correctly!")
else:
    print(f"\n⚠️ Issue: Got '{app.str}' instead of 'HELLO WORLD'")

print("=" * 70)
