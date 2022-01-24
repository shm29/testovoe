from minio import Minio

print("Write host's IP that you set in playbook.yml vars")
print("If click on enter while input empty, default 192.168.57.21")
host = input()
if not host:
    host = "192.168.57.21"
print("Write service's port")
print("If click on enter while input empty, default 9000")
port = input()
if not port:
    port = "9000"
address = host+":"+port
print("Connecting",address)
client = Minio(
        address,
        access_key="testovoe",
        secret_key="sekretnoe",
        secure=False)

# true upload of test.img, as it is distributed object storage and you can't just scp files into bucket
try:
    client.make_bucket("true-bucket")
except:
    pass
client.fput_object("true-bucket", "img-object", "test.jpg")

# download the true file :)
response = client.get_object("true-bucket","img-object", offset=1000) 
f = response.read()
open('result.jpg', 'wb').write(f)
print("Image successfully downloaded with 1000 bytes offset")
