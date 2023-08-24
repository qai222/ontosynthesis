cd owx_dump

for i in *.ttl
do
  mv $i ${i%????}.owx
done

declare -a old_import_paths=(
   "<Import>http://purl.allotrope.org/voc/afo/REC/2023/06/aft</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/REC/2023/06/relation</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/perspective/REC/2023/06/molecular-scale</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/perspective/REC/2023/06/organization</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/perspective/REC/2023/06/portion-of-material</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/perspective/REC/2023/06/system</Import>"
   "<Import>http://purl.allotrope.org/voc/afo/REC/2023/06/curation</Import>"
   "<Import>http://purl.allotrope.org/voc/bfo/REC/2018/04/bfo-2-0</Import>"
   "<Import>http://purl.allotrope.org/voc/skos/REC/2018/10/skos</Import>"
)
declare -a new_import_paths=(
   "<Import>file://$PWD/aft.owx</Import>"
   "<Import>file://$PWD/relation.owx</Import>"
   "<Import>file://$PWD/molecular-scale.owx</Import>"
   "<Import>file://$PWD/organization.owx</Import>"
   "<Import>file://$PWD/portion-of-material.owx</Import>"
   "<Import>file://$PWD/system.owx</Import>"
   "<Import>file://$PWD/curation.owx</Import>"
   "<Import>file://$PWD/bfo-2-0.owx</Import>"
   "<Import>file://$PWD/skos.owx</Import>"
)

sed -i "s#mailto:#mailto://#" *.owx

path_length=${#old_import_paths[@]}
let path_length--
echo "$path_length"
for idx in $(seq 0 1 ${path_length})
do
  sed -i "s#${old_import_paths[$idx]}#${new_import_paths[$idx]}#" *.owx
done

cd ../