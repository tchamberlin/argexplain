#! /usr/bin/env python3

"""Print an explanation of the arguments this script receives

"""


import argparse
import shlex
import sys
import unicodedata

from rich.console import Console
from rich.table import Table

console = Console()


def render_character(char: str):
    # return shlex.quote(char)
    return char if char.isprintable() else repr(char).strip("'").strip('"')


def create_arg_list(argv: list[str]):
    return (f"  {i}) {arg!r}" for i, arg in enumerate(argv))


def print_arg_list(argv: list[str]):
    for arg in create_arg_list(argv):
        console.print(arg)


def create_arg_table(arg: str, title: str | None = None):
    """Display a single argument (string) in a table"""
    arg_table = Table(title=title or render_character(arg), safe_box=False)
    arg_table.add_column("Char.")
    arg_table.add_column("Codepoint")
    arg_table.add_column("Name")
    arg_table.add_column("Repr.")
    arg_table.add_column("Hex")
    for c in arg:
        try:
            name = unicodedata.name(c)
        except ValueError:
            name = "<none>"
        arg_table.add_row(
            render_character(c),
            c.encode("unicode_escape").decode("utf-8"),
            name,
            repr(c),
            hex(ord(c)),
        )
    return arg_table


def create_arg_tables(argv: list[str]):
    grid = Table.grid(expand=False)

    for i, arg in enumerate(argv):
        grid.add_row(create_arg_table(arg, f"{i}) {render_character(arg)}"))

    return grid


def print_arg_tables(argv: list[str]):
    console.print(create_arg_tables(argv))


def argexplain(argv: list[str], thing: str, verbose=False):
    """Display each argument in argv in a table"""
    console.print(f"Received {len(argv)} {thing}{':' if argv else ' (blank argv)'}")
    if verbose:
        print_arg_tables(argv)
    else:
        print_arg_list(argv)


def main():
    args, rest = parse_args()
    if not sys.stdin.isatty():
        stdin_lines = [line.rstrip("\n") for line in sys.stdin.readlines()]
        argexplain(
            stdin_lines,
            verbose=args.verbose,
            thing=f"line{'s' if len(stdin_lines) > 1 else ''} from stdin",
        )
    else:
        console.print("Received 0 lines from stdin")

    console.print()
    # By default, use the full sys.argv. But we also provide the option to ignore
    # "self" args -- script name, and flags for this script
    if args.include_own_args:
        argexplain(
            sys.argv,
            thing="arguments from the command-line",
            verbose=args.verbose,
        )
    else:
        argexplain(
            args.args + rest,
            thing="arguments from the command-line after parsing via argparse",
            verbose=args.verbose,
        )


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("args", nargs="*")
    parser.add_argument("-I", "--include-own-args", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_known_args()


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
