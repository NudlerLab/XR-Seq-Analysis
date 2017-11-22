import argparse
import gzip
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="input file")
parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
args = parser.parse_args()

outfile=open(args.output, 'w')
with gzip.open(args.infile, 'rt') as file1:
    for line in file1:
        
        if '@' in line:
            pass
        else:
            if 'GGCTCAGTTCGTATGAGTGCCG' in line:
                line=line.strip()
                #print(line)
                start=line.find('GGCTCAGTTCGTATGAGTGCCG')
                end=start+len('GGCTCAGTTCGTATGAGTGCCG')
                iden=line[end:end+8]
                outfile.write('@'+iden+'\n')
                outfile.write(line+'\n')
                one=file1.readline()
                two=file1.readline()
                outfile.write(one)
                outfile.write(two)

        


file1.close()
outfile.close()
