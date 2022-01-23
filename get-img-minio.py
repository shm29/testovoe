from minio import Minio

client = Minio(
        "192.168.29.21:9000",
        access_key="testovoe",
        secret_key="sektretnoe",
        secure=False)


response = client.get_object("test", "test (1) (2).jpg", offset=1000) 
f = response.read()
open('result.jpg', 'wb').write(f)
