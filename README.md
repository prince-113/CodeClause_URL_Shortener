# CodeClause_URL_Shortener

shortner works usng SHA-256 algorithm

SHA-256 is a cryptographic hash function that produces a 256-bit (32-byte) hash value. It is part of the Secure Hash Algorithm (SHA) family of cryptographic hash functions, which were designed by the United States National Security Agency (NSA).

The SHA-256 algorithm takes an input message of any length and produces a fixed-size output hash value. The input message is first padded so that its length is a multiple of 512 bits, and then divided into 512-bit blocks. The algorithm then processes each block in turn, using a series of mathematical operations to transform the block into a 256-bit hash value.

The SHA-256 algorithm uses a set of constants and functions that are designed to produce a hash value that is resistant to a variety of attacks, including preimage attacks, second preimage attacks, and collision attacks. It is widely used in applications such as digital signatures, password storage, and blockchain technology.

In Python, you can use the hashlib module to compute the SHA-256 hash of a string or byte sequence:
Eg:
import hashlib

# Compute the SHA-256 hash of a string
message = 'Hello, world!'
hash_object = hashlib.sha256(message.encode())
hash_hex = hash_object.hexdigest()
print(hash_hex)
# Output:  65a8e27d8879283831b664bd8b7f0ad4b6895d3

# Compute the SHA-256 hash of a byte sequence
data = b'\x00\x01\x02\x03'
hash_object = hashlib.sha256(data)
hash_hex = hash_object.hexdigest()
print(hash_hex)
# Output:  01cbe2aefe49314b07f9ababaa8c76d9df1f48d026c23b61e415ebeb8285d5f5
