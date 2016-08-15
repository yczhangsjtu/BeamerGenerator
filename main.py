import json
from beamer import BeamerLoader

if __name__ == "__main__":
    with open("test.json") as f:
        text = f.read()
    data = json.loads(text)
    loader = BeamerLoader(data)
    beamer = loader.beamer

    print beamer.generate()
