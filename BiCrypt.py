# Copyright 2017 Moisés González
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Encrypt files with two different keys"""

import argparse
from getpass import getpass
import os
from hashlib import sha256
import pyaes


def img_encrypt(f1, f_password=None, s_password=None):
    """Encrypt the file"""
    with open('%s.crypt' % f1, 'wb') as file1:
        with open(f1, 'rb') as file2:
            try:
                assert os.stat(f1).st_size > 0
                file2_content = file2.read()
            except AssertionError:
                print('EmptyFile: The file is empty.')
            else:
                key = sha256()
                key.update(bytes(f_password, 'utf-8'))
                key = key.digest()
                even_bytes = file2_content[::2]
                cipher = pyaes.AESModeOfOperationCTR(key)
                cipher_even_bytes = cipher.encrypt(even_bytes)
                key = sha256()
                key.update(bytes(s_password, 'utf-8'))
                key = key.digest()
                odd_bytes = file2_content[1::2]
                cipher = pyaes.AESModeOfOperationCTR(key)
                cipher_odd_bytes = cipher.encrypt(odd_bytes)
                joined_encrypted_bytes = []
                for a, b in zip(cipher_even_bytes, cipher_odd_bytes):
                    joined_encrypted_bytes.append(a)
                    joined_encrypted_bytes.append(b)
                file1.write(bytes(joined_encrypted_bytes))


def img_decrypt(f1, f_password=None, s_password=None):
    """Decrypt the file"""
    with open(f1, 'rb') as file1:
        file1_content = file1.read()
        even_encrypted_bytes = file1_content[::2]
        key = sha256()
        key.update(bytes(f_password, 'utf-8'))
        key = key.digest()
        deciphers = pyaes.AESModeOfOperationCTR(key)
        deciphers_even_bytes = deciphers.decrypt(even_encrypted_bytes)
        odd_encrypted_bytes = file1_content[1::2]
        key = sha256()
        key.update(bytes(s_password, 'utf-8'))
        key = key.digest()
        deciphers = pyaes.AESModeOfOperationCTR(key)
        deciphers_odd_bytes = deciphers.decrypt(odd_encrypted_bytes)
        joined_decrypt_bytes = []
        for a, b in zip(deciphers_even_bytes, deciphers_odd_bytes):
            joined_decrypt_bytes.append(a)
            joined_decrypt_bytes.append(b)
        with open('%s' % f1[:-6:], 'wb') as file2:
            file2.write(bytes(joined_decrypt_bytes))


def get_passwords():
    while True:
        f_password = getpass(prompt='1st Password: ')

        if args.safe:
            f_password_c = getpass(prompt='Confirm 1st Password: ')

            if f_password != f_password_c:
                print('Passwords don\'t match')
                continue

        s_password = getpass(prompt='2nd Password: ')

        if args.safe:
            s_password_c = getpass(prompt='Confirm 2nd Password: ')

            if s_password != s_password_c:
                print('Passwords don\'t match')
                continue

        break

    return [f_password, s_password]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Encrypt and decrypt files
                                     with odd and even bytes
                                     """)
    parser.add_argument('file', metavar='File', help='File to encrypt',
                        type=str)
    parser.add_argument('-f', '--first_password', metavar='FirstPassphrase',
                        help='first secret password,', type=str)
    parser.add_argument('-s', '--second_password', metavar='SecondPassphrase',
                        help='second secret password,', type=str)
    parser.add_argument('-d', '--decrypt', dest='decrypt',
                        help='Decrypt file', action='store_true')
    parser.add_argument('-ns', '--nosafety', dest='safe',
                        help='Disable Password Confirmation (UNSAFE)',
                        action='store_false')
    args = parser.parse_args()

if args.first_password is None and args.second_password is None:
    args.first_password, args.second_password = get_passwords()

if args.decrypt:
    img_decrypt(args.file, args.first_password, args.second_password)
else:
    img_encrypt(args.file, args.first_password, args.second_password)
