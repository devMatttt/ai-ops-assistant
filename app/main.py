import sys

def greet(name: str) -> str:
    return f"Hello, {name}! welcome to AI engineering."

def sum(a: int, b:int) -> int:
    total = a + b
    return f"The sum of {a} & {b} is {total}"

def prompt(question: str)-> str:
    return f"Question: {question}"

def main() -> None:

    if len(sys.argv) > 1:

        message = greet(sys.argv[1])

        if sys.argv[1] == 'sum':
            message = sum(1, 5)

        if "?" in sys.argv[1]:
            message = prompt(sys.argv[1])

        print(message)

    else:
        print("No params found")

if __name__ == "__main__":
    main()