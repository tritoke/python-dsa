#!/usr/bin/env python

import hashlib
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import secrets

# key length
L = 3076
N = 256

# hash function
def H(data):
    hasher = hashlib.sha256()
    hasher.update(long_to_bytes(data))
    return bytes_to_long(hasher.digest())

# this is too slow lmao
# q = getPrime(N)
# p = getPrime(L)
# while (p - 1) % q != 0:
#     p = getPrime(L)

# openssl dsaparam -text -genkey 3076
p = bytes_to_long(bytes([0x0d, 0xcf, 0xa7, 0x4d, 0x54, 0x99, 0xeb, 0x3b, 0x6b, 0x14, 0xf5, 0x8d, 0x0f, 0x51, 0x4a, 0xca, 0xae, 0x94, 0x62, 0xc0, 0x3d, 0xe5, 0x77, 0x6d, 0xee, 0xc4, 0x9a, 0x9c, 0x05, 0xca, 0x36, 0x2b, 0x55, 0x78, 0xcf, 0xb8, 0x74, 0xe6, 0x1e, 0xa3, 0x74, 0x35, 0x57, 0x57, 0x35, 0x48, 0x34, 0xff, 0x40, 0x8e, 0x12, 0x74, 0xcc, 0xad, 0x40, 0xfa, 0xf3, 0x57, 0xd2, 0xe8, 0x7d, 0x5a, 0x46, 0x52, 0x6b, 0x73, 0xf4, 0xb4, 0x42, 0x0e, 0xf4, 0xb3, 0x3f, 0x86, 0x7f, 0x49, 0x83, 0x95, 0x60, 0xa3, 0x85, 0x2a, 0xc7, 0x34, 0x5c, 0x2b, 0x88, 0x74, 0x09, 0x49, 0x1b, 0x53, 0xcc, 0x21, 0x21, 0x78, 0x8e, 0xf3, 0xaa, 0xa2, 0x07, 0x5b, 0xdb, 0xa9, 0xc6, 0x85, 0xe1, 0x77, 0xb9, 0x03, 0x44, 0x1f, 0x0b, 0x39, 0xd5, 0x07, 0x06, 0x3c, 0xd2, 0xc1, 0x65, 0xf5, 0x76, 0x51, 0xa5, 0xd5, 0xa2, 0xf8, 0xb7, 0xb3, 0x68, 0x5b, 0x2c, 0x40, 0x19, 0xa9, 0xf6, 0x52, 0x74, 0x8f, 0x3c, 0x34, 0xad, 0xd8, 0x6b, 0x4f, 0x80, 0xfa, 0x24, 0x1f, 0x5f, 0x02, 0xd2, 0x7b, 0x34, 0xe3, 0x4e, 0x65, 0xea, 0xc4, 0xef, 0xc3, 0x32, 0x9a, 0xb9, 0x13, 0x19, 0xbd, 0x57, 0xf7, 0x3a, 0x81, 0x04, 0x90, 0x89, 0x6d, 0x7d, 0x67, 0xde, 0x3c, 0x22, 0x86, 0x89, 0x70, 0xd2, 0x23, 0xbf, 0x8e, 0xd3, 0x57, 0x0d, 0xcb, 0x35, 0xde, 0xab, 0xf3, 0x65, 0x8e, 0xc9, 0x2a, 0x39, 0xf7, 0x99, 0xde, 0xf6, 0x7a, 0xc1, 0x38, 0x28, 0x01, 0x9b, 0x74, 0x7a, 0x91, 0xed, 0x0d, 0x8c, 0xa0, 0x0f, 0xd8, 0x00, 0x11, 0x56, 0x8f, 0x30, 0x41, 0x9e, 0x35, 0x32, 0xa3, 0x1c, 0x15, 0xe0, 0xd3, 0x38, 0x6e, 0xcb, 0xa3, 0xfd, 0x38, 0x92, 0xf4, 0x30, 0xb5, 0x5d, 0x12, 0x45, 0xea, 0xd7, 0x84, 0xf7, 0x0a, 0xb7, 0x03, 0x68, 0x81, 0x89, 0xda, 0x7b, 0xad, 0xd6, 0x9f, 0x41, 0xb1, 0x58, 0x83, 0xdc, 0x42, 0xcc, 0x76, 0xf3, 0x4e, 0x99, 0xf7, 0x08, 0x60, 0xfd, 0xab, 0x7a, 0x66, 0x44, 0xcd, 0x40, 0xf4, 0x89, 0x48, 0xc5, 0xd5, 0x3c, 0xca, 0x4a, 0x74, 0x99, 0xda, 0x7b, 0x17, 0x21, 0x4c, 0x91, 0xf9, 0x45, 0x18, 0xc4, 0x29, 0x89, 0x7a, 0xee, 0x58, 0x64, 0x38, 0x76, 0xd2, 0xde, 0xb4, 0xb3, 0x9f, 0xf5, 0xc7, 0x7e, 0x97, 0xc8, 0xb5, 0x79, 0x18, 0x8f, 0x27, 0xa9, 0x9c, 0xa2, 0xdd, 0x87, 0x1d, 0x89, 0x44, 0x92, 0xb0, 0x45, 0xf5, 0x2c, 0xea, 0x67, 0xa6, 0xe5, 0x1b, 0x79, 0x2d, 0xb1, 0x5f, 0x8f, 0xfa, 0xcc, 0xf7, 0x35, 0xf5, 0xc7, 0x6c, 0x31, 0x4c, 0xab, 0xbc, 0xff, 0x8b, 0xc6, 0x01, 0x99, 0x60, 0xc9, 0xb2, 0xbe, 0xf4, 0xea, 0xa9, 0x60, 0xd1, 0xf1, 0x45, 0x3d, 0x0e, 0x14, 0x54, 0x98, 0xf0, 0x0a, 0x3b, 0xcf]))
q = bytes_to_long(bytes([0x00, 0xd4, 0x19, 0xbd, 0x24, 0x35, 0xa0, 0xde, 0x6a, 0x0a, 0xdc, 0x06, 0x20, 0x82, 0x12, 0xbd, 0x0e, 0x4d, 0xd4, 0x7b, 0x0b, 0x93, 0xd4, 0x77, 0x51, 0x6b, 0x6d, 0x27, 0x55]))
g = bytes_to_long(bytes([0x0a, 0x18, 0x9b, 0x62, 0xd5, 0x4d, 0x12, 0xd5, 0x4f, 0x3e, 0x06, 0x5c, 0x1a, 0x3d, 0x89, 0x66, 0x29, 0xf9, 0x9d, 0x93, 0x84, 0xbf, 0xde, 0x05, 0xb7, 0x39, 0x54, 0x94, 0xcc, 0x56, 0x7a, 0x4c, 0x41, 0xae, 0x35, 0x80, 0x22, 0x69, 0xb4, 0x62, 0x0a, 0x6d, 0x89, 0x10, 0xc2, 0x06, 0x82, 0xc7, 0xad, 0xf7, 0xe5, 0x95, 0x71, 0x6e, 0x56, 0x61, 0x80, 0xb9, 0xde, 0xae, 0x40, 0xc9, 0x3e, 0x06, 0xa4, 0x6a, 0x84, 0xeb, 0xd0, 0x93, 0x80, 0xad, 0x17, 0xda, 0x0b, 0xf7, 0xc3, 0x57, 0xde, 0x41, 0xc2, 0xaa, 0xc5, 0x98, 0x73, 0x50, 0xaf, 0x2d, 0x2c, 0x6e, 0x35, 0x05, 0x15, 0x40, 0x90, 0x76, 0x8b, 0x31, 0xeb, 0x03, 0xec, 0x63, 0xf2, 0x6b, 0x7e, 0xd2, 0xc3, 0x9f, 0x32, 0xa8, 0xb5, 0x46, 0x89, 0x28, 0x06, 0x0a, 0xa4, 0x85, 0x53, 0x44, 0x30, 0x6d, 0xf3, 0xb7, 0x1b, 0x61, 0xcb, 0xce, 0xfb, 0x98, 0xb7, 0x8c, 0x5e, 0xb9, 0x73, 0x80, 0xaf, 0x06, 0x5e, 0xc2, 0xb3, 0xaa, 0x51, 0xae, 0x8f, 0x6c, 0xe3, 0xca, 0x68, 0xad, 0x98, 0x91, 0x1e, 0xe1, 0x8f, 0x93, 0x3d, 0xc8, 0xfe, 0xdf, 0x41, 0xc4, 0x01, 0x03, 0xdd, 0xe3, 0x0a, 0x13, 0xd6, 0xec, 0x37, 0x1e, 0xd0, 0x5c, 0x5c, 0xd3, 0x9c, 0x54, 0xd9, 0x5c, 0x6a, 0xf4, 0x05, 0x33, 0x08, 0xc7, 0x1f, 0xab, 0x3f, 0xeb, 0x17, 0x6e, 0x0f, 0xfb, 0x21, 0x80, 0xed, 0x62, 0xb8, 0x0b, 0x8f, 0x60, 0xc8, 0x4b, 0xeb, 0x5e, 0x24, 0x70, 0x7c, 0x88, 0x1f, 0x65, 0x2a, 0xe6, 0xf3, 0x89, 0x79, 0x28, 0x98, 0xd4, 0x13, 0x2f, 0xe4, 0xa3, 0xe4, 0x03, 0x32, 0xe5, 0xe8, 0xa8, 0xe9, 0xb8, 0xcf, 0xaf, 0x68, 0x8a, 0x94, 0x7f, 0xe2, 0xf0, 0xa2, 0xf0, 0x2a, 0xe6, 0x6b, 0x01, 0x72, 0x92, 0x3f, 0x10, 0xce, 0x66, 0x61, 0xdc, 0xbc, 0x1b, 0xb3, 0x06, 0x23, 0x7f, 0x7c, 0x02, 0x98, 0x07, 0xb0, 0xac, 0x45, 0x27, 0x1c, 0x17, 0x94, 0xcf, 0xd9, 0xa3, 0x72, 0xec, 0xbe, 0x7b, 0x5c, 0x21, 0x57, 0xfb, 0x33, 0x99, 0x27, 0x2a, 0xb6, 0x4b, 0xaa, 0xd3, 0xb2, 0x5d, 0x4f, 0x59, 0xe1, 0x30, 0x4d, 0xc5, 0xd1, 0xd5, 0x7b, 0xaa, 0x7f, 0x3b, 0xcc, 0x7a, 0x02, 0xb2, 0x54, 0x07, 0xce, 0xed, 0x2e, 0x5a, 0xde, 0xff, 0x7a, 0xd0, 0x11, 0xc0, 0x2e, 0xe4, 0x5c, 0xff, 0xb0, 0xec, 0x40, 0x8d, 0xc7, 0xff, 0x67, 0x86, 0x65, 0x72, 0xb9, 0xee, 0x07, 0xf0, 0xf1, 0x33, 0x22, 0x64, 0x66, 0x0c, 0x0a, 0xb2, 0x43, 0x3c, 0xcc, 0x67, 0x4e, 0xcf, 0x5f, 0xed, 0x3f, 0xc2, 0x2e, 0x75, 0xb7, 0x30, 0x87, 0x8e, 0xbb, 0x5d, 0xb0, 0x39, 0x37, 0xe6, 0xde, 0x1d, 0x91, 0x3f, 0x20, 0xf3, 0xdd, 0x26, 0x52, 0xfa, 0xac, 0x6a, 0x02, 0x62, 0x8d, 0x0e, 0x41]))

# check we've imported the command correct
assert (p - 1) % q == 0

# generate our user's key
x = 1 + secrets.randbelow(q - 1)
y = pow(g, x, p)

print(x, y)

def sign(message: bytes):
    m = bytes_to_long(message)
    while True:
        k = 1 + secrets.randbelow(q - 1)
        r = pow(g, k, p) % q

        if r == 0:
            continue

        k_inv = pow(k, -1, q)
        s = k_inv * (H(m) + x * r) % q
        if s == 0:
            continue

        break

    return (r, s)

def verify(message: bytes, r: int, s: int) -> bool:
    if not (0 < r < q and 0 < s < q):
        return False

    m = bytes_to_long(message)
    w = pow(s, -1, q)
    u1 = H(m) * w % q
    u2 = r * w % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

    print(v, r)
    return v == r

message = b"Wow I sure do love messages!!!!"
r, s = sign(message)
print(message, r, s)
assert verify(message, r, s)

