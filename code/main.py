# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import iris
#import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cnt = 0
    print_hi('PyCharm')
    f = open("C:\\data\\file1.txt","r")
    w = open("C:\\data\\file2.txt","w")
    for x in f:
        #print(x.count("|"))
        if x.count("|") > 4:
            w.write(x)
        else:
            cnt = cnt + 1
    print("The number of invalid records  : {}".format(cnt))

    mydict = { 1:{"name": "KT",
               "age":38,
               "interest":"Cricket"},
               2:{"name": "AP",
                "age": 36,
                "interest": "Cinema"}
               }
    ##mydict["birthyear"] = 1982
    ##mydict.pop("age")

    for x,y in mydict.items():
        print(x)
        for key in y:
            print(key + " :" + str(y[key]))
    print("This is the name of the person : {} ".format(mydict[2]["name"]))

    js = open("C:\\data\\testjson.json","r")
    a = json.load(js)
    for m in a["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"]:
        print("This is the json entry : " + m)
    try:
        print("This is the json entry : " + a["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"])
    except:
        print("exception the the type of the json entry")

    l1 = [12,234,233,222,134,5,55,444,33,222,222]

    print(sum(l1))

    for item in l1[2:len(l1) - 1]:
        print(item)

    s1 = set(l1)
    print(sum(s1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


