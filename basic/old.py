import ssl

from urllib.request import Request
from urllib.request import urlopen

context = ssl._create_unverified_context()

# HTTP 请求
request = Request(
  url="https://foofish.net/pip.html",
  method="GET",
  headers={"Host": "foofish.net"},
  data=None
)

# 响应
response = urlopen(request, context=context)
headers = response.info() # 响应头
content = response.read() # 响应体
code = response.getcode() # 状态码
print(content)