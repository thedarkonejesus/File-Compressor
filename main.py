import sys
import argparse
from tqdm import tqdm
from src.compressor import compress_file, decompress_file

def main():
    parser = argparse.ArgumentParser(
        description="VectorZip: A high-performance, chunked-processing compression utility."
    )
    parser.add_argument("action", choices=["compress", "decompress"], help="Action to perform")
    parser.add_argument("file", help="Path to the target file")
    
    args = parser.parse_args()

    try:
        if args.action == "compress":
            print("Compressing: {}".format(args.file))
            # Wrap the operation in tqdm for a progress bar
            with tqdm(total=100, desc="Processing") as pbar:
                output = compress_file(args.file)
                pbar.update(100)
            print("Success! Created: {}".format(output))
            
        elif args.action == "decompress":
            print("Decompressing: {}".format(args.file))
            with tqdm(total=100, desc="Processing") as pbar:
                output = decompress_file(args.file)
                pbar.update(100)
            print("Success! Extracted: {}".format(output))
            
    except Exception as e:
        print("Error: Operation failed - {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
