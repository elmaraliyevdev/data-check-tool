import argparse
from data_check_tool.processor import process_file


def main():
    parser = argparse.ArgumentParser(description="Data Check Tool")
    parser.add_argument("--input", required=True)
    parser.add_argument(
        "--output",
        default="output.csv",
        help="Output CSV file (default: ./output.csv)",
    )

    args = parser.parse_args()
    process_file(args.input, args.output)


if __name__ == "__main__":
    main()