from flask import Flask
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

app=Flask(__name__)

@app.route('/')

def index():
   

    x0 = '<title>' + '头条' + '</title>'




    return '''
<html>
    <head> 
    ''' + x0 + '''
        
    </head>
    <body>
        <h1>Hello!</h1>
        <a href="https://www.w3schools.com">here</a>
   
    </body>
</html>'''
  


if __name__=='__main__':

  app.run()