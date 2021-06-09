# shopping-cart

## 1. Set up python environment using conda create, such as:
  
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt # (after specifying desired packages inside)



# shopping cart project
This repo contains a program for ringing up groceries by typing in individual product IDs which are stored in a variable.

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
### Configuring Environment Variables
You can configure the local tax rate in the .env file by updating the value of the tax_rate field, as shown below
```
TAX_RATE=<your tax rate here as a decimal>
```
## Usage
To start up the shopping-cart:
```sh
python shopping_cart.py
```