import logging
import argparse

from pythonplusplus.preprocessor import preprocess_code


def main():
    parser = argparse.ArgumentParser(description="A Python script with custom preprocessor.")
    parser.add_argument('script', help="The Python script to execute.")
    parser.add_argument('--debug', action='store_true', help="Enable debug logging.")

    args = parser.parse_args()

    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level)

    script_path = args.script

    with open(script_path, 'r') as file:
        source_code = file.read()

    preprocessed_code = preprocess_code(source_code)
    logging.debug("Preprocessed Code:\n%s", preprocessed_code)

    try:
        exec(preprocessed_code, {"__name__": "__main__", "file": script_path})
    except Exception as e:
        print(f"Execution Error: {e}")


if __name__ == "__main__":
    main()