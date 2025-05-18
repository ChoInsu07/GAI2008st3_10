#2024106140 choinsu
#2023106117 yujianuo

import argparse
import os

def get_original_text():
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                return file.read()
    raise FileNotFoundError("No .txt file found in the current directory.")

def get_shift_amount():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shift', type=int, required=True)
    args = parser.parse_args()
    return args.shift

def remove_nonletters(input_text):
    return ''.join([char for char in input_text if char.isalpha()])

def cipher(text, shift_amount):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift_amount) % 26 + base
            result += chr(shifted)

    grouped = ' '.join([result[i:i+5] for i in range(0, len(result), 5)])
    return grouped

def decipher(text, shift_amount):
    clean_text = text.replace(' ', '')
    result = ''
    for char in clean_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift_amount) % 26 + base
            result += chr(shifted)
    return result

if __name__ == '__main__':
    shift_amount = get_shift_amount()
    original_text = get_original_text()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'cipher_text => {cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'decipher_text => {decipher_text}')




