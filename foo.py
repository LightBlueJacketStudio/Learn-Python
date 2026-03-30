evens_filter = [x for x in range(10) if x % 2 == 0]
evens_front = ["even" if x%2 == 0 else "odd" for x in range(10)]
print(f"filter: {evens_filter}")
print(f"front: {evens_front}")