import io
import time

begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
seconds = end - begin
print("Concat:", seconds)

begin = time.time()
buffer = io.BytesIO()
for i in range(0, 50000):
    buffer.write(b"Hello World")
end = time.time()
seconds = end - begin
print("BytesIO:", seconds)
