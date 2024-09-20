def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('A')
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('A')
        if char.isupper():
            result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)


def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = preprocess_playfair_text(text)
    ciphertext = []
    for i in range(0, len(text), 2):
        digraph = text[i:i+2]
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])
    return ''.join(ciphertext)

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    plaintext = []
    for i in range(0, len(text), 2):
        digraph = text[i:i+2]
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])
    return ''.join(plaintext)

def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used_chars = set()
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_playfair_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text.append(text[i])
            processed_text.append('X')
            i += 1
        else:
            processed_text.append(text[i])
            if i + 1 < len(text):
                processed_text.append(text[i + 1])
            else:
                processed_text.append('X')
            i += 2
    return ''.join(processed_text)

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


import numpy as np

def hill_encrypt(text, key):
    text = preprocess_hill_text(text)
    matrix_key = create_hill_key_matrix(key)
    ciphertext = ''
    for i in range(0, len(text), 2):
        vector = np.array([ord(text[i]) - ord('A'), ord(text[i+1]) - ord('A')])
        result = np.dot(matrix_key, vector) % 26
        ciphertext += chr(result[0] + ord('A')) + chr(result[1] + ord('A'))
    return ciphertext

def hill_decrypt(text, key):
    matrix_key = create_hill_key_matrix(key)
    inv_key = np.linalg.inv(matrix_key) % 26
    inv_key = np.round(inv_key).astype(int)
    plaintext = ''
    for i in range(0, len(text), 2):
        vector = np.array([ord(text[i]) - ord('A'), ord(text[i+1]) - ord('A')])
        result = np.dot(inv_key, vector) % 26
        plaintext += chr(int(result[0]) + ord('A')) + chr(int(result[1]) + ord('A'))
    return plaintext

def preprocess_hill_text(text):
    text = text.upper().replace(' ', '')
    if len(text) % 2 != 0:
        text += 'X'
    return text

def create_hill_key_matrix(key):
    key = key.upper().replace(' ', '')[:4]  
    matrix = np.array([[ord(key[0]) - ord('A'), ord(key[1]) - ord('A')],
                       [ord(key[2]) - ord('A'), ord(key[3]) - ord('A')]])
    return matrix
