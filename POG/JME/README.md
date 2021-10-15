# JetMET POG-recommonded corrections

This repository contains the scale factors (SFs) for heavy object tagging, PUJetID and Quark-Gluon tagging and jet energy corrections recommended by the JetMET POG.
More detailed recommendations can be found on this TWiki page: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetMET#Quick_links_to_current_recommend

The .json files are splitted in YEAR_jmar.json for tagging SFs and XXX for jet energy corrections.

The SFs are meant for the following campaigns:

| Year folder   | MC campaign              | Data campaign           |
|:------------:|:------------------------:| :----------------------:|
| `2016_EOY` | `RunIISummer16MiniAODv3` | `17Jul2018`             |
| `2017_EOY` | `RunIIFall17MiniAODv2`   | `31Mar2018`             |
| `2018_EOY` | `RunIIAutumn18MiniAOD`   | `17Sep2018`/`22Jan2019` |

## Usage

Please install the [`correctionlib`](https://github.com/cms-nanoAOD/correctionlib) tool to read these SFs.
Find out the content of the `jmar.json` using
```
gunzip POG/JME/2017_EOY/2017_jmar.json.gz
correction summary POG/JME/2017_EOY/jmar.json
```
Example:

📈 DeepAK8_W_Nominal (v1)                                                                       
│   Scale factor for DeepAK8 algorithm (nominal and mass decorrelated) for particle W               
│   Node counts: Category: 4, Binning: 24                                                           
│   ╭──────────────────────────── ▶ input ─────────────────────────────╮                            
│   │ eta (real)                                                       │                            
│   │ eta of the jet                                                   │                            
│   │ Range: [-2.4, 2.4)                                               │                            
│   ╰──────────────────────────────────────────────────────────────────╯                            
│   ╭──────────────────────────── ▶ input ─────────────────────────────╮                            
│   │ pt (real)                                                        │                            
│   │ pT of the jet                                                    │                            
│   │ Range: [200.0, 800.0), overflow ok                               │                            
│   ╰──────────────────────────────────────────────────────────────────╯                            
│   ╭──────────────────────────── ▶ input ─────────────────────────────╮                            
│   │ systematic (string)                                              │                            
│   │ systematics: nom, up, down                                       │                            
│   │ Values: down, nom, up                                            │                            
│   ╰──────────────────────────────────────────────────────────────────╯                            
│   ╭──────────────────────────── ▶ input ─────────────────────────────╮                            
│   │ workingpoint (string)                                            │                            
│   │ Working point of the tagger you use (QCD misidentification rate) │                            
│   │ Values: 0p5, 1p0, 2p5, 5p0                                       │                            
│   ╰──────────────────────────────────────────────────────────────────╯                            
│   ╭─── ◀ output ───╮                                                                              
│   │ weight (real)  │                                                                              
│   │ No description │                                                                              
│   ╰────────────────╯                                               

An example how to evaluate is given in [`examples/jmarExample.py`](../../examples/jmarExample.py).
You can load the set of corrections as follows in python as
```
from correctionlib import _core

evaluator = _core.CorrectionSet.from_file('2017_jmar.json')

valsf= evaluator["DeepAK8_Top_Nominal"].evaluate(eta, pt, syst, wp)


Where `syst='nom'`, `'up'` or  `'down'`.
All maps available and the corresponding input parameters can be seen by using the 'correction summary' option mentioned before.

## References

The JMAR POG JSON files are created from https://github.com/cms-jet/JSON_Format