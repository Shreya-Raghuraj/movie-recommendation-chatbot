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
cd movie-recommendation-chatbot
```

2. Install dependencies

```bash
pip install flask scikit-learn google-genai
```

3. Add your Gemini API key

In `gemini.py`, replace:

```python
api_key="YOUR_API_KEY"
```

with your own Gemini API key.

Alternatively, use an environment variable:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

4. Run the application

```bash
python app.py
```

5. Open the chatbot in your browser:

```text
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
## Screenshots:
<img width="773" height="771" alt="Screenshot 2026-06-14 at 5 05 16 PM" src="https://github.com/user-attachments/assets/4db47c80-8592-43a0-b114-918222342fdc" />

<img width="773" height="695" alt="Screenshot 2026-06-14 at 5 05 33 PM" src="https://github.com/user-attachments/assets/5d4040eb-1c5e-44e8-97b6-212e5ca4b1db" />
