"""
Simple tools for writing pre and post conditions in python
"""

#To use contracts, set DEBUG.contracts to be True
class DEBUG(object):
	contracts = True

def requires(stmt):
	if DEBUG.contracts:
		assert stmt

def ensures(stmt):
	if DEBUG.contracts:
		assert stmt
