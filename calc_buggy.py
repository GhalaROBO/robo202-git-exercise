def do(a: float, b: float, op: str) -> float:
    """Simple calculator with four operations."""
    if op in ("add", "plus"):
        return a + b
    if op == "sub":
        return a - b
    if op in ("mult", "mul"):
        return a * b
    if op == "div":
        if b == 0:
            print("Error: division by zero")
            return 0.0
        return a / b
    print("Unknown operation")
    return 0.0


def main():
    print("CALCULATOR")
    x = float(input("1st number: "))
    y = float(input("2nd number: "))
    z = input("operation (add/sub/mult/div): ").strip().lower()
    print("Answer is:", do(x, y, z))


if __name__ == "__main__":
    main()

