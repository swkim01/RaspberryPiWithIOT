import requests

KEY = "<KEY>"

def sendtrigger(eventname, value1, value2, value3):
    data = {}
    data["value1"]=value1
    data["value2"]=value2
    data["value3"]=value3
    res=requests.post("https://maker.ifttt.com/trigger/"+eventname+"/with/key/"+KEY, data=data)
    print("successfully sent with response: " + res.text)

if __name__ == "__main__":
    sendtrigger("alarm", 30.0, 60.0, "V")
