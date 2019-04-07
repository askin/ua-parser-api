User Agent rest server
===

_A simple user agent parser API_

Run
---

```bash
virtualenv -p python3.7 fenv
source fenv/bin/activate
pip3.7 install -r requirements.txt
uvicorn app.main:app --reload
```


```bash
docker run --rm -p 8000:8000 -d askinozgur/ua-parser-api
```

### Request Examples
Curl Example
```bash
curl -X GET "http://localhost:8000/detect?user_agent=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F73.0.3683.103%20Safari%2F537.36" -H "accept: application/json"
```

Request URL
```
http://localhost:8000/detect?user_agent=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F73.0.3683.103%20Safari%2F537.36
```

Response
```json
{
  "user_agent": {
    "family": "Chrome",
    "major": "73",
    "minor": "0",
    "patch": "3683"
  },
  "os": {
    "family": "Linux",
    "major": null,
    "minor": null,
    "patch": null,
    "patch_minor": null
  },
  "device": {
    "family": "Other",
    "brand": null,
    "model": null
  },
  "string": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
```


### Interactive API docs

Now go to <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" target="_blank">Swagger UI</a>):

### Alternative API docs

And now, go to <a href="http://127.0.0.1:8000/redoc" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" target="_blank">ReDoc</a>):
