from pathlib import Path

cwdDir = Path(__file__).parent

files = cwdDir.glob('*.html')

documents = {file.name:file for file in files}

def load(name:str) -> Path:
    return documents[name]