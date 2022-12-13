#!/usr/bin/env python

import os
import argparse
import pathlib as pl
import re
import pandas as pd

header = """
<html>
<head><title>POG SFs</title></head>
<body>
#BODY#
</body>
</html>
"""

def get_year_from_era(era):
    """ Go from '2017'/'2018UL'/'2016ULpreVFP' to '17'/'18'/'16' """
    return re.search(r"20([0-9]+).*", era).group(1)

def get_group_from_era(era):
    year, camp = era.split("_")
    if int(get_year_from_era(year)) < 20:
        if camp == "UL":
            return 1, year, camp, "Run2 UL"
        else:
            return 0, year, camp, "Run2 pre-UL"
    else:
        return 2, year, camp, "Run3"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="input jsonpog-integration POG folder")
    parser.add_argument("-o", "--output", required=True, help="output folder")
    args = parser.parse_args()

    rootPath = pl.Path(args.input)
    files = []
    
    for pogDir in rootPath.iterdir():
        if not pogDir.is_dir(): continue
        pog = pogDir.name
        
        for eraDir in pogDir.iterdir():
            if not eraDir.is_dir(): continue

            era = eraDir.name
            order, year, campaign, group = get_group_from_era(era)

            for fileH in eraDir.iterdir():
                if fileH.suffixes not in [[".json"], [".json", ".gz"]]: continue
                files.append({
                    "pog": pog,
                    "era": era,
                    "year": year,
                    "campaign": campaign,
                    "group": group,
                    "group_order": order,
                    "path": str(fileH),
                    "file": fileH.name.split(".")[0]
                })

    files = pd.DataFrame(files)


    breakpoint()
