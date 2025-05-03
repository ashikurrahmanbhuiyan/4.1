import requests

def get_latest_block(api_key):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "proxy",
        "action": "eth_getBlockByNumber",
        "tag": "latest",
        "boolean": "true",
        "apikey": api_key,
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["result"]
        else:
            print("Request failed with status code:", response.status_code)
    except requests.RequestException as e:
        print("Request failed:", str(e))

    return None


api_key = "E34342B4IR3B8RI3K61XG4YKEUT7SR54MM"

latest_block = get_latest_block(api_key)

if latest_block is not None:
    print("Latest block information:")
    print("Block Number:", int(latest_block["number"], 16))
    print("Timestamp:", int(latest_block["timestamp"], 16))
    print("Miner Address:", latest_block["miner"])
    print("Difficulty:", int(latest_block["difficulty"], 16))
    print("Total Difficulty:", int(latest_block["totalDifficulty"], 16))
    print("Gas Limit:", int(latest_block["gasLimit"], 16))
    print("Gas Used:", int(latest_block["gasUsed"], 16))
    print("Transaction Count:", len(latest_block["transactions"]))
    print("Transactions:")
    
    for tx in latest_block["transactions"]:
        print("Transaction Hash:", tx["hash"])
        print("From:", tx["from"])
        print("To:", tx["to"])
        print("Value (in Wei):", tx["value"])
        print("\n")
else:
    print("Failed to fetch the latest block information.")
