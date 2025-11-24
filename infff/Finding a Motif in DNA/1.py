import argparse
parser = argparse.ArgumentParser(description="какой файл обрабатываем?")
parser.add_argument("way", help = "путь к файлу", type = str)
args = parser.parse_args()

with open (f"{args.way}") as file:
    position = []
    chunk = [line.replace('\n', '') for line in file.readlines()]
    for i in range(len(chunk[0])-len(chunk[1])+1):
        if chunk[0][i:i+len(chunk[1])] == chunk[1]:
            position.append(i+1)
            result = ' '.join(str(n) for n in position)
print(result)