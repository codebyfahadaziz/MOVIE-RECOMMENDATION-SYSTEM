# MOVIE-RECOMMENDATION-SYSTEM
🎬 Lights, Camera… Recommendations! 🍿 This Movie Recommendation System is an interactive web app that helps you discover new movies based on what you already love. Built with Python and Streamlit, it instantly suggests five similar movies when you select a title — complete with official posters fetched live from The Movie Database (TMDB) API.
A Movie Recommendation System built with Python and Streamlit that suggests 5 similar movies based on your choice — complete with live movie posters from The Movie Database (TMDb) API.

Think of it as your own Netflix “More Like This” — but handcrafted from scratch!

✨ Features
🎥 Intelligent Similarity Search — Uses movie metadata & keywords to find related films.

🖼️ Dynamic Poster Fetching — Pulls official posters live from TMDb API.

⚡ Fast & Interactive UI — Built with Streamlit for instant results.

📂 Optimized Backend — Pandas & Pickle for lightning-fast lookups.

🔧 Tech Stack
Python 🐍

Pandas 📊

Streamlit 🌐

TMDb API 🎟️

Pickle 📦

GitHub 💻

📌 How It Works — Flowchart
mermaid
Copy
Edit
flowchart TD
    A[User selects a movie 🎥] --> B[System fetches movie index]
    B --> C[Finds similarity scores from precomputed matrix 📊]
    C --> D[Sorts movies by highest similarity 🔍]
    D --> E[Selects top 5 matches 🏆]
    E --> F[Fetches posters from TMDb API 🖼️]
    F --> G[Displays movies & posters in Streamlit UI 💻]
🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
2️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
📂 Project Structure
bash
Copy
Edit
📦 movie-recommender
├── app.py                # Streamlit app script
├── movies_dict.pkl       # Preprocessed movie data
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # Python dependencies
└── README.md             # This file
🌟 Example Output
You pick: 🎥 Inception
You get:

Interstellar

The Prestige

Shutter Island

The Matrix

Tenet

Each with an official movie poster & clickable TMDb link.

💡 Inspiration
This project was built as a fun deep dive into:

Data preprocessing

Content-based recommendation systems

API integration

Interactive UI development

📜 License
This project is licensed under the MIT License — free to use, modify, and share.


