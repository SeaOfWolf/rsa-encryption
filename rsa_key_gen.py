# RTFM https://cryptography.io/en/42.0.5/hazmat/primitives/asymmetric/rsa/

import base64
import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Create private key
private_key = rsa.generate_private_key(
    public_exponent=65537, # exponent used to decode the original value
    key_size=2048, # number of bits used in the key
)

# Create public key
public_key = private_key.public_key() # An RSA public key object corresponding to the values of the private key

# Serialize private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)

# Write private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_pem)

# Serialize public key
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(public_pem)