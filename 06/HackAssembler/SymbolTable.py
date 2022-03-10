class SymbolTable(object):
    def __init__(self):
        self.symbols = {}
        self.symbol_index = 16

        with open("symbols.csv", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    symbol, address = line.split(",")
                    self.add_entry(symbol, address)

    def add_labels(self, labels):
        for label in labels:
            self.add_entry(label, labels[label])

    def add_entry(self, symbol, address):
        self.symbols[symbol] = int(address)

    def get_address(self, symbol):
        if symbol not in self.symbols:
            self.add_entry(symbol, self.symbol_index)
            self.symbol_index += 1
        return self.symbols[symbol]
