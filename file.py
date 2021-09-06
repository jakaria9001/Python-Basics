import os

try:
    if __file__:
        filepath = os.path.abspath(__file__)
        req_path = os.path.dirname(os.path.dirname(filepath))
        print(req_path)
except OSError:
    print("Failed")