from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)
   
@app.route('/')         
def hello_world():
    return render_template('index.html', color='blue')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 