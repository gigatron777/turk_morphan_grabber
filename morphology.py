import requests, re


url = 'http://coltekin.net/cagri/trmorph/index.php'

print('Enter ta word for morphological analysis:')
word = input()
answer = requests.post(url, data={'word': word, 'submit': 'Analyze'})

regexp1 = r'<td class="trmorph-demo-result">(.*?)</td>'
res = re.search(regexp1, answer.text, re.DOTALL).group(0)

for i in re.findall(r'<td(.*?)>', res, re.DOTALL):
    res = res.replace('<td' + i + '>', '')
for i in re.findall(r'<a(.*?)>', res, re.DOTALL):
    res = res.replace('<a' + i + '>', '')
for i in re.findall(r'<b>(.*?)</b>', res, re.DOTALL):
    res = res.replace('<b>' + i + '</b>', '')

res = res.replace('Analysis for the word :', '')
res = res.replace('</a>', '')
res = res.replace('<ul>', '')
res = res.replace('</ul>', '')
res = res.replace('</td>', '')
res = res.replace('<li>', '')
res = res.replace('<br>', '')
res = res.replace('&lt;', ' ')
res = res.replace('&gt;', ' ')


print(res)

input()