# image to vector REST API docker image powered by img2vec_pytorch

## Run test
```
pytest
```

## Run server
```
python src/main.py
```

## Build Docker image
```
./build.sh
```

## Run server by Docker image
```
docker run -it yuiseki/image-vec
```

## API
- `/vector.json`
  - `GET`
    - request params
      - url
    - response type
      - `application/json`
  - `POST`
    - request type
      - `application/x-www-form-urlencoded`
    - request params
      - image_b64
        - string of base64 encoded image binary
    - response type
      - `application/json`

## ToDo
- エラー処理
  - GET
    - 200以外のURLだったらエラーを返す
    - 画像以外の場合はエラーを返す
    - 巨大すぎる画像の場合はエラーを返す
  - POST
    - base64 decodeに失敗したらエラーを返す
- 学習モデルを選択できるようにする

