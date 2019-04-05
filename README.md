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


### Interactive API docs

Now go to <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" target="_blank">Swagger UI</a>):

### Alternative API docs

And now, go to <a href="http://127.0.0.1:8000/redoc" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" target="_blank">ReDoc</a>):
