#!/usr/bin/env python
"""Simple sentence formatting test - no dependencies"""

print("=" * 70)
print("SENTENCE FORMATTING TEST (No Dependencies)")
print("=" * 70)

# Test the fixed logic
str_sentence = ""
prev_char = ""
test_gestures = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

print("\n📝 Simulating gesture sequence:\n")

for ch1 in test_gestures:
    if ch1 == " " and prev_char != " ":
        str_sentence = str_sentence + " "
        print(f"  Add SPACE → '{str_sentence}'")
    elif ch1 != "next" and ch1 != "Backspace" and ch1 != " " and ch1 != prev_char:
        if isinstance(ch1, str) and len(ch1) == 1 and ch1.isalpha():
            str_sentence = str_sentence + ch1
            print(f"  Add '{ch1}'  → '{str_sentence}'")
    
    prev_char = ch1

print("\n" + "=" * 70)
print("RESULT:")
print("=" * 70)
print(f"Final Sentence: '{str_sentence}'")
print(f"Expected:      'HELLO WORLD'")
print(f"Status:        {'✅ SUCCESS' if str_sentence == 'HELLO WORLD' else '❌ FAILED'}")
print("=" * 70)
