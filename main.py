import argparse
import importlib.metadata
from pathlib import Path
import sys

import vcd_tools

if __name__ == "__main__":
    print(f"{__file__}:__main__")

    parser = argparse.ArgumentParser()

    # Optional argument flag which defaults to False
    parser.add_argument("-d", "--debug", action="store_true", default=False)

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbosity (-v, -vv, etc)"
    )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(
            version=importlib.metadata.version("vcd_tools")
        ),
    )

    # Action to perform:
    parser.add_argument(
        "-a", "--action", action="store", default="find_binary_pattern", help="action to perform: beat_counter, find_binary_pattern, etc"
    )

    # path to file
    parser.add_argument(
        "-f", "--file",
        type=Path,
        default=None,
        help="Path to the iladata file directory",
    )

    args = parser.parse_args()

    ifile = args.file
    if ifile is None:
        ifile = vcd_tools.file_selector()
    if ifile.exists():
        vcd_parse = vcd_tools.parse(ifile)
    else:
        print(f"VCD file {ifile} does not exist.")
        sys.exit(1)

    if "find_binary_pattern" in args.action:
        vcd_tools.find_binary_pattern(vcd_parse)
