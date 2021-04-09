## example how to read the photon format v2
from correctionlib import _core

evaluator = _core.CorrectionSet.from_string(cset.json(exclude_unset=True, indent=4))
valsf= evaluator["UL-Photon-CSEV-SF"].evaluate("2016postVFP","sf","Loose","EBInc")
print("sf is:"+str(valsf))
