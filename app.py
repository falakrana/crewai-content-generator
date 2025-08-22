from flask import Flask, render_template, request
from crewai import Process, Crew
from agent import content_gatherer, content_thinker, content_writer
from task import content_gatherer_task, content_thinker_task, content_writer_task
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    topic = request.form['topic']
    age = request.form['age']
    social_media = request.form['socialMedia']
    formality = request.form['formality']

    # Store search history
    search_entry = {
        'timestamp': datetime.now().isoformat(),
        'topic': topic,
        'age': age,
        'socialMedia': social_media,
        'formality': formality
    }
    history = load_search_history()
    history.append(search_entry)
    save_search_history(history)

    crew = Crew(
        agents=[content_gatherer, content_thinker, content_writer],
        tasks=[content_gatherer_task, content_thinker_task, content_writer_task],
        process=Process.sequential
    )
    result = crew.kickoff(
        inputs={
            "topic": topic,
            "age": age,
            "socialMedia": social_media,
            "formality": formality
        }
    )
    return result

SEARCH_HISTORY_FILE = 'search_history.json'

def load_search_history():
    try:
        with open(SEARCH_HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_search_history(history):
    with open(SEARCH_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

if __name__ == '__main__':
    app.run(debug=True)