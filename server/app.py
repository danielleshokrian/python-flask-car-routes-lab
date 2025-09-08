from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Home route
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Dynamic route - show car model if it exists
@app.route('/<model>')
def show_models(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(port=5555, debug=True)