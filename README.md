# XR-Seq-Analysis

Python codes to analyze XR-seq Data

`remove_duplicates.py` -> removes PCR duplicates from reads after alignment (using sam file)

edit_header.py -> Adds the random 8mer barcode to the header of the fastq (not trimmed) file so that it this barcode ends up in the sam file

filter_TT.py -> filters out any reads that do not have a TT in the 8 and 9th position of the 13 mer read (using sam file)

TT_content.py -> Calculates the number of TT's in a gene and returns a text file with this count

XR-seq_Analysis_Processed_Files.ipynb -> Shows data normalization and how to create histograms and correlation plots with XR-seq data 
