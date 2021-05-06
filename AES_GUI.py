"""
Code written by : @Vansh-Coder on Github
Note : This code is licensed under the MIT License. Happy Coding ! :)
"""

import pyperclip as pc
import numpy as np
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title('AES Encryption & Decryption')
top.geometry("604x506")

def copy_enc():
    current_enc = text_cipher_enc.get("1.0", "end-1c")
    if len(current_enc) > 0:
        pc.copy(current_enc)

def copy_dec():
    current_dec = text_plain_dec.get("1.0", "end-1c")
    if len(current_dec) > 0:
        pc.copy(current_dec)

def encrypt():
    f = True
    if len(text_plain_enc.get("1.0", "end-1c")) == 0:
        f = False
        messagebox.showinfo("Empty text error !", "The text to be encrypted can't be empty, please try again !")
    elif len(entry_IV_enc.get()) == 0:
        f = False
        messagebox.showinfo("Empty IV error !", "The initialization vector can't be empty, please try again !")
    elif len(entry_IV_enc.get()) != 16:
        f = False
        messagebox.showinfo("IV length error !", "The initialization vector should be 16 characters long only, please try again !")
    if f is True:
        for i in entry_IV_enc.get():
            if ord(i) < 32 or ord(i) > 126:
                f = False
                messagebox.showinfo("IV type error !", "The initialization vector should consist of standard ascii printable characters only. Please try again !")
                break
    if f is True and len(entry_key_enc.get()) == 0:
        f = False
        messagebox.showinfo("Empty key error !", "The key cannot be empty, please try again !")
    elif f is True and len(entry_key_enc.get()) != 16:
        f = False
        messagebox.showinfo("Key length error !", "The key should be 16 characters long only, please try again !")
    if f is True:
        for i in entry_key_enc.get():
            if ord(i) < 32 or ord(i) > 126:
                f = False
                messagebox.showinfo("Key type error !", "The key should consist of standard ascii printable characters only. Please try again !")
    if f is True:

        s_box = ((0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76),
                 (0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0),
                 (0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15),
                 (0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75),
                 (0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84),
                 (0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf),
                 (0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8),
                 (0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2),
                 (0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73),
                 (0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb),
                 (0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79),
                 (0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08),
                 (0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a),
                 (0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e),
                 (0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf),
                 (0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16))
        r_con = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)
        fixedMatrix = ((2, 3, 1, 1),
                       (1, 2, 3, 1),
                       (1, 1, 2, 3),
                       (3, 1, 1, 2))

        plaintext = np.array([hex(ord(i)) for i in list(text_plain_enc.get("1.0", "end-1c"))])
        if len(plaintext) % 16 != 0:
            p = len(plaintext) % 16
            for i in range(16 - p):
                plaintext = np.append(plaintext, hex(16 - p))
        totalBlocks = len(plaintext) // 16
        if totalBlocks > 1:
            plaintext = plaintext.reshape(totalBlocks, 4, 4)
        else:
            plaintext = plaintext.reshape(4, 4)

        initVector = np.array([hex(ord(i)) for i in list(entry_IV_enc.get())]).reshape(4, 4)
        if totalBlocks > 1:
            for i in range(4):
                for j in range(4):
                    plaintext[0][i][j] = hex(int(plaintext[0][i][j], 16) ^ int(initVector[i][j], 16))
        else:
            for i in range(4):
                for j in range(4):
                    plaintext[i][j] = hex(int(plaintext[i][j], 16) ^ int(initVector[i][j], 16))

        key = np.array([hex(ord(i)) for i in list(entry_key_enc.get())]).reshape(4, 4)
        keysList = [key]
        for i in range(10):
            temp_key = keysList[i].copy()
            temp_key[3] = [temp_key[3][k] for k in range(1, 4)] + [temp_key[3][0]]
            for j in range(4):
                if len(temp_key[3][j]) == 3:
                    temp_key[3][j] = hex(s_box[0][int(temp_key[3][j][2], 16)])
                else:
                    temp_key[3][j] = hex(s_box[int(temp_key[3][j][2], 16)][int(temp_key[3][j][3], 16)])
                if j == 0:
                    temp_key[3][j] = hex(int(temp_key[3][j], 16) ^ r_con[i])
            final_key = [[], [], [], []]
            for j in range(4):
                final_key[0].append(hex(int(keysList[i][0][j], 16) ^ int(temp_key[3][j], 16)))
            for j in range(4):
                final_key[1].append(hex(int(keysList[i][1][j], 16) ^ int(final_key[0][j], 16)))
            for j in range(4):
                final_key[2].append(hex(int(keysList[i][2][j], 16) ^ int(final_key[1][j], 16)))
            for j in range(4):
                final_key[3].append(hex(int(keysList[i][3][j], 16) ^ int(final_key[2][j], 16)))
            final_key = np.array(final_key).reshape(4, 4)
            keysList.append(final_key)
        keysList = np.array(keysList)

        ciphertext = ''
        if totalBlocks > 1:
            for i in range(totalBlocks):
                if i != 0:
                    for j in range(4):
                        for k in range(4):
                            plaintext[i][j][k] = hex(int(plaintext[i][j][k], 16) ^ int(plaintext[i - 1][j][k], 16))
                for j in range(4):
                    for k in range(4):
                        plaintext[i][j][k] = hex(int(plaintext[i][j][k], 16) ^ int(keysList[0][j][k], 16))
                for j in range(1, 11):
                    for k in range(4):
                        for x in range(4):
                            if len(plaintext[i][k][x]) == 3:
                                plaintext[i][k][x] = hex(s_box[0][int(plaintext[i][k][x][2], 16)])
                            else:
                                plaintext[i][k][x] = hex(
                                    s_box[int(plaintext[i][k][x][2], 16)][int(plaintext[i][k][x][3], 16)])
                    temp_block = plaintext[i].copy()
                    for k in range(4):
                        for x in range(4):
                            plaintext[i][x][k] = temp_block[(x + k) % 4][k]
                    if j != 10:
                        tempText = plaintext[i].copy()
                        dp_list = []
                        for k in range(4):
                            for x in range(4):
                                for y in range(4):
                                    if fixedMatrix[x][y] != 3:
                                        dp = np.dot(fixedMatrix[x][y], int(tempText[k][y], 16))
                                    else:
                                        dp = np.dot(2, int(tempText[k][y], 16)) ^ int(tempText[k][y], 16)
                                    while dp > 255:
                                        dp = dp ^ 0x11b
                                    dp_list.append(dp)
                                dp = hex(dp_list[0] ^ dp_list[1] ^ dp_list[2] ^ dp_list[3])
                                plaintext[i][k][x] = dp
                                dp_list = []
                    for k in range(4):
                        for x in range(4):
                            plaintext[i][k][x] = hex(int(plaintext[i][k][x], 16) ^ int(keysList[j][k][x], 16))
                for j in plaintext[i].reshape(16):
                    j = j.replace('0x', '').upper()
                    if len(j) == 1:
                        j = '0' + j
                    ciphertext += j
            text_cipher_enc.delete("1.0", "end")
            text_cipher_enc.insert("1.0", ciphertext)
        else:
            for i in range(4):
                for j in range(4):
                    plaintext[i][j] = hex(int(plaintext[i][j], 16) ^ int(keysList[0][i][j], 16))
            for i in range(1, 11):
                for j in range(4):
                    for k in range(4):
                        if len(plaintext[j][k]) == 3:
                            plaintext[j][k] = hex(s_box[0][int(plaintext[j][k][2], 16)])
                        else:
                            plaintext[j][k] = hex(s_box[int(plaintext[j][k][2], 16)][int(plaintext[j][k][3], 16)])
                temp_block = plaintext.copy()
                for j in range(4):
                    for k in range(4):
                        plaintext[k][j] = temp_block[(k + j) % 4][j]
                if i != 10:
                    tempText = plaintext.copy()
                    dp_list = []
                    for j in range(4):
                        for k in range(4):
                            for x in range(4):
                                if fixedMatrix[k][x] != 3:
                                    dp = np.dot(fixedMatrix[k][x], int(tempText[j][x], 16))
                                else:
                                    dp = np.dot(2, int(tempText[j][x], 16)) ^ int(tempText[j][x], 16)
                                while dp > 255:
                                    dp = dp ^ 0x11b
                                dp_list.append(dp)
                            dp = hex(dp_list[0] ^ dp_list[1] ^ dp_list[2] ^ dp_list[3])
                            plaintext[j][k] = dp
                            dp_list = []
                for j in range(4):
                    for k in range(4):
                        plaintext[j][k] = hex(int(plaintext[j][k], 16) ^ int(keysList[i][j][k], 16))
            for i in plaintext.reshape(16):
                i = i.replace('0x', '').upper()
                if len(i) == 1:
                    i = '0' + i
                ciphertext += i
            text_cipher_enc.delete("1.0", "end")
            text_cipher_enc.insert("1.0", ciphertext)

def decrypt():
    f = True
    if len(text_cipher_dec.get("1.0", "end-1c")) == 0:
        f = False
        messagebox.showinfo("Empty text error !", "The text to be decrypted can't be empty, please try again !")
    elif len(text_cipher_dec.get("1.0", "end-1c")) % 32 != 0:
        f = False
        messagebox.showinfo("Invalid text error !", "The text to be decrypted is invalid, its length must be a multiple of 32 (or equal to 32). Please try again !")
    if f is True:
        for i in text_cipher_dec.get("1.0", "end-1c").rstrip():
            if ord(i) < 32 or ord(i) > 126:
                f = False
                messagebox.showinfo("Invalid text error !", "The text to be decrypted is invalid, it should consist of standard ascii printable characters only. Please try again !")
    elif f is True and len(entry_IV_dec.get()) == 0:
        f = False
        messagebox.showinfo("Empty IV error !", "The initialization vector can't be empty, please try again !")
    elif f is True and len(entry_IV_dec.get()) != 16:
        f = False
        messagebox.showinfo("IV length error !", "The initialization vector should be 16 characters long only, please try again !")
    if f is True:
        for i in entry_IV_dec.get():
            if ord(i) < 32 or ord(i) > 126:
                f = False
                messagebox.showinfo("IV type error !", "The initialization vector should consist of standard ascii printable characters only. Please try again !")
                break
    if f is True and len(entry_key_dec.get()) == 0:
        f = False
        messagebox.showinfo("Empty key error !", "The key cannot be empty, please try again !")
    elif f is True and len(entry_key_dec.get()) != 16:
        f = False
        messagebox.showinfo("Key length error !", "The key should be 16 characters long only, please try again !")
    if f is True:
        for i in entry_key_dec.get():
            if ord(i) < 32 or ord(i) > 126:
                f = False
                messagebox.showinfo("Key type error !", "The key should consist of standard ascii printable characters only. Please try again !")
    if f is True:

        s_box = ((0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76),
                 (0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0),
                 (0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15),
                 (0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75),
                 (0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84),
                 (0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf),
                 (0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8),
                 (0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2),
                 (0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73),
                 (0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb),
                 (0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79),
                 (0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08),
                 (0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a),
                 (0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e),
                 (0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf),
                 (0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16))
        inv_sBox = ((0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb),
                    (0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb),
                    (0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e),
                    (0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25),
                    (0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92),
                    (0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84),
                    (0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06),
                    (0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b),
                    (0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73),
                    (0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e),
                    (0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b),
                    (0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4),
                    (0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f),
                    (0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef),
                    (0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61),
                    (0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d))
        r_con = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)
        fixedMatrix = (('0x0E', '0x0B', '0x0D', '0x09'),
                       ('0x09', '0x0E', '0x0B', '0x0D'),
                       ('0x0D', '0x09', '0x0E', '0x0B'),
                       ('0x0B', '0x0D', '0x09', '0x0E'))
        E_table = ((0x01, 0x03, 0x05, 0x0F, 0x11, 0x33, 0x55, 0xFF, 0x1A, 0x2E, 0x72, 0x96, 0xA1, 0xF8, 0x13, 0x35),
                   (0x5F, 0xE1, 0x38, 0x48, 0xD8, 0x73, 0x95, 0xA4, 0xF7, 0x02, 0x06, 0x0A, 0x1E, 0x22, 0x66, 0xAA),
                   (0xE5, 0x34, 0x5C, 0xE4, 0x37, 0x59, 0xEB, 0x26, 0x6A, 0xBE, 0xD9, 0x70, 0x90, 0xAB, 0xE6, 0x31),
                   (0x53, 0xF5, 0x04, 0x0C, 0x14, 0x3C, 0x44, 0xCC, 0x4F, 0xD1, 0x68, 0xB8, 0xD3, 0x6E, 0xB2, 0xCD),
                   (0x4C, 0xD4, 0x67, 0xA9, 0xE0, 0x3B, 0x4D, 0xD7, 0x62, 0xA6, 0xF1, 0x08, 0x18, 0x28, 0x78, 0x88),
                   (0x83, 0x9E, 0xB9, 0xD0, 0x6B, 0xBD, 0xDC, 0x7F, 0x81, 0x98, 0xB3, 0xCE, 0x49, 0xDB, 0x76, 0x9A),
                   (0xB5, 0xC4, 0x57, 0xF9, 0x10, 0x30, 0x50, 0xF0, 0x0B, 0x1D, 0x27, 0x69, 0xBB, 0xD6, 0x61, 0xA3),
                   (0xFE, 0x19, 0x2B, 0x7D, 0x87, 0x92, 0xAD, 0xEC, 0x2F, 0x71, 0x93, 0xAE, 0xE9, 0x20, 0x60, 0xA0),
                   (0xFB, 0x16, 0x3A, 0x4E, 0xD2, 0x6D, 0xB7, 0xC2, 0x5D, 0xE7, 0x32, 0x56, 0xFA, 0x15, 0x3F, 0x41),
                   (0xC3, 0x5E, 0xE2, 0x3D, 0x47, 0xC9, 0x40, 0xC0, 0x5B, 0xED, 0x2C, 0x74, 0x9C, 0xBF, 0xDA, 0x75),
                   (0x9F, 0xBA, 0xD5, 0x64, 0xAC, 0xEF, 0x2A, 0x7E, 0x82, 0x9D, 0xBC, 0xDF, 0x7A, 0x8E, 0x89, 0x80),
                   (0x9B, 0xB6, 0xC1, 0x58, 0xE8, 0x23, 0x65, 0xAF, 0xEA, 0x25, 0x6F, 0xB1, 0xC8, 0x43, 0xC5, 0x54),
                   (0xFC, 0x1F, 0x21, 0x63, 0xA5, 0xF4, 0x07, 0x09, 0x1B, 0x2D, 0x77, 0x99, 0xB0, 0xCB, 0x46, 0xCA),
                   (0x45, 0xCF, 0x4A, 0xDE, 0x79, 0x8B, 0x86, 0x91, 0xA8, 0xE3, 0x3E, 0x42, 0xC6, 0x51, 0xF3, 0x0E),
                   (0x12, 0x36, 0x5A, 0xEE, 0x29, 0x7B, 0x8D, 0x8C, 0x8F, 0x8A, 0x85, 0x94, 0xA7, 0xF2, 0x0D, 0x17),
                   (0x39, 0x4B, 0xDD, 0x7C, 0x84, 0x97, 0xA2, 0xFD, 0x1C, 0x24, 0x6C, 0xB4, 0xC7, 0x52, 0xF6, 0x01))
        L_table = ((0x00, 0x00, 0x19, 0x01, 0x32, 0x02, 0x1A, 0xC6, 0x4B, 0xC7, 0x1B, 0x68, 0x33, 0xEE, 0xDF, 0x03),
                   (0x64, 0x04, 0xE0, 0x0E, 0x34, 0x8D, 0x81, 0xEF, 0x4C, 0x71, 0x08, 0xC8, 0xF8, 0x69, 0x1C, 0xC1),
                   (0x7D, 0xC2, 0x1D, 0xB5, 0xF9, 0xB9, 0x27, 0x6A, 0x4D, 0xE4, 0xA6, 0x72, 0x9A, 0xC9, 0x09, 0x78),
                   (0x65, 0x2F, 0x8A, 0x05, 0x21, 0x0F, 0xE1, 0x24, 0x12, 0xF0, 0x82, 0x45, 0x35, 0x93, 0xDA, 0x8E),
                   (0x96, 0x8F, 0xDB, 0xBD, 0x36, 0xD0, 0xCE, 0x94, 0x13, 0x5C, 0xD2, 0xF1, 0x40, 0x46, 0x83, 0x38),
                   (0x66, 0xDD, 0xFD, 0x30, 0xBF, 0x06, 0x8B, 0x62, 0xB3, 0x25, 0xE2, 0x98, 0x22, 0x88, 0x91, 0x10),
                   (0x7E, 0x6E, 0x48, 0xC3, 0xA3, 0xB6, 0x1E, 0x42, 0x3A, 0x6B, 0x28, 0x54, 0xFA, 0x85, 0x3D, 0xBA),
                   (0x2B, 0x79, 0x0A, 0x15, 0x9B, 0x9F, 0x5E, 0xCA, 0x4E, 0xD4, 0xAC, 0xE5, 0xF3, 0x73, 0xA7, 0x57),
                   (0xAF, 0x58, 0xA8, 0x50, 0xF4, 0xEA, 0xD6, 0x74, 0x4F, 0xAE, 0xE9, 0xD5, 0xE7, 0xE6, 0xAD, 0xE8),
                   (0x2C, 0xD7, 0x75, 0x7A, 0xEB, 0x16, 0x0B, 0xF5, 0x59, 0xCB, 0x5F, 0xB0, 0x9C, 0xA9, 0x51, 0xA0),
                   (0x7F, 0x0C, 0xF6, 0x6F, 0x17, 0xC4, 0x49, 0xEC, 0xD8, 0x43, 0x1F, 0x2D, 0xA4, 0x76, 0x7B, 0xB7),
                   (0xCC, 0xBB, 0x3E, 0x5A, 0xFB, 0x60, 0xB1, 0x86, 0x3B, 0x52, 0xA1, 0x6C, 0xAA, 0x55, 0x29, 0x9D),
                   (0x97, 0xB2, 0x87, 0x90, 0x61, 0xBE, 0xDC, 0xFC, 0xBC, 0x95, 0xCF, 0xCD, 0x37, 0x3F, 0x5B, 0xD1),
                   (0x53, 0x39, 0x84, 0x3C, 0x41, 0xA2, 0x6D, 0x47, 0x14, 0x2A, 0x9E, 0x5D, 0x56, 0xF2, 0xD3, 0xAB),
                   (0x44, 0x11, 0x92, 0xD9, 0x23, 0x20, 0x2E, 0x89, 0xB4, 0x7C, 0xB8, 0x26, 0x77, 0x99, 0xE3, 0xA5),
                   (0x67, 0x4A, 0xED, 0xDE, 0xC5, 0x31, 0xFE, 0x18, 0x0D, 0x63, 0x8C, 0x80, 0xC0, 0xF7, 0x70, 0x07))

        def gf_multiplication(fixed_elem, var_elem):
            if int(var_elem, 16) == 0:
                return 0
            elif int(var_elem, 16) == 1:
                return int(fixed_elem, 16)
            else:
                if len(var_elem) == 3:
                    V = L_table[0][int(var_elem[2], 16)]
                    F = L_table[int(fixed_elem[2], 16)][int(fixed_elem[3], 16)]
                    q = F + V
                    if q > 255:
                        q -= 255
                    z = hex(q)
                    if len(z) == 3:
                        e = E_table[0][int(z[2], 16)]
                        return e
                    else:
                        e = E_table[int(z[2], 16)][int(z[3], 16)]
                        return e
                else:
                    F = L_table[int(fixed_elem[2], 16)][int(fixed_elem[3], 16)]
                    V = L_table[int(var_elem[2], 16)][int(var_elem[3], 16)]
                    q = F + V
                    if q > 255:
                        q -= 255
                    z = hex(q)
                    if len(z) == 3:
                        e = E_table[0][int(z[2], 16)]
                        return e
                    else:
                        e = E_table[int(z[2], 16)][int(z[3], 16)]
                        return e

        ciphertext = text_cipher_dec.get("1.0", "end-1c").rstrip()
        if len(ciphertext) > 32:
            totalBlocks = len(ciphertext) // 32
            ciphertext = np.array([hex(int(ciphertext[i] + ciphertext[i + 1], 16)) for i in range(0, len(ciphertext) - 1, 2)]).reshape(totalBlocks, 4, 4)
        else:
            totalBlocks = 1
            ciphertext = np.array([hex(int(ciphertext[i] + ciphertext[i + 1], 16)) for i in range(0, len(ciphertext) - 1, 2)]).reshape(4, 4)

        initVector = np.array([hex(ord(i)) for i in list(entry_IV_dec.get())]).reshape(4, 4)

        key = np.array([hex(ord(i)) for i in list(entry_key_enc.get())]).reshape(4, 4)
        keysList = [key]
        for i in range(10):
            temp_key = keysList[i].copy()
            temp_key[3] = [temp_key[3][k] for k in range(1, 4)] + [temp_key[3][0]]
            for j in range(4):
                if len(temp_key[3][j]) == 3:
                    temp_key[3][j] = hex(s_box[0][int(temp_key[3][j][2], 16)])
                else:
                    temp_key[3][j] = hex(s_box[int(temp_key[3][j][2], 16)][int(temp_key[3][j][3], 16)])
                if j == 0:
                    temp_key[3][j] = hex(int(temp_key[3][j], 16) ^ r_con[i])
            final_key = [[], [], [], []]
            for j in range(4):
                final_key[0].append(hex(int(keysList[i][0][j], 16) ^ int(temp_key[3][j], 16)))
            for j in range(4):
                final_key[1].append(hex(int(keysList[i][1][j], 16) ^ int(final_key[0][j], 16)))
            for j in range(4):
                final_key[2].append(hex(int(keysList[i][2][j], 16) ^ int(final_key[1][j], 16)))
            for j in range(4):
                final_key[3].append(hex(int(keysList[i][3][j], 16) ^ int(final_key[2][j], 16)))
            final_key = np.array(final_key).reshape(4, 4)
            keysList.append(final_key)
        keysList = np.array(keysList)

        plaintext = ''
        if totalBlocks > 1:
            cipher_list = []
            for i in range(totalBlocks):
                cipher_list.append(ciphertext[i].copy())
                for j in range(4):
                    for k in range(4):
                        ciphertext[i][j][k] = hex(int(ciphertext[i][j][k], 16) ^ int(keysList[10][j][k], 16))
                for j in range(10, 0, -1):
                    temp_block = ciphertext[i].copy()
                    for k in range(4):
                        for x in range(4):
                            ciphertext[i][x][k] = temp_block[x - k][k]
                    for k in range(4):
                        for x in range(4):
                            if len(ciphertext[i][k][x]) == 3:
                                ciphertext[i][k][x] = hex(inv_sBox[0][int(ciphertext[i][k][x][2], 16)])
                            else:
                                ciphertext[i][k][x] = hex(
                                    inv_sBox[int(ciphertext[i][k][x][2], 16)][int(ciphertext[i][k][x][3],
                                                                                  16)])
                    for k in range(4):
                        for x in range(4):
                            ciphertext[i][k][x] = hex(int(ciphertext[i][k][x], 16) ^ int(keysList[j - 1][k][x], 16))
                    if j != 1:
                        tempText = ciphertext[i].copy()
                        dp_list = []
                        for k in range(4):
                            for x in range(4):
                                for y in range(4):
                                    dp = gf_multiplication(fixedMatrix[x][y], tempText[k][y])
                                    dp_list.append(dp)
                                dp = hex(dp_list[0] ^ dp_list[1] ^ dp_list[2] ^ dp_list[3])
                                ciphertext[i][k][x] = dp
                                dp_list = []
                if i == 0:
                    for j in range(4):
                        for k in range(4):
                            ciphertext[i][j][k] = hex(int(ciphertext[i][j][k], 16) ^ int(initVector[j][k], 16))
                else:
                    for j in range(4):
                        for k in range(4):
                            ciphertext[i][j][k] = hex(int(ciphertext[i][j][k], 16) ^ int(cipher_list[i - 1][j][k], 16))
                for j in ciphertext[i].reshape(16):
                    if int(j, 16) in range(32, 127):
                        j = chr(int(j, 16))
                        plaintext += j
            text_plain_dec.delete("1.0", "end")
            text_plain_dec.insert("1.0", plaintext)
        else:
            for i in range(4):
                for j in range(4):
                    ciphertext[i][j] = hex(int(ciphertext[i][j], 16) ^ int(keysList[10][i][j], 16))
            for i in range(10, 0, -1):
                temp_block = ciphertext.copy()
                for j in range(4):
                    for k in range(4):
                        ciphertext[k][j] = temp_block[k - j][j]
                for j in range(4):
                    for k in range(4):
                        if len(ciphertext[j][k]) == 3:
                            ciphertext[j][k] = hex(inv_sBox[0][int(ciphertext[j][k][2], 16)])
                        else:
                            ciphertext[j][k] = hex(inv_sBox[int(ciphertext[j][k][2], 16)][int(ciphertext[j][k][3], 16)])
                for j in range(4):
                    for k in range(4):
                        ciphertext[j][k] = hex(int(ciphertext[j][k], 16) ^ int(keysList[i - 1][j][k], 16))
                if i != 1:
                    tempText = ciphertext.copy()
                    dp_list = []
                    for j in range(4):
                        for k in range(4):
                            for x in range(4):
                                dp = gf_multiplication(fixedMatrix[k][x], tempText[j][x])
                                dp_list.append(dp)
                            dp = hex(dp_list[0] ^ dp_list[1] ^ dp_list[2] ^ dp_list[3])
                            ciphertext[j][k] = dp
                            dp_list = []
            for i in range(4):
                for j in range(4):
                    ciphertext[i][j] = hex(int(ciphertext[i][j], 16) ^ int(initVector[i][j], 16))
            for i in ciphertext.reshape(16):
                if int(i, 16) in range(32, 127):
                    i = chr(int(i, 16))
                    plaintext += i
            text_plain_dec.delete("1.0", "end")
            text_plain_dec.insert("1.0", plaintext)

label_enc = Label(top, text='Enter text to be encrypted :', font=("Times New Roman", 13))
label_dec = Label(top, text='Enter text to be decrypted :', font=("Times New Roman", 13))

text_plain_enc = Text(top, height=8, width=35, bd=2, font=("Arial", 11))
text_cipher_dec = Text(top, height=8, width=35, bd=2, font=("Arial", 11))

label_IV_enc = Label(top, text='Enter initialization vector (16 characters only) :', font=("Arial", 10))
label_IV_dec = Label(top, text='Enter initialization vector (16 characters only) :', font=("Arial", 10))

entry_IV_enc = Entry(top, width=31, borderwidth=2, font=("Arial", 11))
entry_IV_dec = Entry(top, width=31, borderwidth=2, font=("Arial", 11))

label_key_enc = Label(top, text='Enter the key (16 characters only) :', font=("Arial", 10))
label_key_dec = Label(top, text='Enter the key (16 characters only) :', font=("Arial", 10))

entry_key_enc = Entry(top, width=31, borderwidth=2, font=("Arial", 11))
entry_key_dec = Entry(top, width=31, borderwidth=2, font=("Arial", 11))

button_enc = Button(top, text='Encrypt', width=7, fg='#009933', activeforeground='#00802b', activebackground='#cccccc', font=("Times New Roman", 12), command=encrypt)
button_copy_enc = Button(top, text='Copy', width=7, activebackground='#cccccc', font=("Times New Roman", 12), command=copy_enc)

button_dec = Button(top, text='Decrypt', width=7, fg='#ff3333', activeforeground='#ff1a1a', activebackground='#cccccc', font=("Times New Roman", 12), command=decrypt)
button_copy_dec = Button(top, text='Copy', width=7, activebackground='#cccccc', font=("Times New Roman", 12), command=copy_dec)

text_cipher_enc = Text(top, height=8, width=35, bd=2, font=("Arial", 11))
text_plain_dec = Text(top, height=8, width=35, bd=2, font=("Arial", 11))

label_enc.place(x=60, y=6)
label_dec.place(x=370, y=6)

text_plain_enc.place(x=3, y=35)
text_cipher_dec.place(x=315, y=35)

label_IV_enc.place(x=10, y=190)
label_IV_dec.place(x=320, y=190)

entry_IV_enc.place(x=16, y=217)
entry_IV_dec.place(x=327, y=217)

label_key_enc.place(x=10, y=250)
label_key_dec.place(x=320, y=250)

entry_key_enc.place(x=16, y=277)
entry_key_dec.place(x=327, y=277)

button_enc.place(x=50, y=314)
button_copy_enc.place(x=160, y=314)

button_dec.place(x=361, y=314)
button_copy_dec.place(x=471, y=314)

text_cipher_enc.place(x=3, y=362)
text_plain_dec.place(x=315, y=362)

top.resizable(False, False)
top.mainloop()
