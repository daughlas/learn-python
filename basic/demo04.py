import requests


class SimpleCrawler:
    def crawl(self, params=None):
        # 必须指定UA，否则知乎服务器会判定请求不合法

        url = "https://www.zhihu.com/api/v4/columns/pythoneer/followers"
        # 查询参数
        params = {"limit": 30,
                  "offset": 0,
                  "include": "data[*].follower_count, gender, is_followed, is_following"}

        headers = {
            "authority": "www.zhihu.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        response = requests.get(url, headers=headers, params=params)
        # 解析返回的数据
        for follower in response.json().get("data"):
            print(follower['name'])


if __name__ == '__main__':
    SimpleCrawler().crawl()