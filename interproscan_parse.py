import os
import re
import csv
import argparse
import glob
from pathlib import Path

#Parse commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--proteins', help='path to a fasta file containing protein sequences, (default = "proteins.fasta" file in script directory)')
parser.add_argument('-i', '--interproscan', help='path to an interproscan.out file (default = "interproscan.tsv" file in script directory)')
parser.add_argument('-o', '--output', help='path and name of output file (default = searchterm.fasta)')
parser.add_argument('-s', '--searchterm', help='a string of what you are looking for (default = amylase)')
parser.add_argument('-d', '--database', help='limit hits to certain database (pfam, tmhmm, panther, prosite, mobidb, signalp, prints, prodom)')
args = parser.parse_args()

if args.interproscan:
    interproscan_file = Path(args.interproscan)
else:
    interproscan_file_name = '*interproscan.tsv'
    interproscan_file_path = os.path.join(os.getcwd(), interproscan_file_name)
    for element in glob.glob(interproscan_file_path):
        interproscan_file = Path(element)

if args.proteins:
    proteins_file = Path(args.proteins)
else:
    proteins_file_name = '*proteins.fasta'
    proteins_file_path = os.path.join(os.getcwd(), proteins_file_name)
    for element in glob.glob(proteins_file_path):
        proteins_file = Path(element)

if args.searchterm:
    searchterm = args.searchterm
else:
    searchterm = 'amylase'

if args.output:
    output_file = Path(args.output)
elif args.searchterm:
    output_file_name = searchterm+'.fasta'
    output_file = Path(os.path.join(os.getcwd(), output_file_name))
else:
    output_file = Path(os.path.join(os.getcwd(),'amylase.fasta'))

if args.database:
    print('Limiting output to', args.database, 'hits')
    database = args.database.lower()

proteins = {}
interproscan = {}
output = {}

#If file with same outputname exists, delete it first
if os.path.isfile(output_file):
    os.unlink(output_file)

print("Parsing protein file")
with open(proteins_file) as file:
    input = file.read().splitlines()
    for line in input:
        if not line.strip(): continue
        if line[0] == '>':
            name = line[1:]
            proteins[name] = ''
        else:
            proteins[name] += line
print("Finished parsing protein file")

print("Parsing interproscan file")
with open(interproscan_file) as file:
    input = csv.reader(file, delimiter='\t')
    for line in input:
        proteinID = line[0]
        lineString = str(line)
        lineString = lineString.lower()
        if args.database:
            if searchterm in lineString and database in lineString:
                output[proteinID] = proteins[proteinID]
                interproscan[proteinID] = line
        else:
            if searchterm in lineString:
                output[proteinID] = proteins[proteinID]
                interproscan[proteinID] = line
print("Finished parsing protein file")
print('================================================================')
print('looking for interproscan hits to:', searchterm)
print('================================================================')
print('found',len(output),'hits:')  
print('')

for key, value in output.items():
    if interproscan[key][3] == 'PANTHER':
        print(key, interproscan[key][3],':', interproscan[key][12])
    else:
        print(key, interproscan[key][3],':', interproscan[key][5])

    print('>'+key, '\n'+value, file=open(output_file,'a'))