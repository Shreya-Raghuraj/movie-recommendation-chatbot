# Movie Recommendation Chatbot

A Flask-based Movie Recommendation Chatbot that combines intent recognition using TF-IDF and Gemini AI fallback responses.

## Features

- Movie recommendations by genre
- Intent recognition using TF-IDF and cosine similarity
- Gemini AI fallback for unknown queries
- User-friendly chat interface
- Dynamic movie-related responses

## Technologies Used

- Python
- Flask
- Scikit-learn
- Google Gemini API
- HTML/CSS

## Project Structure

```
movie-recommendation-chatbot/
│
├── app.py
├── chatbot.py
├── gemini.py
├── intents.json
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

## Installation

1. Clone the repository

```bash
git clone <https://github.com/Shreya-Raghuraj/movie-recommendation-chatbot>
```

2. Install dependencies

```bash
pip3 install flask scikit-learn google-genai
```

3. Add Gemini API key in `gemini.py` [from google AI stuido]

4. Run the application

```bash
python app.py
```

5. Open

```
http://127.0.0.1:5000
```

## Supported Intents

- Greeting
- Goodbye
- Action movies
- Comedy movies
- Horror movies
- Thriller movies
- Romance movies
- Sci-Fi movies

## Fallback Handling

If user input does not match any predefined intent, Gemini AI generates a contextual response.
