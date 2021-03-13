1. Goal: To obtain Uversky plot from multiple fasta sequences

2. Insall localcider in a separate python enviornment
(a)https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands 
(b)http://pappulab.github.io/localCIDER/
(c)install matplotlib, natsort (https://pypi.org/project/natsort/3.3.0/)

3. create a new folder with cider_analysis.py code and a subfolder containing all the fasta files

4. Activate the local python environment 

5. run the analysis script from the terminal using
python cider_analysis.py
note: may have to run pre_process.sh script before this to edit input files with white spaces

6. Output is a scatter plot of Uversky variables

7. Example input files in the folder
(a) RNAP contains processed input files
(b) ecoli contains unprocessed input files
output figure obtained with the scripts are RNAP_table1.png and ecoli_uversky.png
data files with other cider output variables are in cider_rnap.dat and cider_ecoli.dat   
