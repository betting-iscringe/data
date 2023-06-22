import requests
import datetime
import json
from pathlib import Path

# Checks betting history which betting pools aren't recorded
if __name__ == "__main__":
    scriptDir = str(Path(__file__).parent.resolve())
    parentDir = str(Path.cwd())
    data = {}
    compilation = {}
    res = requests.get("https://nasfaq.biz/api/getBettingHistory")
    bettingHistory = res.json()["bettingHistory"]
    for pastBets in bettingHistory:
        if pastBets["poolTotal"] > 0:
            dt = datetime.datetime.fromtimestamp(pastBets["timestamp"]/1000)
            data[pastBets["id"]] = {
                "id": pastBets["id"],
                "topic": pastBets["topic"],
                "timestamp": pastBets["timestamp"],
                "date": str(dt),
            }
    for folder in ["divegrass", "hfz", "etc"]:
        files = Path(parentDir + "\\" + folder).glob("*")
        for file in files:
            if not file.name.startswith("index"):
                with open(file, "r", encoding="utf8") as bets:
                    betDict = json.loads(bets.read())
                    compilation.update(betDict)
    for key in compilation:
        try:
            data.pop(key)
        except:
            print("Key not found: " + key)
    # Writing to sample.json
    with open(scriptDir + "\\discrepancy.json", "w", encoding="utf8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)
