items = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
unique_item = set()
for item in items:
    if item in unique_item:
        print("duplicate", item)
        break
    else:
        unique_item.add(item)
