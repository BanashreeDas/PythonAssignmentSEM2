str=input("enter the text : ")
dict={}

def ReplaceChar(str):
    for i in range(len(str)):
        if str[i] in dict:
            str=str[:i]+ "*" + str[i+1:]
        dict[str[i]]=i
    return str

print(ReplaceChar(str))
