# ManyRequests
Library for making many python requests concurrently.

```python
from ManyRequests.WebRunner import WebRunner

urls = [u'http://google.com'] * 100
proxies = {
    u'http': u'http://example.com',
    u'https': u'http://example.com'
}

runner = WebRunner()
responses = runner.run(urls, concurrency=20, proxies=proxies, timeout=10)

responses
>> [<Response [200]>,
>> <Response [200]>,
>> <Response [200]>,
>> <Response [200]>,
>> ...
>> <Response [200]>,
>> <Response [200]>,
>> <Response [200]>,
>> <Response [200]>]

```