#! /usr/bin/env python
# Example of how to read the JME-JERC JSON files
# For more information, see the README in
# https://gitlab.cern.ch/cms-nanoAOD/jsonpog-integration/-/tree/master/POG/JME
# For a comparison to the CMSSW-syntax refer to
# https://github.com/cms-jet/JECDatabase/blob/master/scripts/JERC2JSON/minimalDemo.py

import correctionlib._core as core
jec,algo,algoAK8,lvl,unc=("Summer19UL16_V7_MC","AK4PFchs","AK8PFPuppi","L2Relative","Total")
pt,eta,rho,area=(100.,0.,15.,.5)
print("\JEC Parameters: ", jec, algo, algoAK8, lvl, unc,  pt, eta, rho, area)

print("\n\nSingle JEC level:\n===================")
#JSON (JEC,single)
cset = core.CorrectionSet.from_file("../POG/JME/2016postVFP_UL/jet_jerc.json.gz")
csetAK8 = core.CorrectionSet.from_file("../POG/JME/2016postVFP_UL/fatJet_jerc.json.gz")
print("JSON access to: {}_{}_{} and _{}".format(jec, lvl, algo, algoAK8))
sf=cset["{}_{}_{}".format(jec, lvl, algo)]
sfAK8=csetAK8["{}_{}_{}".format(jec, lvl, algoAK8)]
print([input.name for input in sf.inputs])
print("JSON result AK4: {}".format(sf.evaluate(eta,pt)))
print("JSON result AK8: {}".format(sfAK8.evaluate(eta,pt)))


print("\n\nCompound JEC:\n===================")
#JSON (JEC,compound)
compoundLevel="L1L2L3Res"
print("JSON access to: {}_{}_{} and _{}".format(jec,compoundLevel , algo, algoAK8))
sf=cset.compound["{}_{}_{}".format(jec, compoundLevel, algo)]
sfAK8=csetAK8.compound["{}_{}_{}".format(jec, compoundLevel, algoAK8)]
print([input.name for input in sf.inputs])
print("JSON result AK4: {}".format(sf.evaluate(area,eta,pt,rho)))
print("JSON result AK8: {}".format(sfAK8.evaluate(area,eta,pt,rho)))


print("\n\n JECSource:\n===========")
#JSON (JECSource)
print("JSON access to: {}_{}_{}".format(jec, unc, algo))
sf=cset["{}_{}_{}".format(jec, unc, algo)]
print([input.name for input in sf.inputs])
print("JSON result: {}".format(sf.evaluate(eta,pt)))


jer,algo,algoAK8,syst=("Summer20UL16_JRV3_MC","AK4PFchs","AK8PFchs","nom")
pt,eta,rho=(100.,0.,15.)
print("\n\n JER parameters: ", jer, algo, algoAK8, lvl, syst,  pt, eta)

print("\n\n JER SF:\n=========")
#JSON (JER scale factor)
print("JSON access to: {}_{}_{} and _{}".format(jer, "ScaleFactor", algo, algoAK8))
sf=cset["{}_ScaleFactor_{}".format(jer, algo)]
#sfAK8=csetAK8["{}_ScaleFactor_{}".format(jer, algoAK8)]
print([input.name for input in sf.inputs])
print("JSON result AK4: {}".format(sf.evaluate(eta,syst)))
#print("JSON result AK8: {}".format(sfAK8.evaluate(eta,syst))) #not included in current release


print("\n\n PtResolution:\n==============")
ResolutionChoice="PtResolution"
#JSON (JER scale factor)
print("JSON access to: {}_{}_{} and _{}".format(jer, ResolutionChoice, algo, algoAK8))
sf=cset["{}_{}_{}".format(jer, ResolutionChoice, algo)]
#sfAK8=csetAK8["{}_{}_{}".format(jer, ResolutionChoice, algoAK8)]
print([input.name for input in sf.inputs])
print("JSON result AK4: {}".format(sf.evaluate(eta,pt,rho)))
#print("JSON result AK8: {}".format(sfAK8.evaluate(eta,pt,rho))) #not included in current release


