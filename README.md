# Configuration

Before start get your APP_ID and APP_HASH.
[Log in with this link](https://my.telegram.org/)

Then go to API development tools 
copy your api_id and api hash
create .env file and paste it there

## Instalation 

1. Build image 
``` shell
docker build -t borobot .
```

2. Run container
``` shell
docker run -d --rm --name borobot borobot
```


3. Stop container
``` shell
docker stop borobot
```

## Details

*If you don`t see your APP_ID and APP_HASH you have to create your application in the website

*In first start you have to confirm your account in telegram.
If you don`t trust me, [follow this link](https://docs.pyrogram.org/start/auth)