# AppScanLangs

AppScanLangs is a Python program that scrapes the supported list of languages supported by HCL AppScan Source and HCL AppScan on Cloud (application static analysis tools), from the online product documentation. AppScanLangs will output the languages to the console as a single line or list along with the count.

## Installation

* Clone this GitHub repository: git clone `https://github.com/gledonne/appscanlangs.git`

* Create a virtual environment: python -m venv *myvenv*
* Activate the virtual environment: \myvenv\Scripts>activate.bat or  VSCode
* Install required packages: pip install -r requirements.txt
* Upgrade pip (Optional): python.exe -m pip install --upgrade pip


## Usage

usage: python appscanlangs.py -f/--format <'list' (default) or 'line'>

Examples: 
* python appscanlangs.py
* python appscanlangs.py -f list
* python appscanlangs.py > listing.txt
* python appscanlangs.py -f list > listing.txt


## License

MIT License
