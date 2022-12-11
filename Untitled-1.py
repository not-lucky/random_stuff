with open('even_odd.py', 'w') as fl:
    print(
        "num = input(\"Enter number to check for even or odd (from 0 to 1000000):\")",
        file=fl)
    print("\nif num == 1:\n    print(\"Odd\")", file=fl)
    for i in range(2, 1000001):
        print(f"elif num == {i}:\n    print(\"Even\")",
              file=fl) if i % 2 == 0 else print(
                  f"elif num == {i}:\n    print(\"Odd\")", file=fl)
