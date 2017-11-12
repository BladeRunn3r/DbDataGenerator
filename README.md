# DbDataGenerator
Used data/tools:

  --> [PyFaker](https://github.com/hayd/pyfaker) for generating users and their location (matching randomed nationality) - needed to run code
  
  --> cars csv file exported from Oracle using data from [this](https://github.com/n8barr/automotive-model-year-data) database
  
  --> companies csv file downloaded from [Nasdaq](http://www.nasdaq.com/screening/company-list.aspx) website
  
  It is suggested to run files using PowerShell on Windows as it is tested to print output properly.
  Problems with UTF-8 encoding can be solved with pasting "chcp 65001" to force it in PowerShell.
  Reportedly problem exists only up to Python 3.5.
