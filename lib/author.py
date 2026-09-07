class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        from lib.contract import Contract

        return [
            contract for contract in Contract.all
            if contract.author == self
        ]

    def books(self):
        return [
            contract.book for contract in self.contracts()
        ]

    def sign_contract(self, book, date, royalties):
        from lib.contract import Contract

        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(
            contract.royalties
            for contract in self.contracts()
        )