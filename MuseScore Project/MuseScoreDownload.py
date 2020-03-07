import urllib.request

if __name__ == '__main__':
    extensions = ['mp3', 'mxl', 'mid']
    user_input = input("Search title: ")
    words = user_input.split(" ")
    query = "+".join(words)
    url = "https://musescore.com/sheetmusic?text=" + query
    print(url)
    urllib.request.urlretrieve(url, 'C:/Users/Annie/Desktop/searchresults.png')

    pdf_url = 'https://musescore.com/score/2431571/download/pdf?h=12201921758843614765'
    pdf_address = 'C:/Users/Annie/Desktop/wearenumberone/score.pdf'
    urllib.request.urlretrieve(pdf_url, pdf_address)

    for ext in extensions:
        url = 'https://musescore.com/static/musescore/scoredata/gen/1/7/5/2431571/2b880c7c3ccf9dfdc15f3a2b26f0377eb5ff1a20/score.'
        file_url = url + ext
        address = 'C:/Users/Annie/Desktop/wearenumberone/score.'
        file_address = address + ext
        urllib.request.urlretrieve(file_url, file_address)