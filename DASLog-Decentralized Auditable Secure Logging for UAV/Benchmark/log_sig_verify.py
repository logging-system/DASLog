from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def verify_signature(public_key, message, signature):
    """Verifies the signature of a message using a public key."""
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        print("Signature is valid.")
        return True
    except:
        print("Signature is invalid.")
        return False