# 📘 Introduction to Flask — A Complete Beginner’s Guide

A clean, minimal, and hands-on learning journey into **Flask**, the lightweight and flexible Python web framework. This repository mirrors a real-world development setup — from environment to project organization — for building scalable Flask apps step by step.

---

## 🚀 What is Flask?

Flask is a **micro web framework** for Python.

- Lightweight and minimal  
- Flexible structure — you define your architecture  
- Easy to learn and perfect for beginners  
- Extensible with a rich ecosystem of third-party tools  

---

## ⚔️ Flask vs Django — What's the Difference?

| Feature        | Flask                            | Django                          |
| ------------- | --------------------------------- | ------------------------------- |
| Design        | Micro-framework (minimal core)    | Full-stack framework            |
| Structure     | Developer-defined (flexible)      | Convention-based (pre-defined)  |
| Admin UI      | Not included by default           | Built-in admin panel            |
| Best For      | APIs, small apps, rapid prototyping | Large-scale feature-rich apps |
| Learning Curve| Simple & beginner-friendly        | Steeper but comprehensive       |

---

## 🛠️ Project Setup

### 📁 Step 1: Create Project Directory

```bash
mkdir Flask-Learning && cd Flask-Learning\app
````

---

### 🐍 Step 2: Create and Activate Virtual Environment

```bash
python -m venv MyEnvironment
```

#### ✅ Activate (PowerShell)

```bash
.\MyEnvironment\Scripts\Activate.ps1

or

.\Flask-Learning\MyEnvironment\Scripts\Activate.ps1
```

> To deactivate:

```bash
deactivate
```

---

### 📦 Step 3: Install Flask Inside Virtual Environment

```bash
pip install flask
```

---

## 📂 Project Structure

```
Flask-Learning/
│
├── app/                        # Core application folder
│   ├── app.py                  # Main Flask app
│   └── templates/              # Jinja2 HTML templates
│       └── Welcome.html        # Sample template
│
├── MyEnvironment/              # Virtual environment (not pushed to GitHub)
├── .gitignore                  # Ignores MyEnvironment and other unnecessary files
└── Readme.md                   # Project documentation
```

---

Exactly ✅ — you're absolutely right!

No need to include the actual Flask server code (`app.run(...)`) in your **README.md**, since:

* It's already written in your `app.py`.
* Anyone checking your GitHub repo will see the code directly.
* Your README should focus on **how to run**, not replicate the source code.

So here's the clean version for your **README** section:

---

## ▶️ How to Run the Flask Server

Once you're inside the virtual environment and at the root of your project:

```bash
python app.py
```

By default, Flask will run on:

```
http://127.0.0.1:5000
```

> If you've set a custom host and port (like `0.0.0.0:3000`), Flask will reflect that in the terminal when the server starts.

---

## 🌱 What’s Coming Next?

* Dynamic routes & URL parameters
* Using Jinja2 templates
* Handling forms & POST requests
* Flask Blueprints
* Connecting databases
* REST API with Flask

Stay tuned! This repo will grow along with your Flask skills 🔥

---

## 📚 References

* [Flask Official Docs](https://flask.palletsprojects.com/)
* [Jinja2 Templates](https://jinja.palletsprojects.com/)
* [Flask GitHub Repo](https://github.com/pallets/flask)

---

Happy Coding 🧪✨