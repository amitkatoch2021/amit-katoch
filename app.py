from flask import Flask
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
@app.route('/') 
def home():
	return "Wow this is a basic output!"
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',debug=True)  # EStablishes the host, required for repl to detect the site

 # '/' for the default page
