#pip install -r req.txt
pip freeze > req.txt
#git clone -o penguinl https://github.com/Kovalsky95/penguinl.git
#git config --global user.email "diana1997525@gmail.com"
#git config --global user.name "Kovalsky95"
#git config --global credential.helper cache
git config --global credential.helper "cache --timeout=25200"
#git config credential.helper store
#git config --unset credential.helper
git pull --all
git add .
git commit -m PenguinL
git push --set-upstream penguinl master
