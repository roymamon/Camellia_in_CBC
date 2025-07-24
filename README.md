Camellia in a CBC mode

This project implements the Camellia block cipher in Python, including support for:
	• ECB mode (single block encryption)
	• CBC mode (full-message encryption with padding)

How to run:

python3 main.py

How to use:

	1.	Choose a Mode:
	•	[1] → ECB mode (raw Camellia block 
	•	[2] → CBC mode (secure full-message encryption with IV)
	2.	Choose Action:
	•	[E] → Encrypt
	•	[D] → Decrypt
	3.	Provide Required Inputs.
	4.	Receive Output:

You can type -1 at any point to exit.

Sources:
1. RFC 3713 – Camellia Encryption Algorithm: https://datatracker.ietf.org/doc/html/rfc3713
2. NIST SP 800-38A – “Recommendation for Block Cipher Modes of Operation”: https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-38a.pdf
3. RFC 4312 – Camellia for IPsec: https://datatracker.ietf.org/doc/html/rfc4312
4. Specification of Camellia — CRYPTREC (Japan’s Cryptography Research): https://www.cryptrec.go.jp/en/cryptrec_03_spec_cypherlist_files/PDF/06_01espec.pdf
5. Camellia official website: https://info.isl.ntt.co.jp/crypt/eng/camellia/

