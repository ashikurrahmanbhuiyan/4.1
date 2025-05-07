import hashlib

def hash_func(data):
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(leaves):
    hashes = [hash_func(leaf) for leaf in leaves]
    tree = [hashes]  # level 0

    while len(hashes) > 1:
        next_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else left  # duplicate last if odd
            combined = hash_func(left + right)
            next_level.append(combined)
        tree.append(next_level)
        hashes = next_level

    return tree

def get_proof(tree, index):
    proof = []
    for level in tree[:-1]:
        sibling_index = index ^ 1  # flip last bit (0<->1)
        if sibling_index < len(level):
            proof.append(level[sibling_index])
        index //= 2
    return proof

def verify_merkle_proof(leaf, proof, root, index):
    current_hash = hash_func(leaf)
    for sibling_hash in proof:
        if index % 2 == 0:
            current_hash = hash_func(current_hash + sibling_hash)
        else:
            current_hash = hash_func(sibling_hash + current_hash)
        index //= 2
    return current_hash == root

# Sample data
leaves = ["data0", "data1", "data2", "data3"]
tree = build_merkle_tree(leaves)
root = tree[-1][0]
index_to_check = 2
leaf = "data2"
print(leaf)
proof = get_proof(tree, index_to_check)

# Verify
is_member = verify_merkle_proof(leaf, proof, root, index_to_check)
print("Merkle Root:", root)
print("Proof:", proof)
print("Is member:", is_member)
