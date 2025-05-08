#2024106140 choinsu
#2023106117 yujianuo

def get_original_text():
    return 'as df'

def get_shift_amount():
    return 1

def remove_nonletters(input_text):
    return 'asdf'

def cipher(text, shift_amount):
    # 加密，每5个字母插入空格
    return 'zxcv'

def decipher(text, shift_amount):
    # 解密，把空格去掉并做逆向位移
    return 'asdf'


if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'cipher_text=> {cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'decipher_text=> {decipher_text}')