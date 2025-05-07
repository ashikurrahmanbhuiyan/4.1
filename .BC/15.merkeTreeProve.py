import hashlib

def hash_func(data: bytes) -> bytes:
    """SHA-256 hash function"""
    return hashlib.sha256(data).digest()

def build_merkle_tree(leaves: list[bytes]) -> list[list[bytes]]:
    """Builds a Merkle tree and returns all levels (bottom-up)."""
    tree = [list(map(hash_func, leaves))]  # bottom level (hashed leaves)

    while len(tree[0]) > 1:
        current_level = tree[0]
        next_level = []

        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1] if i+1 < len(current_level) else left
            next_level.append(hash_func(left + right))

        tree.insert(0, next_level)

    return tree  # root is tree[0][0]

def get_merkle_proof(tree: list[list[bytes]], index: int) -> list[tuple[bytes, bool]]:
    """Generates a Merkle proof for the leaf at a given index."""
    proof = []
    for level in range(len(tree) - 1, 0, -1):
        level_nodes = tree[level]
        sibling_index = index ^ 1
        is_left = sibling_index < index
        if sibling_index < len(level_nodes):
            proof.append((level_nodes[sibling_index], is_left))
        index //= 2
    return proof

def verify_merkle_proof(leaf: bytes, proof: list[tuple[bytes, bool]], root: bytes) -> bool:
    """Verifies the Merkle proof."""
    computed_hash = hash_func(leaf)
    for sibling_hash, is_left in proof:
        if is_left:
            computed_hash = hash_func(sibling_hash + computed_hash)
        else:
            computed_hash = hash_func(computed_hash + sibling_hash)
    return computed_hash == root

def get_index_of_leaf(leaves: list[bytes], leaf: bytes) -> int:
    """Finds the index of the given leaf."""
    try:
        return leaves.index(leaf)
    except ValueError:
        raise ValueError("Leaf not found in leaves list.")

# --------------------------
# Example usage
# --------------------------

if __name__ == "__main__":
    # Step 1: Define your leaf data (must be in bytes)
    leaves = [b"A", b"B", b"C", b"D"]

    # Step 2: Build the Merkle Tree
    tree = build_merkle_tree(leaves)
    root = tree[0][0]
    print("Merkle Root:", root.hex())

    # Step 3: Input leaf value instead of index
    leaf_to_prove = b"B"

    try:
        index_to_prove = get_index_of_leaf(leaves, leaf_to_prove)
        proof = get_merkle_proof(tree, index_to_prove)

        # Step 4: Verify the proof
        is_valid = verify_merkle_proof(leaf_to_prove, proof, root)
        print("Is proof valid?", is_valid)

        # Optional: print proof values
        print("\nProof path:")
        for sibling, is_left in proof:
            side = "left" if is_left else "right"
            print(f"  Sibling on the {side}: {sibling.hex()}")
    except ValueError as e:
        print("Error:", e)
