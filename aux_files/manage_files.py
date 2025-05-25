import json
import os

# method to open the file with the test cases
def get_test_cases(fileName):
    # path for ../data/fileName.json
    test_cases_path = os.path.join(os.path.dirname(__file__),'..','data', fileName)
    # open the file
    with open(test_cases_path) as f:
        test_cases = json.load(f)
    return test_cases