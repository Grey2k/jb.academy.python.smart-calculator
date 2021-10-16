import argparse


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


parser = argparse.ArgumentParser(description="Decrypt the dataset")
parser.add_argument('--file', type=str, required=True, help='File with dataset')

args = parser.parse_args()

filename = args.file
with open(filename) as opened_file:
    encoded_text = opened_file.read()  # read the file into a string

decode_caesar_cipher(encoded_text, -13)
