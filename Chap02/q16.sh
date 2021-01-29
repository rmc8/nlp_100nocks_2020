n=`wc -l ./popular-names.txt | awk '{print $1}'`
ln=`expr $n / $1`
split -l $ln ./popular-names.txt ./q16_