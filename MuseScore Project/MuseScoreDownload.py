import requests
import urllib.request

if __name__ == '__main__':
    extensions = ['mp3', 'mxl', 'mid']
    '''
    user_input = input("Search title: ")
    words = user_input.split(" ")
    query = "+".join(words)
    url = "https://musescore.com/sheetmusic?text=" + query
    print(url)
    request = requests.get(url)
    print(text)
    '''
    pdf_url = 'https://s3.ultimate-guitar.com/musescore.scoredata/gen/1/7/5/2431571/2b880c7c3ccf9dfdc15f3a2b26f0377eb5ff1a20/score_full.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=4SHNMJS3MTR9XKK7ULEP%2F20200307%2Fus-west%2Fs3%2Faws4_request&X-Amz-Date=20200307T035533Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Signature=f2690a33277af1205ea246e5c7b2cac3006c54173a08fb0a9dc17ce45f85e015'
    request = requests.get(pdf_url)
    pdf_address = 'C:/Users/Annie/Desktop/wearenumberone/score.pdf'
    urllib.request.urlretrieve(pdf_url, pdf_address)

    page_number = 0
    for ext in extensions:
        url = 'https://musescore.com/static/musescore/scoredata/gen/1/7/5/2431571/2b880c7c3ccf9dfdc15f3a2b26f0377eb5ff1a20/score.'
        file_url = url + ext
        address = 'C:/Users/Annie/Desktop/wearenumberone/score.'
        file_address = address + ext
        urllib.request.urlretrieve(file_url, file_address)