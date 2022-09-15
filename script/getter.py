import requests
import json

if __name__ == "__main__":
	res = requests.get("https://nasfaq.biz/api/getBettingPools")
	data = res.json()['bettingPools']
	with open("instructions.txt", 'r') as instructFile:
		instructions = instructFile.read().splitlines()
		out = {}
		with open(instructions[0]+".json", "w", encoding='utf8') as outfile:
			for id in instructions[1:]:
				if not data[id]["open"]:
					out[id] = data[id]
			json.dump(out, outfile, ensure_ascii=False)