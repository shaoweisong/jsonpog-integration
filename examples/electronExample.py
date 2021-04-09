## example how to read the electron format v2
from correctionlib import _core

evaluator = _core.CorrectionSet.from_string(cset.json(exclude_unset=True, indent=4))
valsf= evaluator["UL-Electron-ID-SF"].evaluate("2017","sf","Medium",1.1, 34.0)
print("sf is:"+str(valsf))
