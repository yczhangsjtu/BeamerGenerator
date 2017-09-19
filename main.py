#!/usr/bin/python

import json
import sys

sys.path.append('/Users/yuncong/Projects/BeamerGenerator')

from beamer import BeamerLoader

if __name__ == "__main__":
	filename = "test.json"
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	with open(filename) as f:
			text = f.read()
	data = json.loads(text)
	loader = BeamerLoader(data)
	beamer = loader.beamer

	print beamer.generate()
