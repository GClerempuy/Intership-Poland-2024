head -n 1 quast_results/AMAD/transposed_report.tsv | sed 's/#//g' > tmp/Merged_data_tmp.tsv
tail -n +2 quast_results/*/transposed_report.tsv >> tmp/Merged_data_tmp.tsv
grep -v "^==" tmp/Merged_data_tmp.tsv > tmp/Merged_data_tmp2.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($1, 1, 4), $0}' tmp/Merged_data_tmp2.tsv > tmp/Merged_data_tmp3.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($2, 5, 1), $0}' tmp/Merged_data_tmp3.tsv > tmp/Merged_data_tmp4.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($3, 7, 1), $0}' tmp/Merged_data_tmp4.tsv > tmp/Merged_data_tmp5.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } NR==1 { $1="Fraction_Size"; $2="Depth"; $3="Lakes_names" } { print }' tmp/Merged_data_tmp5.tsv > Merged_data.tsv
rm tmp/Merged_data_tmp.tsv
rm tmp/Merged_data_tmp2.tsv
rm tmp/Merged_data_tmp3.tsv
rm tmp/Merged_data_tmp4.tsv
rm tmp/Merged_data_tmp5.tsv



head -n 1 /home/clerempuy/Dowload/ZURI/transposed_report.tsv | sed 's/#//g' > tmp/Merged_data_tmp.tsv
tail -n +2 /home/clerempuy/Dowload/*/transposed_report.tsv >> tmp/Merged_data_tmp.tsv
grep -v "^==" tmp/Merged_data_tmp.tsv > tmp/Merged_data_tmp2.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($1, 1, 4), $0}' tmp/Merged_data_tmp2.tsv > tmp/Merged_data_tmp3.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($2, 5, 1), $0}' tmp/Merged_data_tmp3.tsv > tmp/Merged_data_tmp4.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } {print substr($3, 7, 1), $0}' tmp/Merged_data_tmp4.tsv > tmp/Merged_data_tmp5.tsv
awk 'BEGIN { FS="\t"; OFS="\t" } NR==1 { $1="Fraction_Size"; $2="Depth"; $3="Lakes_names" } { print }' tmp/Merged_data_tmp5.tsv > Merged_data.tsv
rm tmp/Merged_data_tmp.tsv
rm tmp/Merged_data_tmp2.tsv
rm tmp/Merged_data_tmp3.tsv
rm tmp/Merged_data_tmp4.tsv
rm tmp/Merged_data_tmp5.tsv