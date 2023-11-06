import asyncio
import os
import urllib.request

# Creating Coroutines

async def download_coroutine(url):
    request = urllib.request.urlopen(url)
    filename = os.path.basename(url)

    with open(filename, 'wb') as file_handle:
        while True:
            chunk = request.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
        msg = f'Finished downloading {filename}'
        return msg
    
# calling coroutines
async def main(urls):
    coroutines = [await download_coroutine(url) for url in urls]
    await asyncio.wait(coroutines)
              
urls = ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
"https://www.orimi.com/pdf-test.pdf",
]

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(urls))
finally:
    event_loop.close()
# asyncio.run(main(urls))