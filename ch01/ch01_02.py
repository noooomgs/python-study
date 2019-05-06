# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
text1 = 'パトカー'
text2 = 'タクシー'
res = ''
for i,s in enumerate(text1):
    res += s
    res += text2[i]
print(res)
