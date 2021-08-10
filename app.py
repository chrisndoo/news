from flask import Flask
import ny
app=Flask(__name__)

@app.route('/')

def index():
   

    headdict = ny.get_headlines()

    x0 = '<title>' + '头条' + '</title>'

    i=0
    x =''
    for i in headdict:
    
        #x1 = '<p>' + headdict[i][0] + '</p>'
        
        x2 = '<a href="' + headdict[i][2] + '">' + '<p>' + headdict[i][1] + '</p>' + '</a>' 

        x = x+x2


   return '''
<html>
    <head> 
    ''' + x0 + '''
        
    </head>
    <body>
        <h1>Hello!</h1>
        <a href="https://www.w3schools.com">here</a>
        ''' + x + '''
    </body>
</html>'''

  


if __name__=='__main__':

  app.run()
