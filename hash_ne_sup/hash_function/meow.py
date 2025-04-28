def custom_hash(data: bytes) -> bytes:
    state = bytearray(32)

    for i, b in enumerate(data):
        state[i % 32] = (state[i % 32] + b + (i % 256)) % 256

    for i in range(32):
        state[i] = (state[i] ^ (state[(i - 1) % 32] + state[(i - 3) % 32])) % 256

    return bytes(state)
