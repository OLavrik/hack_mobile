
export fileid=1xH1ASlSPGDDG6bzRiHdKwHTfA8TtBWGi
export filename=submission_catboost.zip
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ./${filename}

mkdir ./submissions
mkdir ./submissions/catboost
unzip ./submission_catboost.zip -d ./submissions/catboost

rm ./cookie