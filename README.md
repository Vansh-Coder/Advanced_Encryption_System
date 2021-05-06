# Advanced_Encryption_System
Advanced Encryption System (AES) with a graphical user interface.

## How to use ?

(Referances: The text to be encrypted - 'plaintext' , The text to be decrypted - 'ciphertext')

1. Enter the plaintext (or ciphertext) inside the respective entry column. Note that the ciphertext should have a length which is a multiple of (or equal to) 32. This is because      in AES, each block size of a ciphertext is always 264-bits long (32 characters), consisting of ONLY printable standard ascii characters (not extended ascii characters). More      specifically, ciphertext should be in HEX format (consisting of only 0-9 digits and A-F letters). However, the plaintext can have any variable length, but should consist of        ONLY printable standard ascii characters (generally, any printable character found on a keyboard).
2. Enter the initialization vector (or IV) in the respective entry column. Note that it should be 16 characters long (128-bits long) and consist of ONLY printable standard ascii      characters. It is used to perform cipher block chaining (CBC) on the plaintext to further make it cryptanalysis proof. It may or may not be kept secret, depending upon your        need.
3. Now, enter the key (which should be kept secret) in the respective entry column. Note that jsut like initialization vector, it should also consist of ONLY printable standard      ascii characters, and should be 16 characters long (128-bits long).
4. Finally, click the 'Encrypt' button (or 'Decrypt' button, if you are decrypting a ciphertext). The decrypted (or encrypted) text is available in the entry column below, click      'Copy' button to directly copy it to your clipboard.

## Note:
This code does not store any of your entered text, IV, or key. It is purely safe to use. You may verify the same by checking out the code file. Also, this code is licensed under the open source MIT License, feel free to use it !

## An additional note:
I made this encryption code WITHOUT using any cryptographic or encryption modules, from beginning to end. That's why I think it is a unique program, and I hope to inspire others to first try to code anything by themseleves without the use of additional modules, to build & enhance their problem solving skills.
