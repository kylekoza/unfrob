import argpase

parser = argparse.ArgumentParser(description="(Un)Memfrob a string.")
parser.add_argument('string', help="The string to (un)frob.")

args = parser.parse_args()
args = vars(args)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

key = "*"*len(args["string"])  

print strxor(key, args["string"])
