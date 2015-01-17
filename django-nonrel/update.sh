echo '**********************************'
echo '* AUTOLOAD                       *'
echo '**********************************'
hg clone https://bitbucket.org/twanschik/django-autoload
rm -rf autoload
mv django-autoload/autoload .
git add autoload && git commit -a -m "autoload" && git push
git status
git branch
echo '**********************************'
echo '* DJANGO                         *'
echo '**********************************'
cd django
git reset --hard origin/nonrel-1.6
git status
git branch
git pull
git remote show origin
cd ..
echo '**********************************'
echo '* DBINDEXER                      *'
echo '**********************************'
cd django-dbindexer
git reset --hard origin/master
git status
git branch
git pull
git remote show origin
cd ..
echo '**********************************'
echo '* DJANGOAPPENGINE                *'
echo '**********************************'
cd djangoappengine
git reset --hard origin/master
git status
git branch
git pull
git remote show origin
cd ..
echo '**********************************'
echo '* DJANGOTOOLBOX                  *'
echo '**********************************'
cd djangotoolbox
git reset --hard origin/master
git status
git branch
git pull
git remote show origin
cd ..
cd ..

echo '**********************************'
echo '* CMS PEGASUS                    *'
echo '**********************************'
git remote show origin
