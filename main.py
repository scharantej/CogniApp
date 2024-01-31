
# Importing necessary modules
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def homepage():
    """
    Renders the homepage of the website.
    """
    return render_template('home.html')

# Define the route for the Basics of AI page
@app.route('/basics')
def basics():
    """
    Renders the Basics of AI page.
    """
    return render_template('basics.html')

# Define the route for the Advanced Topics in AI page
@app.route('/advanced')
def advanced():
    """
    Renders the Advanced Topics in AI page.
    """
    return render_template('advanced.html')

# Define the route for the Generative AI page
@app.route('/genai')
def genai():
    """
    Renders the Generative AI page.
    """
    return render_template('genai.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
