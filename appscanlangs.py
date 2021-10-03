import argparse
import pandas as pd
import requests
from bs4 import BeautifulSoup

ASoC_URL = "https://help.hcltechsw.com/appscan/ASoC/src_language_support.html"
Source_URL = "https://help.hcltechsw.com/appscan/Source/10.0.5/topics/system_requirements_win.html"


def getASoCLangs(url):
    """Scraps the ASoC online documentation to produce a list of supported languages.

    Args:
        None

    Returns:
        list: a list of strings representing the supported languages
    """

    # Define the AppScan Source system requirements url
    # Define the table on the page where the languages are specified (zero based)
    supportedLanguagesTable = 0

    # Scrap the table from the web page
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all("table")[supportedLanguagesTable]
    # print(table)

    # Bring the table into Pandas for processing
    df = pd.read_html(str(table), keep_default_na=False)

    # Get list of languages
    langs = df[0]["Language"].to_list()
    # print(df[0].info())

    return langs


def getSourceLangs(url):
    """Scraps the AppScan Source online documentation to produce a list of supported languages.

    Args:
        None

    Returns:
        list: a list of strings representing supported languages
    """

    # Define the AppScan Source system requirements url
    # Define the table on the page where the languages are specified (zero based)
    supportedLanguagesTable = 4

    # Scrap the table from the web page
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all("table")[supportedLanguagesTable]
    # print(table)

    # Bring the table into Pandas for processing
    df = pd.read_html(str(table), header=1, keep_default_na=False)

    # Get list of languages
    langs = df[0]["Supported  software"].to_list()
    # print(df[0].info())

    # Remove blank entries
    langs = list(filter(None, langs))
    # print(langs)

    # Create a new list of language only items
    ignore = [
        "Apache Tomcat",
        "IBM Runtime Environment, Java Technology  Edition",
        "Microsoft Visual Studio",
        "Oracle WebLogic Server 12c",
        "Oracle WebLogic Server 12cR1",
        "Oracle/BEA WebLogic Server",
        "Sun Java SDK/JRE/JDK",
        "WebSphere Application Server",
    ]
    newLangs = [x for x in langs if x not in ignore]

    return newLangs


def printLangs(languages, fmt="line"):
    """Prints/outputs the list of languages to the console.

    Args:
        languages: list of languages
        fmt:
            'line': outputs as a single string. Default
            'list': outputs one string/language per line

    Returns:

    """

    if fmt == "line":
        print(languages)
    elif fmt == "list":
        for l in languages:
            print(l)
    print("Count: %d\n" % len(languages))


if __name__ == "__main__":

    # Create the parser
    parser = argparse.ArgumentParser()

    # Add long and short argument
    parser.add_argument(
        "-f",
        "--format",
        choices=["line", "list"],
        default="line",
        help="output format",
    )

    # Read arguments from the command line
    args = parser.parse_args()

    # Check for -f/--format
    fmt = "line"
    if args.format == "list":
        fmt = "list"

    # Print langs to the console
    printLangs(getSourceLangs(Source_URL), fmt)
    printLangs(getASoCLangs(ASoC_URL), fmt)
