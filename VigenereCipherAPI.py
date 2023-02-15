from flask import Flask, request, jsonify
from VigenereCipherScript import VigenereCipher

app = Flask(__name__)

# Initialize a new VigenereCipher object
vc = VigenereCipher()

# Endpoint for encrypting a plaintext with a given key
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    key = data['key']
    ciphertext = vc.encrypt(plaintext, key)
    return jsonify({'ciphertext': ciphertext})

# Endpoint for decrypting a ciphertext with a given key
@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = data['key']
    plaintext = vc.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.run(debug=True)
