import sys

from Code import Code
from Parser import Parser
from SymbolTable import SymbolTable


# Usage: python HackAssembler.py <input_file>
# Example: python HackAssembler.py ../pong/Pong.asm

def main():
    f = open(sys.argv[1], "r")
    lines = f.readlines()

    symbol_table = SymbolTable()
    code = Code(symbol_table)
    parser = Parser(lines)
    parser.remove_comments()
    parser.read_labels()

    symbol_table.add_labels(parser.labels)

    for line in parser.lines:
        instruction = parser.read_instructions(line)

        if instruction["type"] is None:
            continue
        elif instruction["type"] == "a":
            code.add_a_instruction(instruction)
        elif instruction["type"] == "c":
            code.add_c_instruction(instruction)

    name = sys.argv[1].split("/")[-1].split(".")[0]

    with open("out/" +name + ".hack", "w") as f:
        for instruction in code.instructions:
            f.write(instruction + "\n")


if __name__ == "__main__":
    main()
