import requests
api_key="API_KEY"
def function():
    fromc=input("enter From currency :").upper()
    api_key="633a0d1922729eafe469d0a8"
    url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{fromc}"
    try:
        data=requests.get(url,timeout=5)
    except requests.exceptions.RequestException as f:
        print(f"Connection reset by peer{f}")
    data1=data.json()
    status_code=data1["result"]
    while True:
        if status_code=="success":
            toc=input("enter To currency :").upper()
            if toc in data1["conversion_rates"]:
                amount=float(input("enter the amount :"))
                get1=data1["conversion_rates"][toc]
                total=get1*amount
                try:
                    with open("currency_converter.txt", "a") as f:
                        f.write(f"From :{fromc}\nTo :{toc}\nAmount :{amount}\nTotal :{total}")
                        f.write("\n---------------------\n")
                    print("______________________________")
                    print(f"{fromc} to {toc} :{total:.2f}{toc}")
                    print("______________________________")
                except FileNotFoundError:
                    print("file not found")
                break
            else:
                print("Invalid currency")
        else:
            print("Invalid currency")
            break
function()
while True:
    retry = input("Do another conversion? (y/n)").upper()
    if retry=="Y":
        function()
    else:
        print("Thank You")
        break
