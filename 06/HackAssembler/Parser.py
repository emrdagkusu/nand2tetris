class Parser(object):
    def __init__(self, lines):
        self.lines = lines

    def remove_comments(self):
        lines = []
        for line in self.lines:
            line = line.partition("//")[0]
            line = line.strip()
            line = line.replace(" ", "")
            if line:
                lines.append(line)
        self.lines = lines

    def read_labels(self):
        labels = {}
        l_count = 0
        for index, line in enumerate(self.lines):
            if line.startswith("("):
                label = line[1:-1]
                labels[label] = index - l_count
                l_count += 1
        self.labels = labels

    def read_instructions(self, line):
        if line.startswith("@"):
            return self.read_a_instruction(line)
        elif line.startswith("("):
            return {"type": None}
        else:
            return self.read_c_instruction(line)

    def read_a_instruction(self, line):
        instruction = {"type": "a"}

        line = line.partition("@")[2]
        line = line.strip()

        if line.isdigit():
            instruction["value"] = int(line)
        else:
            instruction["symbol"] = line

        return instruction

    def read_c_instruction(self, line):
        instruction = {"type": "c"}

        splitted_line = line.split(";")

        if len(splitted_line) == 1:
            jump = "null"
        elif len(splitted_line) == 2:
            jump = splitted_line[1].strip()

        splitted_line = splitted_line[0].split("=")

        if len(splitted_line) == 1:
            comp = splitted_line[0].strip()
            dest = "null"
        elif len(splitted_line) == 2:
            comp = splitted_line[1].strip()
            dest = splitted_line[0].strip()

        instruction["dest"] = dest
        instruction["comp"] = comp
        instruction["jump"] = jump

        return instruction
