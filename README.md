# ja3-server

Thanks to [nginx-ssl-ja3](https://github.com/fooinha/nginx-ssl-ja3), we can obtain ja3 information without invading existing services.

Refer to `nginx-ssl-ja3` to configure nginx and forward the ja3 information to the service through the header.

## Usage
```shell
git clone git@github.com:vvanglro/ja3-server.git
cd ja3_server/docker
docker-compose up
```
```python
import requests

resp = requests.get("https://your-ip/", verify=False)
print(resp.json())
```