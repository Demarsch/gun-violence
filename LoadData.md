# How to load the data from Kaggle

## First Time Install

1. Navigate to your repository folder in GitBash
   
2. Run `source activate YOUR_PYTHON_ENV`

3. Run `pip install kaggle`

4. Login to `kaggle.com`, go to `My Account` and click on `Create New API Token`

5. The download of `kaggle.json` file will start. Put the downloaded file into `C:\Windows\<Your username>\.kaggle` folder

6. Go back to GitBash and run `kaggle datasets download jameslko/gun-violence-data -p Data/Auto/ --unzip`


## Update/re-download

If you have already put your `kaggle.json` file into `.kaggle` folder, then navigate to your repository folder in GitBash and run `sh load_data.sh YOUR_PYTHON_ENV`