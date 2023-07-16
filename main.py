import uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


with open('file_a.txt', 'wb') as file:
    file.write(b'a')
with open('file_b.txt', 'wb') as file:
    file.write(b'b')