import pytest
from hash_function.meow import custom_hash

def test_hash_length():
    assert len(custom_hash(b"hello")) == 32
    assert len(custom_hash(b"")) == 32
    assert len(custom_hash(b"a" * 1000)) == 32

def test_hash_different_inputs():
    assert custom_hash(b"hello") != custom_hash(b"world")
    assert custom_hash(b"hello") != custom_hash(b"hello ")

def test_hash_same_input_same_output():
    assert custom_hash(b"OpenAI") == custom_hash(b"OpenAI")
