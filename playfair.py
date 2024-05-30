#Playfair Cipher
"""
The Playfair cipher is a manual symmetric encryption technique and is a substitution cipher.
The Playfair cipher encrypts pairs of letters instead of single letters as in the simple substitution cipher.
The security of the Playfair cipher is much improved over the simple monoalphabetic cipher. 

The Rules for encryption that we will use:
1. If both letters are the same (or only one letter is left), add a filler letter like "X" after the first letter.
   Encrypt the new pair and continue. (for example, "BALLOON" becomes "BA LX LO ON")
2. If both letters fall in the same row, replace each letter with the letter to its right (wrapping back to the start from the end).
3. If both letters fall in the same column, replace each letter with the letter below it (wrapping to the top from the bottom).
4. If both letters fall in different rows and columns, replace each letter with the letter in its row in the column of the other letter of the pair.

The Rules for decryption that we will use:
1. Use the inverse (opposite) of the encryption rules.
2. Drop any extra "X" that do not make sense in the final message when finished.

Explination of each func:
- generate_playfair_matrix: Generates a 5x5 matrix based on the provided keyword.
- find_position: Finds the position of a character in the matrix.
- process_digraphs: Processes the plaintext into digraphs (pairs of letters).
- encrypt_digraph: Encrypts a digraph using the Playfair cipher rules.
- decrypt_digraph: Decrypts a digraph using the Playfair cipher rules.
- playfair_encrypt: Encrypts the entire plaintext message using the Playfair cipher.
- playfair_decrypt: Decrypts the entire ciphertext message using the Playfair cipher.
"""

def generate_playfair_matrix(keyword):
    """
    Generates a 5x5 matrix based on the provided keyword.
    - Removes duplicates from the keyword.
    - Fills the rest of the matrix with remaining letters of the alphabet, except I/J which we will put in one.
    """
    matrix = []
    keyword = keyword.upper().replace("J", "I")
    used_letters = set()

    # Add keyword letters to the matrix
    for char in keyword:
        if char not in used_letters and char.isalpha():
            matrix.append(char)
            used_letters.add(char)

    # Add remaining letters to the matrix
    for char in range(ord('A'), ord('Z') + 1):
        if chr(char) not in used_letters and chr(char) != 'J':
            matrix.append(chr(char))

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """
    Finds the position of a character in the matrix.
    Returns the row and column indices of the character.
    """
    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            if letter == char:
                return i, j
    return None

def process_digraphs(text):
    """
    Processes the plaintext into digraphs (pairs of letters).
    If a pair contains the same letter or a single letter is left, adds a filler letter here we will use 'X'.
    """
    digraphs = []
    text = text.upper().replace("J", "I")
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                digraphs.append(text[i] + 'X')
                i += 1
            else:
                digraphs.append(text[i] + text[i + 1])
                i += 2
        else:
            digraphs.append(text[i] + 'X')
            i += 1
    return digraphs

def encrypt(matrix, digraph):
    """
    Encrypts using the Playfair cipher rules.
    """
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt(matrix, digraph):
    """
    Decrypts using the Playfair cipher rules.
    """
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(plaintext, keyword):
    """
    Encrypts the entire plaintext message using the Playfair cipher.
    """
    matrix = generate_playfair_matrix(keyword)
    digraphs = process_digraphs(plaintext)
    ciphertext = ''

    for digraph in digraphs:
        ciphertext += encrypt(matrix, digraph)

    return ciphertext

def playfair_decrypt(ciphertext, keyword):
    """
    Decrypts the entire ciphertext message using the Playfair cipher.
    """
    matrix = generate_playfair_matrix(keyword)
    digraphs = process_digraphs(ciphertext)
    plaintext = ''

    for digraph in digraphs:
        plaintext += decrypt(matrix, digraph)

    return plaintext

# example from slides
keyword = "MONARCHY"
plaintext = "BALLOON"
ciphertext = playfair_encrypt(plaintext, keyword)
decrypted_text = playfair_decrypt(ciphertext, keyword)

print("\nPlayfair Cipher for Information System Security Course:")

print("\nKeyword:", keyword)
print("\nPlaintext:", plaintext)
print("\nCiphertext:", ciphertext)
print("\nDecrypted Text:", decrypted_text)

print("\nThank you Doctor Mustafa for all your support and the amazing lectures!")
print("Done by: \nSadeel Muwahed 20200232\n")