import requests, json
percentIn = str(input("What percent would you like to increase the overall price?"))
percent = 0.0
if len(percentIn) == 1:
  percent = float("0.0"+percentIn)
else:
  percent = float("0."+percentIn)
print("\nWill increase overall display value by "+str(percent)+"\n")

overallPrice = 0
while True:
  item = str(input("Add an item or enter q to quit: "))
  if item.lower() == "q":
    break
  else:
    item = item.replace(" ","_")
    r = requests.get("http://acnhapi.com/v1/houseware/"+item)
    if "Furniture not found" in r.text:
      r = requests.get("http://acnhapi.com/v1/misc/"+item)
      if "Furniture not found" in r.text:
        r = requests.get("http://acnhapi.com/v1/wallmounted/"+item)
        if "Furniture not found" in r.text:
          r = requests.get("http://acnhapi.com/v1/art/"+item)
          if "Art not found" in r.text:
            r = requests.get("http://acnhapi.com/v1/fossils/"+item)
            if "Fossil not found" in r.text:
              r = requests.get("http://acnhapi.com/v1/bugs/"+item)
              if "Bug not found" in r.text:
                r = requests.get("http://acnhapi.com/v1/sea/"+item)
                if "Sea Creature not found" in r.text:
                  r = requests.get("http://acnhapi.com/v1/fish/"+item)
                  if "Fish not found" in r.text:
                    print("Invalid item!")
                    continue
    value = json.loads(r.text)
    try:
      price = int(value[0]["sell-price"])
    except:
      price = int(value["price"])
    print("\nThis item costs "+str(price)+" at Nook's Cranny. Adding to total..\n")
    overallPrice += price
print("\nThis lot of goods would normally sell for "+str(overallPrice)+" bells at Nook's Cranny. Adding your specified percent would raise this to "+str(int(overallPrice + (overallPrice * percent)))+".\n")
