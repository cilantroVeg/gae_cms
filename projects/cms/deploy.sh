if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 0
fi
cd ~/interpegasus/gae_cms/projects/cms/static/foundation/
mkdir ~/Downloads/foundation_static_files
mv * ~/Downloads/foundation_static_files
mv ~/Downloads/foundation_static_files/$1 .
cd ~/interpegasus/gae_cms
find . -name "*.pyc" -exec rm -rf {} \;
cd ~/interpegasus/gae_cms/projects/cms
python manage.py deploy
mv ~/Downloads/foundation_static_files/* ~/interpegasus/gae_cms/projects/cms/static/foundation/