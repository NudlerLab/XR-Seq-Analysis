#This code takes in a SAM file and removes any reads that do not have a TT in the expected position for a 13-mer excision product
#Note, this code is used after the reads are split into plus and minus strands, if the file contains a minus strand, then it will first reverse complement the read.

import argparse

def main(infile,output,strand):
    file1=open(infile)
    outfile=open(output,'w')
    strand= strand
    for line in file1:
        if '@'in line:
            outfile.write(line)
        else:
            list_line=line.split()
            read=list_line[9]
            if strand=='m':
                read=reverse_comp(read)
            if read[7:9]=="TT":
                outfile.write(line)
            else:
                pass
    outfile.close()
    file1.close()

def reverse_comp(read):
    code={"A":"T","T":"A","G":"C","C":"G"}
    new=""
    for nuc in read:
        new=code[nuc]+new
    return new

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="input file")
    parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
    parser.add_argument("-s", "--strand", help="Indicate if reads are on plus (p) or minus (m) strand")
    args = parser.parse_args()
    main(args.infile,args.output,args.strand)
    

