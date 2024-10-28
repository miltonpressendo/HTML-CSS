import hashlib
import time

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    nonce = 0
    while True:
        text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith(prefix_str):
            print(f"Mining successful with nonce: {nonce}")
            return hash_result
        nonce += 1

# Parâmetros de exemplo
block_number = 1
transactions = "Alice pays Bob 5 BTC"
previous_hash = "0000000000000000000769c1be66e8b4c7e19f58b3ea4d982b8ec373acf108d8"
prefix_zeros = 4

# Iniciando o processo de mineração
start_time = time.time()
new_hash = mine(block_number, transactions, previous_hash, prefix_zeros)
end_time = time.time()

print(f"New hash: {new_hash}")
print(f"Time taken: {end_time - start_time} seconds")
