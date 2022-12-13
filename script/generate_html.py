#!/usr/bin/env python

import os
import argparse
import pathlib as pl
import re
import pandas as pd
from rich.console import Console

from correctionlib.highlevel import model_auto, open_auto


template = """
<html>
<head>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery.fancytable/dist/fancyTable.min.js"></script>
    
    #TABLE#

    <script type="text/javascript">
        $(function() {
            $("#jsonTable").fancyTable({
                sortColumn: 0,
                pagination: true,
                exactMatch: "auto",
                perPage: 50
            });
        });
    </script>
</body>
</html>
"""


def get_year_from_era(era):
    """ Go from '2017'/'2018UL'/'2016ULpreVFP' to '17'/'18'/'16' """
    return re.search(r"20([0-9]+).*", era).group(1)


def get_run_from_era(era):
    year, camp = era.split("_")
    if int(get_year_from_era(year)) <= 18:
        return year, camp, "Run2"
    else:
        return year, camp, "Run3"


def generate_json_summary(inPath, outPath):
    with open(os.devnull, "w") as devnull:
        console = Console(width=100, file=devnull, record=True)
        cset = model_auto(open_auto(inPath))
        console.print(cset)
        console.save_html(outPath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="input jsonpog-integration POG folder")
    parser.add_argument("-o", "--output", required=True, help="output folder for html pages")
    args = parser.parse_args()

    outPath = pl.Path(args.output)
    outPath.mkdir(parents=True, exist_ok=True)

    rootPath = pl.Path(args.input)
    files = []
    
    for pogDir in rootPath.iterdir():
        if not pogDir.is_dir(): continue
        pog = pogDir.name
        
        for eraDir in pogDir.iterdir():
            if not eraDir.is_dir(): continue

            era = eraDir.name
            year, campaign, run = get_run_from_era(era)

            for fileH in eraDir.iterdir():
                if fileH.suffixes not in [[".json"], [".json", ".gz"]]: continue
                fileNm = fileH.name.split(".")[0]

                summary_path = outPath / f"{pog}_{era}_{fileNm}.html"
                print(f"Generating HTML summary for {fileH}")
                generate_json_summary(str(fileH), str(summary_path))

                files.append({
                    "POG": pog,
                    "Era": era,
                    "Year": year,
                    "Campaign": campaign,
                    "Run": run,
                    "File": f'<a href="{summary_path.name}">{fileNm}</a>'
                })

    print("Generating index page")

    files = pd.DataFrame(files)

    outIndex = outPath / "index.html"
    outIndex.write_text(
        template.replace("#TABLE#",
                         files.to_html(index=False, table_id="jsonTable", escape=False)
                        )
    )
