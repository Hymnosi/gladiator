import toml

def init(file):
    cfg = toml.load(file)
    print("Configuration Loaded")
    return cfg