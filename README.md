# interproscan_parse
A Python3 script that parses interproscan.tsv output for keywords and creates a fasta file with hits. <br>
You need to provide a proteome file in fasta format and the interproscan output file in tsv format, which was created by running interproscan over the same proteome file (to make sure the protein IDs are the same).

# Usage

usage: 
```
interproscan_parse.py [-h] [-p PROTEINS] [-i INTEROROSCAN] [-o OUTPUT] [-s SEARCHTERM] [-d DATABASE]
```

## Examples
### Example 1 - default parameters
Expects `proteins.fasta` and `interproscan.tsv` to be in the same directory as `interproscan_parse.py`.
```
interproscan_parse.py
```
This will parse your `interproscan.tsv` file for the string 'amylase' and output a file called `amylase.fasta` containing protein sequences of hits to all databases used when running interproscan.

### Example 2 - advanced parameters
```
interproscan_parse.py -p /path/to/proteins.fasta -i /path/to/interproscan.tsv -o /path/to/output.fasta -s 'alpha amylase' -d pfam
```
This will parse your `interproscan.tsv` file for the string 'alpha amylase' and output a file called `alpha amylase.fasta` containing protein sequences of hits to the `Pfam` database.

## Optional arguments:
```
-h, --help 
show this help message and exit

-p PROTEINS, --proteins PROTEINS
path to a fasta file containing protein sequences, (default = "proteins.fasta" file in script directory)

-i INTERPROSCAN, --interproscan INTERPROSCAN
path to an interproscan.out file (default = "interproscan.tsv" file in script directory)

-o OUTPUT, --output OUTPUT
path and name of output file (default = searchterm.fasta)

-s SEARCHTERM, --searchterm SEARCHTERM
a string of what you are looking for (default = amylase)

-d DATABASE, --database DATABASE
limit hits to certain database (pfam, tmhmm, panther, prosite, mobidb, signalp, prints, prodom)

-n, --nooutputfile
prevents the creation of an output file and only prints results to the terminal
```

