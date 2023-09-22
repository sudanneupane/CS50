import requests
import json
import sys
def get_bitcoin(bit):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
    except requests.RequestException:
        sys.exit()
    out_data = response.json()
    # Gives out the response data into proper json formatted form
    # print(json.dumps(out_data, indent = 2))
    rate = out_data["bpi"]["USD"]["rate_float"]
    res = bit * rate
    return res

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        accept = float(sys.argv[1])
    except TypeError:
        sys.exit("Command-Line argument is not a number")
    else:
        print(f"${get_bitcoin(accept):,.4f}")

if __name__ == "__main__":
    main()

