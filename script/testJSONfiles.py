print()
print("################################")
print("Starting testJSONfiles.py")
print("I will check all .json files in this folder")
print()

from correctionlib.schemav1 import CorrectionSet
from pydantic import ValidationError

def testJSONfile( fileName ):
    print()
    print(f"{fileName} -> test started")
    try:
        obj = CorrectionSet.parse_file(fileName)
    except ValidationError:
        # Possibly print error text
        print(f"{fileName} -> test failed")
        return False
    print(f"{fileName} -> test passed")
    return True

import glob, os
onlyfiles = glob.glob("POG/*/*.json")
failedTests = []
for fileName in onlyfiles:
    if os.stat(fileName).st_size == 0:
        print("Skipping empty file %s"%fileName)
        continue
    isFailed = not testJSONfile(fileName)
    if isFailed: failedTests.append(fileName)

if isFailed: 
    raise Exception("testJSONfiles.py is failed for the following files:" + str(failedTests))

print()
print("testJSONfiles.py is DONE without errors.")
print("################################")
print()
