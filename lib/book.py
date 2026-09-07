class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        from lib.contract import Contract

        return [
            contract for contract in Contract.all
            if contract.book == self
        ]

    def authors(self):
        return [
            contract.author for contract in self.contracts()
        ]
        