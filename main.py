import sys
from src.compressor import compress_file, decompress_file

def print_usage():
    print("VectorZip CLI")
    print("Usage:")
    print("  python main.py compress <file_path>")
    print("  python main.py decompress <file_path>")

def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    command = sys.argv[1].lower()
    file_path = sys.argv[2]

    try:
        if command == 'compress':
            out = compress_file(file_path)
            print("Successfully compressed to: {}".format(out))
        elif command == 'decompress':
            out = decompress_file(file_path)
            print("Successfully decompressed to: {}".format(out))
        else:
            print("Unknown command: {}".format(command))
            print_usage()
    except Exception as e:
        print("Error: Operation failed - {}".format(e))

if __name__ == "__main__":
    main()
