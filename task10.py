from speck import SpeckCipher
from simon import SimonCipher

# Initialize Cipher
my_simon = SimonCipher(0xABBAABBAABBAABBAABBAABBAABBAABBA)
my_speck = SpeckCipher(0x123456789ABCDEF00FEDCBA987654321)
my_plaintext = 0xCCCCAAAA55553333
print("Original plaintext: ", my_plaintext)
# Encrypt & Decrypt
speck_ciphertext = my_speck.encrypt(my_plaintext)
print("Speck Ciphertext: ", speck_ciphertext)
speck_plaintext = my_speck.decrypt(speck_ciphertext)
print("Recovered Speck Plaintext: ", speck_plaintext)
simon_ciphertext = my_simon.encrypt(0xFFFF0000EEEE1111)
print("Simon Ciphertext: ", simon_ciphertext)
simon_plaintext = my_simon.decrypt(simon_ciphertext)
print("Recovered Simon Plaintext: ", simon_plaintext)