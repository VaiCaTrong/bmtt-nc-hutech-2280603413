from flask import Flask, request, jsonify
from Cipher.Caesar import CaesarCipher
app = Flask(__name__)

Caesar_cipher = CaesarCipher()

@app.route("/API/Caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = Caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'encrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
@app.route("/API/Caesar/decrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = Caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)