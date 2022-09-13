"""
  Contract
  @author Blazed Labs LLC
  @standard BBS-1
"""
import hashlib
import uuid
import random

import block

# Generate Chain id:
# uuid.uuid4()
# ex: f50ec0b7-f960-400d-91f0-c42a6d44e3d0


# Generate wallet address:
# uuid.uuid4().hex
# ex: [ROUTING]::9fe2c4e93f654fdbb24c02b15259716c

class Contract:

    def __init__(self, config):
        self.id = str(uuid.uuid4())
        self.name = config['name']
        self.symbol = config['symbol']
        self.uri = self.symbol + "://" + self.id + "/"
        self.period = [0, 0]
        self.total = 0
        self.transactionLimit = 0
        self.blocks = 0
        self.chain = []

    def mintBlock(self, prev='0'):
      b = block.Block({
        'prev_hash': prev
      })
      self.chain.append(b)
