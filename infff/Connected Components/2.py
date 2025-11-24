import argparse
pars = argparse.ArgumentParser(description="путь к файлуууууу")
pars.add_argument("-i","--way",help="никто не поможет", required=True,type=str)
args = pars.parse_args()


with open(f"{args.way}") as file:
    lines = [line.strip() for line in file.readlines()]

n, m = map(int, lines[0].split())

adj = [[] for _ in range(n + 1)]
for line in lines[1:]:
    u, v = map(int, line.split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

stack = []
components = 0

for start in range(1, n + 1):
    if not visited[start]:
        components += 1
        stack.append(start)
        visited[start] = True

        while stack:
            v = stack.pop()
            for to in adj[v]:
                if not visited[to]:
                    visited[to] = True
                    stack.append(to)

print(components)
