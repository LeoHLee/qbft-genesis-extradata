import sys
from eth_utils import *
import rlp
fileName = sys.argv[1]
validatorAddressList = []
with open(fileName) as f:
	validatorList = f.readlines()
	for validatorEntry in validatorList:
		validatorEntry = validatorEntry.strip()
		if validatorEntry[0:5] == 'enode':
			# enode
			pubkey = validatorEntry.split("//")[1].split("@")[0]
			validatorAddress = keccak(hexstr = "0x" + pubkey)[-20:]
		elif is_address(validatorEntry):
			validatorAddress = decode_hex(validatorEntry)
		else:
			print(validatorEntry, is_address(validatorEntry))
			raise Exception("Invalid representation: " + validatorEntry)
		validatorAddressList.append(validatorAddress)
extraData = encode_hex(rlp.encode([b"\x00" * 32, validatorAddressList, [], '', []]))
print(extraData)