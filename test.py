#!/usr/bin/env python
import base64

# Replace the quoted text with the code you wish to decrypt.
coded_string = 'SG9va2VkIG9uIHBob25pY3Mgd29ya2VkIGZvciBtZQo='

# Decrypt the code string.
code_dump = base64.b64decode(coded_string)

# Print the decryption output to the screen.
print(code_dump)

# Print the decryption output a file.
f = open('base64_out.txt', 'w')
f.write(code_dump)
f.close()
