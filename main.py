import argparse
import importlib.metadata

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

    args = parser.parse_args()

    solved = vcd_tools.vcd_tools_fun()
