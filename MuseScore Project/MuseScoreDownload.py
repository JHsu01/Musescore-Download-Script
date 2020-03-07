import requests
import urllib.request

if __name__ == '__main__':
    extentions = ['mp3', 'xml', 'mid']
    '''
    user_input = input("Search title: ")
    words = user_input.split(" ")
    query = "+".join(words)
    url = "https://musescore.com/sheetmusic?text=" + query
    print(url)
    request = requests.get(url)
    print(text)
    '''
    page_number = 0
    pdf_url = 'https://s3.ultimate-guitar.com/musescore.scoredata/gen/1/7/5/2431571/2b880c7c3ccf9dfdc15f3a2b26f0377eb5ff1a20/score_full.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=4SHNMJS3MTR9XKK7ULEP%2F20200307%2Fus-west%2Fs3%2Faws4_request&X-Amz-Date=20200307T031028Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Signature=8ae18e3f15d459c02d9b90c2306777e1eb6556fdb931f1a9aa3e5194f9fb5099'
    request = requests.get(pdf_url)
    pdf_address = 'C:/Users/Annie/Desktop/wearenumberone/score.pdf'
    urllib.request.urlretrieve(pdf_url, pdf_address)
    '''
    url = 'https://musescore.com/static/musescore/scoredata/gen/1/7/5/2431571/2b880c7c3ccf9dfdc15f3a2b26f0377eb5ff1a20/score.'
    address = 'C:/Users/Annie/Desktop/wearenumberone/score.'
    for ext in extentions:
        new_url = url + ext
        file_address = address + ext
        urllib.request.urlretrieve(new_url, file_address)
    '''
