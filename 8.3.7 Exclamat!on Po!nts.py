def exclamation(myStr):
    s = list(myStr)
    for i in range(len(s)):
        if s[i] == "i":
            s[i] = '!'
    myStr = "".join(s)
    return myStr
