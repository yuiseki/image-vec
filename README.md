# image to vector REST API docker image powered by img2vec_pytorch

## Run test
```
pytest
```

## Run server
```
export FLASK_APP="src/main.py" && flask run
```

## API
- `/vector.json`
  - `GET`
    - request params
      - url
    - response type
      - `application/json`
  - `POST`
    - request params
      - image_b64
    - response type
      - `application/json`