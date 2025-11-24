import argparse
pars = argparse.ArgumentParser(description="put k file")
pars.add_argument("file", help="dymat nado", type=str)
args = pars.parse_args()

sequences = []
current = ""

with open(f"{args.file}") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current != "":
                sequences.append(current)
                current = ""
        else:
            current += line

    
    if current != "":
        sequences.append(current)
n = len(sequences[0])

profile = {
    'A': [0] * n,
    'C': [0] * n,
    'G': [0] * n,
    'T': [0] * n
}

for seq in sequences:
    for i in range(n):
        letter = seq[i]
        profile[letter][i] += 1

consensus = ""
for i in range(n):
    best = None
    best_value = -1
    for base in "ACGT":
        value = profile[base][i]
        if value > best_value:
            best_value = value
            best = base
    consensus += best

print(consensus)
print("A:", *profile['A'])
print("C:", *profile['C'])
print("G:", *profile['G'])
print("T:", *profile['T'])
