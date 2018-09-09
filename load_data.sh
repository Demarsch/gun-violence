if [[ $# -eq 0 ]] ; then
    echo 'You need to pass in a string name for your virtual environment'
    exit 1
fi
echo "Activating virtual environment..."
source activate $1
echo "Installing/upgrading Kaggle package"
pip install kaggle
echo "Downloading Kaggle dataset"
kaggle datasets download jameslko/gun-violence-data -p Data/Auto/ --unzip