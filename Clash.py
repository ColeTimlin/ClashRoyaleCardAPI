import urllib.request
import json

with open("key.txt") as f:
        key = f.read().rstrip("\n")
        url = "https://api.clashroyale.com/v1/"
        endpoint = "cards"
        
        

        request = urllib.request.Request(
                        url+endpoint,
                        None,
                        {
                            "Authorization": "Bearer %s" % key
                        }
        )
        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)

        print(data)

        for item in data["items"]:
                print("\n%s \n[Max Level: %d]" % (item["name"], item["maxLevel"]))

