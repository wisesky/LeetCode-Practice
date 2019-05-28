import matplotlib.pyplot as plt
from wordcloud import WordCloud

s1 = []
s2 = []
with open('./isSubsequence.py') as f:
    for line in f:
        s1.append(line.strip())
with open('./getMoneyAmount.py') as f:
    for line in f:
        s2.append(line.strip())
s = [' '.join(x) for x in [s1,s2]]
st = ' '.join(s)
wc = WordCloud().generate(st)
#plt.imshow(wc)
#plt.show()
wc.to_file('./test.png')

