class Code(object):
    def __init__(self, symbol_table):
        self.instructions = []
        self.symbol_table = symbol_table

        self.dest_dict = {
            "null": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }

        self.jump_dict = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }

        self.comp_dict = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101",
        }

    def add_a_instruction(self, instruction):
        if "value" in instruction:
            self.instructions.append(self.get_binary_code(instruction["value"]))
        else:
            value = self.symbol_table.get_address(instruction["symbol"])
            self.instructions.append(self.get_binary_code(value))

    def add_c_instruction(self, instruction):
        dest = self.dest_dict[instruction["dest"]]
        comp = self.comp_dict[instruction["comp"]]
        jump = self.jump_dict[instruction["jump"]]

        self.instructions.append("111" + comp + dest + jump)

    def get_binary_code(self, decimal):
        return bin(decimal)[2:].zfill(16)
