# 3a
def split(st, sep):
    result = []
    occurrence = st.find(sep)

    while occurrence != -1:
        result.append(st[:occurrence])
        st = st[occurrence + 1:]
        occurrence = st.find(sep)

    if st != '':
        result.append(st)

    return result

print(split("1232542234323322232", "2"))