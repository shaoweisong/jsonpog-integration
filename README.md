# jsonPOG-integration


**POG folder**

Each object have a json, and each POG has a folder for storage

| directory  | name.json |
| -------- | ----------|
| POG/EGM  | photon.json |
|          | electron.json |
| POG/TAU  | tau.json |
| POG/MUON | muon.json |
| POG/JME  | fatJetPuppi.json |
|          | jetCHS.json |
| POG/BTV  | bjets.json |
|          | cjets.json |

Initial notes: 
1. we have one json for Run2, one for Run3
2. we have one json for all the data taking years go together i.e. 2016/2017/2018 and sililarly the prompt, re-reco, UL go on the same file.
3. the label identifier should be unique: i.e. 2016postVFP_UL


**Repository with templates and tools**

for the time being things are here
https://github.com/nsmith-/correctionlib


**Script folder**

The tests will happen with the script defined here
Goal of the test:
* verify can be loadeded
* verify that is compliant to the format "Schema Version" 


**Distribution to users**

Once a PR is made, a test is being started and once the PR is merged a copy is saved in *cvms* for distribution.





