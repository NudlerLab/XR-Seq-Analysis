import gzip 
import collections
import pandas as pd
from functools import reduce
def readgenome(fasta):
    genome=""
    with open(fasta,"r") as file1:
        for line in file1:
            if line.startswith(">"):
                pass
            else:
                genome=genome+''.join(line.rstrip())
   
   
    return genome
    


def TT_count(gene):
    count=0
    
    for i in range(len(gene)-1):
       
        if gene[i:i+2]=="TT":
            count=count+1
            
        i=i+2
    return count

def complement(gene):
    code={"A":"T","T":"A","G":"C","C":"G"}
    minus_strand=""
    for nuc in gene:
        minus_strand=minus_strand+code[nuc]
    return minus_strand

def plusTTcounts(file1):
    TS_dict={}
    plus_genome=readgenome("NC_000913.2.fasta")
    
    minus_genome=complement(plus_genome)
    bedfile=open(file1,"r")
    index=0
    for line in bedfile:
        newLine=line.split("\t")
        start=int(newLine[1])
        end=int(newLine[2])
        strand=newLine[5].rstrip("\n")
        
        
        if strand=="+":
            TT= TT_count(minus_genome[start:end])
            #if TT>30:
            TS_dict[index]=TT
        if strand=="-":
            TT= TT_count(plus_genome[start:end])
            #if TT>30:
            TS_dict[index]=TT
        index=index+1
    od = collections.OrderedDict(sorted(TS_dict.items()))
    return od

def minusTTcounts(file1):
    NTS_dict={}
    plus_genome=readgenome("NC_000913.2.fasta")
    
    minus_genome=complement(plus_genome)
    bedfile=open(file1,"r")
    index=0
    for line in bedfile:
        newLine=line.split("\t")
        start=int(newLine[1])
        end=int(newLine[2])
        strand=newLine[5].rstrip("\n")
        
        
        if strand=="+":
            TT= TT_count(plus_genome[start:end])
            NTS_dict[index]=TT
        if strand=="-":
            TT= TT_count(minus_genome[start:end])
            NTS_dict[index]=TT
        index=index+1
    od = collections.OrderedDict(sorted(NTS_dict.items()))
    
    return od
            


TS_TTcount= plusTTcounts("primary_upstreamsense_TSS_2")
TS_df=pd.DataFrame.from_dict(TS_TTcount,orient='index')

TS_df.columns=["TS"]

NTS_TTcount=minusTTcounts("primary_upstreamsense_TSS_2")
NTS_df=pd.DataFrame.from_dict(NTS_TTcount,orient='index')
NTS_df.columns=["NTS"]
df_lis=[TS_df,NTS_df]
final_df=reduce(lambda left,right:pd.merge(left,right,how='left',left_index=True,right_index=True),df_lis) 
#print(TS_df)           
final_df.to_csv("TTcount.txt", sep='\t')    

        


#index genome start in bedfile, end in bedfile
#make a function that counts T dinucleotides
