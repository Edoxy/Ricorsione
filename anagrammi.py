anagrammi = []
def anag(str, pre):
    if str == "":
        anagrammi.append(pre)
        return
    for c in str:
        pos = str.find(c)
        new_str = str[:pos] + str[pos+1 :]
        new_pre = pre + c
        anag(new_str, new_pre)
    return

anag("dog", "")
print(anagrammi, len(anagrammi))