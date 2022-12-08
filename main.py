import json
with open("response.json", "r") as read_file:
    data = read_file.read()
    data = json.loads(data)
    print(data)
    #r