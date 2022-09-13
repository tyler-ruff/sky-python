"""
  Block
  @author Blazed Labs LLC
  @standard BBS-1
"""
import hashlib
import uuid
import random
import time

# Generate Block hash
# sha256(id + nonce + prev_hash)
# ex: 7762e509418c1be06ef23b8201dc2cdc1a678637bc9a5a38c4b0881bdf8363ff

class Block:
  def __init__(self, config):
    self.id = uuid.uuid4().hex
    self.prevHash = config['prev_hash']
    self.nonce = str(random.getrandbits(10))
    self.hash = hashlib.sha256(
      self.id.encode('utf-8') + self.nonce.encode('utf-8') +
      self.prevHash.encode('utf-8')).hexdigest()
    self.transactions = []

  def transaction(self, config):
    t = {
      'from': config['from'],
      'to': config['to'],
      'amount': config['amount'],
      'timestamp': round(time.time()*1000)
    }
    self.transactions.append(t)


