#!/usr/bin/python

import requests

links = open('links', 'r')

counter = 0

def download_pdf(request, filename):
  with open('Downloads/'+filename, 'wb+') as f:
    f.write(request.content)


for link in links:
  filename = str(counter) + '-'+link[23:-1] + '.pdf'
  url = 'https://url-to-pdf-api.herokuapp.com/api/render?url=' + link[:-1] +'&emulateScreenMedia=false'
  try:
    r = requests.get(url)
    download_pdf(r, filename)
    counter = counter + 1
  except Exception as e:
    print 'error =>' + str(e)



