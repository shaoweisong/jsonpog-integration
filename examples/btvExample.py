## Example showing how to read the BTV scale factors
from correctionlib import _core

evaluator = _core.CorrectionSet.from_file('./../POG/BTV/2017_UL/btagging.json.gz')

# Reading deepCSV working point and reshaping

# Working point: evaluate('systematic', 'method', 'working_point', 'flavor', 'abseta', 'pt')
# method = "comb"/"mujets"/"incl"
# working_point = "T"/"M"/"L"
# flavor = 5, 4, 0 (== b, c, light jet hadron flavor)
valsf_deepCSV_wp = evaluator["deepCSV_wp"].evaluate("central", "comb", "M", 4, 0., 30.)
print("deepCSV working point scale factor is: "+str(valsf_deepCSV_wp))

# Reshaping: evaluate('systematic', 'flavor', 'abseta', 'pt', 'discriminator')
# flavor = 5, 4, 0 (== b, c, light jet hadron flavor)
valsf_deepCSV_shape = evaluator["deepCSV_shape"].evaluate("central", 5, 0., 20., 0.8)
print("deepCSV reshaping scale factor is: "+str(valsf_deepCSV_shape))

# Reading deepJet working point and reshaping

valsf_deepJet_wp = evaluator["deepJet_wp"].evaluate("central", "incl", "T", 0, 0., 30.)
print("deepJet working point scale factor is:  "+str(valsf_deepJet_wp))

valsf_deepJet_shape = evaluator["deepJet_shape"].evaluate("central", 5, 0., 20., 0.8)
print("deepJet reshaping scale factor is: "+str(valsf_deepJet_shape))


# Sanity check of the UL 18 version

evaluator = _core.CorrectionSet.from_file('./../POG/BTV/2018_UL/btagging.json.gz')

valsf_deepCSV_wp = evaluator["deepCSV_wp"].evaluate("central", "comb", "M", 4, 0., 30.)
print("deepCSV working point scale factor in UL 18 is: "+str(valsf_deepCSV_wp))

valsf_deepCSV_shape = evaluator["deepCSV_shape"].evaluate("central", 5, 0., 20., 0.8)
print("deepCSV reshaping scale factor in UL 18 is: "+str(valsf_deepCSV_shape))

valsf_deepJet_wp = evaluator["deepJet_wp"].evaluate("central", "incl", "T", 0, 0., 30.)
print("deepJet working point scale factor in UL 18 is:  "+str(valsf_deepJet_wp))

valsf_deepJet_shape = evaluator["deepJet_shape"].evaluate("central", 5, 0., 20., 0.8)
print("deepJet reshaping scale factor in UL 18 is: "+str(valsf_deepJet_shape))
