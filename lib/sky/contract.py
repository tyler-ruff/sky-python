"""
  Contract
  @author Blazed Labs LLC
  @standard BBS-1
"""


class Contract:

    def __init__(self):
        self.hash = ""
        self.name = ""
        self.symbol = ""
        self.uri = ""
        self.period = [0, 0]
        self.totalNFT = 0
        self.transactionLimit = 0
        self.block = 0
        self.chain = []

    def transfer(self, config):
        pass
