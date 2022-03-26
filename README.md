![banner-readme](img/laliga_banner.png)

A Python Data Analyst Code-Louisville Project.

##### Version 1.0

## Summary

The Spain Soccer League, is a Python Data Analyst CodeLouisville project, where
you can find some data and analysis of the Spain soccer league and Real Madrd soccer team as well. You can also find unit converter and string operation mudules. This project will be part of our go-to tool to show off to potential employers and demonstrate we know what we’re talking about.

## Packages & Modules
Spain League uses system, unittest, pyodbc, pandas, csv, operator, numpy and matplotlib.

## Setup Instructions
  - Most recent version of Google Chrome
  - Python 3.10.2 (older 3.3+ versions may work, but no promises). Download and install it from `https://www.python.org/downloads/`
  - Copy to C:\Users\ `Window-User`\AppData\Local\Programs\Python\Python310 the file from project `data/pyodbc-4.0.32-cp310-cp310-win_amd64.whl` (replace `Window-User` by the current one on Windows)
  - Edit `requirements.txt` file and replace `Window-User` in this line: pyodbc @ file:///C:/Users/`Window-User`/AppData/Local/Programs/Python/Python310/pyodbc-4.0.32-cp310-cp310-win_amd64.whl`
  - Run `pip install -r requirements.txt`
  
## Run the application
- `Download` the repo to your PC, or using the Terminal run `git clone https://github.com/mtoirac2011/SpainLeague.git` to clone the repository instead.
- On Terminal:
    - Go to the `SpainLeague-main` folder as extracted.
    - Run `Python setup.py` to execute the application.
    - Run `Jupyter notebook` to open and execute the notebook files `data/Laliga.ipynb` and `data/real_madrid.ipynb` 

## The Spain Soccer League pretents to give you a brief view about the soccer spain league, and this project is made up of the following pages:

* ###   Welcome screen 
* ###   Main menu
* ###   La Liga Menu 
* ###   Real Madrid Menu
* ###   Converter Menu 
* ###   Utilities Menu 

### Welcome screen
> It welcomes the site and describes what the app will bring for us. 

### Main menu
> Shows the diffrent menues that the application has to be used.

### La Liga Menu
> Reports some kind of information about 2018 La liga soccer in Spain (Uses `2018Laliga.csv` file ). It also does some analyst in jupyter notebooks.

### Real Madrid Menu
> Reports some kind of information about Real Madrid soccer team (Uses `real_madrid_fc.csv` file ).  Do some analyst in jupyter notebooks as well.

### Converter Menu 
> Converts an user input number to a several units.

### Utilities menu
> Reads data from SQL Server and create a dictionary with data from a table (Uses `laligadb.bak`: a ([SQL Backup Database.py](https://github.com/mtoirac2011/SpainLeague/tree/main/data))). Also it shows operations over string using the `Name of the players` field.

### Code Louisville Requirements

1. **Category 1: Python Programming Basics**:
    - [x] Implement a “master loop” console application. 
        ([setup.py](setup.py))
    - [x] Create and call at least 3 functions or methods. 
        ([realmadrid.py](realmadrid.py)) ([ligatools.py](ligatools.py)) ([utilities.py](utilities.py)) ([laliga.py](laliga.py))
    - [x] Implement a regular expression.
        ([ligatools.py](ligatools.py)) specific on `if_integer` function.
    - [x] Build a conversion tool that converts user input to another type and displays it ([ligatools.py](ligatools.py)) specific on `farToCelcious` `milesToKm` `feetToMeter` and `meterToCm`functions.
    - [x] Create a dictionary or list, populate it with several values
        ([utilities.py](utilities.py)) specific on `loadTable` function.
    - [x] Analyze text and display information about it (ex: how many words in a paragraph).
        ([utilities.py](utilities.py))
    - [ ] *( Not yet)*     
        - Create a class and create at least one object of that class and populate it.
        - Calculate and display data based on an external factor (ex: get the   current date, and display how many days remain until some event).
         

2. **Category 2: Utilize External Data**:
    - [x] Read data from an external file, such as text, JSON, CSV, etc
        ([realmadrid.py](realmadrid.py)) ([laliga.py](laliga.py))
    - [x] Connect to a database and read data using SQL. 
        ([utilities.py](utilities.py))
    - [ ] *(Not yet)*
        - Connect to an external/3rd party API and read data into your app
        
3. **Category 3: Data Display**:
    - [x] Visualize data in a graph, chart, or other visual representation of data.
        ([Laliga notebook]([utilities.py](https://github.com/mtoirac2011/SpainLeague/blob/main/data/Laliga.ipynb)))
    - [x] Display data in tabular form.
        ([RealMadrid notebook]([utilities.py]https://github.com/mtoirac2011/SpainLeague/blob/main/data/real_madrid.ipynb))

4. **Category 4: Best Practices**:
    - [x] Implement a log that records errors, invalid inputs.
        ([ligatools.py](ligatools.py)) specific on `checklogfile` and `printlogfile` functions.
    - [x] Create 3 or more unit tests for your application.
        ([test_ligatools.py](test_ligatools.py))
    - [ ] *(Not yet)*
        - The program should utilize a virtual environment and document library
        dependencies in a requirements.txt file.