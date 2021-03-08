#!/bin/bash
for file in iupred/*;
do
printf "$file "
count=0;
total=0; 
grep -o '^[^#]*' $file > temp
for i in $( awk '{ print $3; }' temp )
   do 
     total=$(echo $total+$i | bc )
     ((count++))
   done
echo "scale=3; $total / $count" | bc;
done

