from bs4 import BeautifulSoup
import requests


TABLE_NAMES = ["Indicative", "Subjunctive", "Imperative", "Progressive", "Perfect", "Perfect Subjunctive"]
SUBLIST_LENGTH = [5, 3, 2, 5, 5, 3]
PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/ellas/Uds."]


def getVerbData(verb):
    URL = f"https://www.spanishdict.com/conjugate/{verb}"

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    allTableData = []
    formattedData = {}
    allTables = soup.find_all("table")[1:]

    try:
        verbTranslation = soup.find("div", {"id": "quickdef1-es"}).text.capitalize()

        for sublistIndex, table in enumerate(allTables):
            tds = table.find_all("td")
            tableData = []
            for td in tds:
                if (text := td.text) not in PRONOUNS:
                    tableData.append(text)
            
            rowLength = SUBLIST_LENGTH[sublistIndex]
            del tableData[0]
            dividedTableData = [tableData[i:i+rowLength] for i in range(0, len(tableData)+rowLength, rowLength)][:-1]
            allTableData.append(dividedTableData)

        for tableIndex, tableData in enumerate(allTableData):
            formattedData[TABLE_NAMES[tableIndex]] = tableData
    except AttributeError:
        return False, False

    return formattedData, verbTranslation