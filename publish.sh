echo 'set pip python version'

source ~/.bash_profile

echo 'remove dist'

rm -rf dist/*

echo 'build frontend'

cd streamlit_l7/frontend

yarn run build  # build frontend

echo 'build python'

cd ../..

python setup.py sdist bdist_wheel

echo 'upload to pypi'

python -m twine upload  dist/*

echo 'upload to pypi success'

echo 'update local version'
pip install --upgrade streamlit-l7


