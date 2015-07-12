echo '**********************************'
echo '* AUTOLOAD                       *'
echo '**********************************'
cd /Users/arturo/interpegasus/gae_cms/django-nonrel
rm -rf autoload
hg clone https://bitbucket.org/twanschik/django-autoload
mv django-autoload/autoload .
rm -rf django-autoload
git add autoload && git commit -a -m "autoload"
git status
git branch
echo '**********************************'
echo '* DJANGO                         *'
echo '**********************************'
cd /Users/arturo/interpegasus/gae_cms/django-nonrel
rm -rf django
git clone https://github.com/django-nonrel/django.git
git status
git branch
git remote show origin
echo '**********************************'
echo '* DBINDEXER                      *'
echo '**********************************'
cd /Users/arturo/interpegasus/gae_cms/django-nonrel
rm -rf django-dbindexer
git clone https://github.com/django-nonrel/django-dbindexer.git
git status
git branch
git remote show origin
echo '**********************************'
echo '* DJANGOAPPENGINE                *'
echo '**********************************'
cd /Users/arturo/interpegasus/gae_cms/django-nonrel
rm -rf djangoappengine
git clone https://github.com/django-nonrel/djangoappengine.git --branch master
git status
git branch
git remote show origin
echo '**********************************'
echo '* DJANGOTOOLBOX                  *'
echo '**********************************'
cd /Users/arturo/interpegasus/gae_cms/django-nonrel
rm -rf djangotoolbox
git clone https://github.com/django-nonrel/djangotoolbox.git
git status
git branch
git remote show origin
cd /Users/arturo/interpegasus/gae_cms/
echo '**********************************'
echo '* CMS PEGASUS                    *'
echo '**********************************'
git remote show origin
find . -name "*.pyc" -exec rm -rf {} \;
