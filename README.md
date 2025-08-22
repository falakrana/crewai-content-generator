# Content Generator 
![Extension Screenshot](/image.png) 
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Project Description
This project is a Flask-based web application that generates content based on user input. It utilizes a CrewAI framework to orchestrate different AI agents (content gatherer, thinker, and writer) to produce tailored content. The application now also stores a history of all content generation requests.

## Table of Contents
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [File Structure](#file-structure)

## Features ✨
*   **Content Generation**: Generate content based on a specified topic, target age group, social media platform, and desired formality.
*   **AI-Powered Agents**: Leverages a multi-agent system (CrewAI) for intelligent content creation.
*   **Search History**: Automatically stores a detailed history of all content generation requests, including input parameters and timestamps, in a `search_history.json` file.

## Setup and Installation 🚀

### Prerequisites
*   Python 3.10+
*   pip (Python package installer)

### Steps

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd content-generator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv content-Env
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .\content-Env\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source content-Env/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/`.

## Usage 💡
1.  Navigate to the application in your web browser (e.g., `http://127.00.0.1:5000/`).
2.  Fill out the content generation form on the `index.html` page, providing details such as:
    *   **Topic**: The subject for content generation.
    *   **Age**: The target age group for the content.
    *   **Social Media**: The social media platform the content is intended for.
    *   **Formality**: The desired tone (e.g., formal, informal).
3.  Click the "Generate Content" button.
4.  The generated content will be displayed on the page.
5.  All search requests will be logged in `search_history.json`.

## File Structure 📂
*   `app.py`: The main Flask application, handling routes and integrating with CrewAI.
*   `agent.py`: Defines the AI agents used for content generation.
*   `task.py`: Defines the tasks assigned to the AI agents.
*   `requirements.txt`: Lists all Python dependencies.
*   `templates/`: Contains HTML templates (`index.html`, `about.html`, `base.html`).
*   `search_history.json`: Stores the history of content generation requests.


## Future enhancement
1.  Implementing memory for each sessino by user.
