#2024106140 choinsu
#2023106117 yujianuo

import argparse

def clean_text(text):
    return ''.join(filter(str.isalpha, text))

def shift_text(text, shift):
    shifted = ""
    for c in text.upper():
        shifted += chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
    return shifted

def unshift_text(text, shift):
    return shift_text(text, -shift)

def format_five(text):
    return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("shift", type=int)
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        original = f.read()

    cleaned = clean_text(original)
    ciphered = shift_text(cleaned, args.shift)
    formatted = format_five(ciphered)
    deciphered = unshift_text(ciphered, args.shift)

    print("Cipher Text:", formatted)
    print("Deciphered Text:", deciphered)

if __name__ == "__main__":
    main()
