import argparse
parser = argparse.ArgumentParser(description="какой файл обрабатываем?")
parser.add_argument("way", help = "путь к файлу", type = str)
args = parser.parse_args()

with open (f"{args.way}") as file:
    count = 0
    chains = [line.replace("\n","") for line in file.readlines()]
    for i in range(len(chains[0])-1):
        if chains[0][i] != chains[1][i]:
            count += 1
print(count)
