This README provides an overview of the code and instructions for running the Diffie-Hellman Key Exchange implementation for secure communication between two parties, Alice and Bob, while an eavesdropper, Darth, attempts to intercept messages. The code is implemented in Python and focuses on generating a shared secret key for encryption.

Learning Objectives
- Construct an application that communicates over UDP.
- Implement the Diffie-Hellman key exchange method.
- Use the Custom Encryption technique developed in Lab 3 for secure communication.

# Components
* dh.py
- This module contains the implementation of the Diffie-Hellman key exchange algorithm. It includes three functions:

1. power(a, b, p): Calculates a^b mod p using Python's pow function.
2. dh_generatePublicKey(P, G, privateKey): Generates and returns a public key using the provided prime number P, generator G, and a private key chosen by the sender.
3. dh_generateSecretKey(publicKey, privateKey, P): Generates and returns a secret key using the public key, private key, and prime number P.

* alice.py
This module represents Alice, one of the communicating parties. It includes functions for generating a shared key and encrypting messages. It uses the Diffie-Hellman key exchange algorithm to establish a shared secret with Bob.

* bob-1.py
This module represents Bob, the other communicating party. It includes functions for generating a shared key and decrypting messages. It also uses the Diffie-Hellman key exchange algorithm to establish a shared secret with Alice.

* darth.py
This module represents the eavesdropper, Darth, who also uses the Diffie-Hellman key exchange algorithm to intercept the shared key. However, Darth's purpose is to demonstrate the security of the key exchange.

lab6_support.py
This module provides a set of helper functions for message encryption and decryption. It contains the encrypt and decrypt functions for securely transmitting and receiving messages using a custom encryption technique.

Instructions
Make sure you have Python installed on your system.

Run Alice's code by executing alice.py:

'python alice.py'

Alice will establish a shared secret key with Bob using the Diffie-Hellman key exchange algorithm and send encrypted messages.

Run Bob's code by executing bob-1.py:

'python bob-1.py'

Bob will also establish a shared secret key with Alice and decrypt messages received from her.

To test the eavesdropping scenario, you can run Darth's code:

'python darth.py'

Darth will intercept the shared secret key using the Diffie-Hellman key exchange algorithm, but the shared secret will remain secure due to encryption.

Follow the prompts to send and receive messages securely between Alice and Bob. To exit, type 'exit' in either Alice or Bob's terminal.

Additional Notes
- The code uses custom encryption for message transmission, which is a simple custom encryption technique developed in Lab 3. You can modify the cipherEncrypt function in lab6_support.py for different encryption methods if desired.
- The code demonstrates the use of Diffie-Hellman key exchange for secure communication. The shared key between Alice and Bob remains secret, even if an eavesdropper (Darth) intercepts it.
- To change the values of P, G, and private keys for Alice and Bob, you can update the corresponding variables in the alice.py and bob-1.py files.





