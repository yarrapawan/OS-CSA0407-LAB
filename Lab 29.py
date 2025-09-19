buffer = []
capacity = int(input("Enter buffer size: "))
while True:
    print("1. Produce  2. Consume  3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        if len(buffer) == capacity:
            print("Buffer full, cannot produce")
        else:
            item = input("Enter item to produce: ")
            buffer.append(item)
            print("Produced:", item)
    elif choice == 2:
        if len(buffer) == 0:
            print("Buffer empty, cannot consume")
        else:
            item = buffer.pop(0)
            print("Consumed:", item)
    else:
        break
