def hash_func(key, size):
    return sum(ord(ch) for ch in key) % size


def hash_table_chains(text, size=50):
    table = [[] for _ in range(size)]
    for word in text.split():
        idx = hash_func(word, size)
        table[idx].append(word)
    return table



with open("input.txt", "w", encoding="utf-8") as f:
    f.write("hello world this is a test hello world\n")
    f.write("python is a great language\n")


with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()


table = hash_table_chains(text, size=50)


with open("hash_table_chains.txt", "w", encoding="utf-8") as f:
    for i, chain in enumerate(table):
        if chain:
            f.write(f"{i}: {chain}\n")

print("Готово. Результат в hash_table_chains.txt")
