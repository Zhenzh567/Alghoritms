def hash_func(key, size):
    return sum(ord(ch) for ch in key) % size


def hash_table_overlay(text, size=100):
    table = [None] * size
    for word in text.split():
        idx = hash_func(word, size)
        while table[idx] is not None:
            idx = (idx + 1) % size
        table[idx] = word
    return table



filename = "input.txt"
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()


table = hash_table_overlay(text, size=50)


with open("hash_table_overlay.txt", "w", encoding="utf-8") as f:
    for i, val in enumerate(table):
        if val is not None:
            f.write(f"{i}: {val}\n")

print("Готово. Результат в hash_table_overlay.txt")
