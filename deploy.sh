# secret_key do django
useradd -m easyfly
usermod --shell /bin/bash
sudo su - easyfly
mkdir django_project
cd django_project

# RSYNC #-n para dry-run
rsync -ruzz --exclude-from=.gitignore  --progress . easyfly:/home/easyfly/django_project/

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r server/requirements.txt

cat /dev/urandom | tr -dc 'a-zA-Z0-9#%&()*' | fold -w 50 | head -n 1 > server/secret_key.txt
chmod -w server/secret_key.txt
chmod go-r server/secret_key.txt
chmod +x server/manage.py

# Build Semantic ui
npx gulp build
