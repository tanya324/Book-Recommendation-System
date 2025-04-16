from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

recommendations = {
    "happy": {
        "fantasy": ["Harry Potter", "The Hobbit", "Percy Jackson"],
        "romance": ["The Rosie Project", "Love & Gelato", "Me Before You"]
    },
    "sad": {
        "drama": ["A Little Life", "The Fault in Our Stars", "Tuesdays with Morrie"],
        "mystery": ["Gone Girl", "Sharp Objects", "The Girl on the Train"]
    },
    "excited": {
        "adventure": ["The Maze Runner", "Ready Player One", "Jurassic Park"],
        "sci-fi": ["Dune", "Ender's Game", "Project Hail Mary"]
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    books = []
    if request.method == 'POST':
        mood = request.form['mood'].lower()
        genre = request.form['genre'].lower()
        books = recommendations.get(mood, {}).get(genre, ["No books found."])
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
