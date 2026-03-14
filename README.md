# 🎬 Movie Recommendation System

A **Movie Recommendation System** built using **Collaborative Filtering** that recommends movies based on similarity between user ratings. The system analyzes user–movie interactions and suggests movies similar to the one selected by the user.

---

## 🚀 Features

* 📊 Uses **Collaborative Filtering** based on user ratings
* 📈 Computes movie similarity using **Cosine Similarity**
* 🎯 Recommends **Top 5 similar movies**
* 📁 Uses the **MovieLens dataset**
* 🌐 Interactive **web interface built with Streamlit**
* ⚡ Fast recommendations using a **user–movie rating matrix**

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
movie-recommendation-system
│
├── app.py
├── movies.csv
├── ratings.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/Charan-dev247/movie-recommendation-system.git
```

### 2️⃣ Navigate to the Project Folder

```
cd movie-recommendation-system
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

If requirements.txt is not available:

```
pip install streamlit pandas scikit-learn numpy
```

### 4️⃣ Run the Streamlit App

```
python -m streamlit run app.py
```

---

## 🌐 Running Application

After running the command above, Streamlit will generate a local server URL such as:

```
http://localhost:8501
```

Open this URL in your browser to access the application.

---

## 🎯 How the Recommendation Works

1. User selects a movie from the dropdown.
2. A **User–Movie Rating Matrix** is created from the dataset.
3. Missing ratings are filled with zeros.
4. **Cosine similarity** is calculated between movies.
5. The system returns the **Top 5 most similar movies**.

---

## 📊 Dataset

This project uses the **MovieLens dataset**, which contains user ratings for thousands of movies.

---

## 📌 Future Improvements

* Add **movie posters using TMDB API**
* Implement **content-based filtering**
* Improve UI with movie cards
* Deploy the application online

---

## 👨‍💻 Author

**Charan**

GitHub:
https://github.com/Charan-dev247
