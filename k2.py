linked_list = {1: 2, 2: 3, 3: 4, 9: 2}
visited = set()
current = 1

while current is not None:
    if current in visited:
        print("Loop exist")
        break
    visited.add(current)
    current = linked_list.get(current)
else:
    print("loop does not exist")
