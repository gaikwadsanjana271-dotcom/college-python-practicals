# Practical: Linear Search and Binary Search using Strings

def linear_search():
    names = ["Amit", "Rahul", "Priya", "Sneha", "Neha"]
    search = input("Enter name to search: ")
    found = False

    for i in range(len(names)):
        if names[i] == search:
            print("Name found at position", i + 1)
            found = True
            break

    if not found:
        print("Name not found.")


def binary_search():
    # Binary Search requires the list to be sorted alphabetically.
    names = ["Amit", "Neha", "Priya", "Rahul", "Sneha"]
    search = input("Enter name to search: ")
    low = 0
    high = len(names) - 1

    while low <= high:
        mid = (low + high) // 2

        if names[mid] == search:
            print("Name found at position", mid + 1)
            return
        elif search > names[mid]:
            low = mid + 1
        else:
            high = mid - 1

    print("Name not found.")


if __name__ == "__main__":
    print("--- Linear Search ---")
    linear_search()
    print("\n--- Binary Search ---")
    binary_search()
