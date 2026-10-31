"""A standalone rehearsal application; not part of the fr distribution."""

import argparse

NAME = "collected-closeout-fixture"
VERSION = "1"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=NAME)
    parser.add_argument("--version", action="store_true", help="Print the fixture version.")
    args = parser.parse_args(argv)
    print(VERSION if args.version else NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
