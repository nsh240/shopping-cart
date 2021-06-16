
# shopping cart project
This repo contains a program for ringing up groceries by typing in individual product IDs which are stored in a CSV file located at data/products.csv.  This CSV file can be updated with the latest products.

## Installation
Clone or download this repo onto your local computer.
Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):
```sh
cd shopping-cart
```
## Setup
Setup a virtual environment to ensure your packages are installed
```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```
Install the required packages:
```sh
pip install -r requirements.txt
```
Add a products.csv file with your products:
```sh
Add a file of products named "products.csv" to the data folder with your products.  The format should match the existing "ddfaults_products.csv" file currently in the data folder.  Make sure you save your file with the name "products.csv"
```
### Configuring Environment Variables
You can configure the local tax rate in a .env file by updating the value of the tax_rate field, as shown below
```
TAX_RATE=<your tax rate here as a decimal>
```

## Usage
To start up the shopping-cart:
```sh
python shopping_cart.py
```