# Configuration

Before start get your APP_ID and APP_HASH. 
[Log in with this link](https://my.telegram.org/)

Then go to API development tools 
copy your api_id and api hash
paste it to .env file

2. Build image 
docker build -t borobot .

3. Run container
docker run -d --rm --name borobot borobot

4. Stop container
docker stop borobot

In first start you need confirm your account in telegram.
If you don`t trust me, follow this link 
https://docs.pyrogram.org/start/auth