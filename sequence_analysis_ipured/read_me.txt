Goal: Run the iupred analysis over all protein sequences located in the same folder
1. create an empty folder test
2. create two subfolders inside test, one with all the fasta sequence and another named “ipured”
3. cd to the folder containing fasta files (e.g. RNAP) and type the follwing command
for file in *; do /home/pinaki/iupred2a/iupred2a.py $file long > ../iupred/${file}_iupred.dat; done
note: change the directory name where iupred is installed in your computer after "do" in the above line 
4. cd .. to come back to the test folder
4. Get the average disorder of a protein by running the shell script
 ./avg_disorder.sh > iupred_summary.dat
