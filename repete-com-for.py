#!/usr/bin/env python3

original = [1, 2, 3]

# Programação Estruturada
# List
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(f"Lista estruturada: {dobrada}")

# Programação Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print("Lista funcional: {dobrada}")

# Programação Estruturada
# Dict
dados = {}
for line in open("post.txt"):
    if ":" in line:
        key, value = line.split(":")
        dados[key] = value.strip()
print(f"Dict estruturado: {dados}")

# Programação Funcional
# Dict
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
print(f"Dict funcional: {dados}")
