import sys
from pythonplusplus.lexer import lexer
from pythonplusplus.parser import parser


# Function to convert parse tree to Python code
def transform_to_python_code(parse_tree, indent=0):
    result = ""
    if isinstance(parse_tree, tuple):
        if parse_tree[0] == 'program':
            for statement in parse_tree[1]:
                result += transform_to_python_code(statement, indent) + "\n"
        elif parse_tree[0] == '=':
            result += " " * indent + f"{parse_tree[1]} = {transform_to_python_code(parse_tree[2], 0)}"
        elif parse_tree[0] == '+=':
            result += " " * indent + f"{parse_tree[1]} += {parse_tree[2]}"
        elif parse_tree[0] == '+':
            left = transform_to_python_code(parse_tree[1], 0)
            right = transform_to_python_code(parse_tree[2], 0)
            result += f"{left} + {right}"
    else:
        result += str(parse_tree)
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: mypython <script>")
        sys.exit(1)

    script_path = sys.argv[1]

    with open(script_path, 'r') as file:
        source_code = file.read()

    # Lexing
    lexer.input(source_code)
    
    # Tokenize input for debugging
    print("Tokens:")
    for token in lexer:
        print(token)

    # Parsing
    parse_tree = parser.parse(source_code, lexer=lexer)
    if parse_tree:
        print(f"Parse Tree: {parse_tree}")

        # Transform to Python code
        transformed_code = transform_to_python_code(parse_tree)
        print("Transformed Code:\n", transformed_code)

        # Execute the transformed code
        try:
            exec(transformed_code, {"__name__": "__main__", "__file__": script_path})
        except Exception as e:
            print(f"Execution Error: {e}")
    else:
        print("Failed to parse the script.")


if __name__ == "__main__":
    main()