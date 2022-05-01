# Configuration

Before start get your APP_ID and APP_HASH.
[Log in with this link](https://my.telegram.org/)

Then go to API development tools 
copy your api_id and api hash
create .env file and paste it there

## Start 

Just run
```shell
dokcer-compose up
```

And this command for kill container
```shell
dokcer-compose down
```

## Details

* File user_bots.py has example function which help you find out Id of your person for .env file 

* If you don`t see your APP_ID and APP_HASH you have to create your application in the website

* In first start you have to confirm your account in telegram.
If you don`t trust me, [follow this link](https://docs.pyrogram.org/start/auth)