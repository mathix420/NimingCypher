#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import b64encode as to64, b64decode as from64
import rsa

class NExchange:
    def __init__(self, key_size):
        _public, self._private = rsa.newkeys(key_size)
        self.public = '###START-OF-NIMING-RSA-PUBLIC###%s@@%s###END-OF-NIMING-RSA-PUBLIC###' % (_public.n, _public.e)

    def encrypt_key(self, key, public_key):
        splitted_key = public_key[32:-30].split("@@")
        public = rsa.PublicKey(int(splitted_key[0]), int(splitted_key[1]))
        return '###START-OF-NIMING-KEY###%s###END-OF-NIMING-KEY###' % to64(rsa.encrypt(key.encode(), public)).decode()

    def decrypt_key(self, encrypted_key):
        return rsa.decrypt(from64(encrypted_key[25:-23].encode()), self._private).decode()

    def identity_proof(self, username):
        return '###NIMING-IDENTITY-PROOF###%s###END-IDENTITY-PROOF###' % to64(rsa.sign(username.encode(), self._private, 'SHA-1')).decode()

    def verify_identity(self, proof, emitter_name, emitter_public_key):
        splitted_key = emitter_public_key[32:-30].split("@@")
        emit_public = rsa.PublicKey(int(splitted_key[0]), int(splitted_key[1]))
        proof = from64(proof[27:-24].encode())
        return rsa.verify(emitter_name.encode(), proof, emit_public)
