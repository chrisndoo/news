from flask import Flask
import requests

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
        <h1>Hello4!</h1>
        <a href="https://www.w3schools.com">here</a>
   
    </body>
</html>'''
  


if __name__=='__main__':

  app.run()
