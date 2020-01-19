import requests
url = "http://httpbin.org/get"
headers = {'user-agent': 'Mozilla/5.0'}
params = {"key":"val"}
cookies = {'from-my': 'browser'}
timeout = 100
proxies = {
  'http': 'http://127.0.0.1:1080',
  'https': 'http://127.0.0.1:1080',
}
r = requests.get(
  url,
  headers=headers,
  params=params,
  cookies=cookies,
  timeout=timeout,
  proxies=proxies
)
print(r.text)
