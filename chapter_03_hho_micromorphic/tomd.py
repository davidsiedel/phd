import re
from os import listdir
from os.path import isfile, join
from typing import List

def convert(file_path: str, new_lines: List[str]):
    with open(file_path, 'r') as file:
        c = file.readlines()
        for line in c:
            new_line = ""
            if "subsubsection{" in line:
                res = line.replace('{', '%').replace('}', '%').split('%')
                new_line += "#### {}\n".format(res[1])
            elif "subsection{" in line:
                res = line.replace('{', '%').replace('}', '%').split('%')
                new_line += "### {}\n".format(res[1])
            elif "section{" in line:
                res = line.replace('{', '%').replace('}', '%').split('%')
                new_line += "## {}\n".format(res[1])
            elif "%" in line:
                res = line.split('%')
                # new_line += "<!--- {} -->\n".format(res[1].splitlines()[0])
                new_line += ""
            elif "paragraph{" in line:
                res = line.replace('{', '%').replace('}', '%').split('%')
                new_line += "##### {}\n".format(res[1])
            else:
                new_line = line
            new_lines.append(new_line)

dir_path = "/home/dsiedel/Documents/2022_01_06_PAPER_01/paper_n/chapter_01_hho_mechanics/sections"
new_lines = []
files = [f for f in listdir(dir_path) if (isfile(join(dir_path, f)) and ".tex" in join(dir_path, f))]
files.sort()
for file_path in files:
    convert(join(dir_path, file_path), new_lines)
with open(dir_path + "/out.md", 'w') as out_file:
    for line in new_lines:
        out_file.write(line)