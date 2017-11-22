import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="input file")
parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
args = parser.parse_args()

seq_lis=[]
file1=open(args.infile)
outfile=open(args.output,'w')

first_read=False
for line in file1:
    if '@' in line:
        outfile.write(line)
    elif first_read==False:
        first_read=True
        parent_line=line
        #print(parent_line.split()[9])
        seq_lis.append(parent_line.split()[0])
    else:
        next_line=line
        key1=parent_line.split()[9]
        key2=next_line.split()[9]
        if key1==key2:
            seq_lis.append(next_line.split()[0])
            
        else:
            seq_set=set(seq_lis)
            print(seq_set)
            for i in range(len(seq_set)):
                outfile.write(parent_line)
                
            #first_read=False
            seq_lis=[]
            parent_line=next_line
            seq_lis.append(next_line.split()[0])
            #outfile.write(next_line)
outfile.close()
file1.close()