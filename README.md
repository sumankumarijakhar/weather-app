# Weather App - CI/CD Pipeline with GitHub Actions

This is a small weather app project I created for my midterm assignment. I built a Continuous Integration pipeline using GitHub Actions. The pipeline builds the app, runs unit tests, performs lint checks, creates a Docker image, and pushes it to Docker Hub. I also implemented multi-environment deployment using `develop` and `main` branches.

## 🗂️ Project Structure

```
weather-app/
│
├── app.py                 # Main application script
├── test_app.py            # Unit tests
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker build instructions
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
├── .gitignore             # Files to ignore in Git
└── README.md              # Project information
```

## 🚀 How to Run the App

1. Clone the repo:
```bash
git clone https://github.com/sumankumarijakhar/weather-app.git
cd weather-app
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

Make sure to get an API key from https://openweathermap.org and add it to your environment or directly in the code if testing.

---

## ✅ How CI Pipeline Works

### Trigger
- **Dev Environment**: Automatically runs when I push to `develop` branch.
- **Prod Environment**: Manually triggered through GitHub Actions workflow tab (for main branch).

### Stages

- **Build**: Installs all dependencies from requirements.txt.
- **Lint**: Uses `flake8` to check for code issues.
- **Test**: Runs 4 unit tests written using `unittest`.
- **Docker Build & Push**:
  - Builds Docker image with tag:
    - `sumanjakhar13/weather-app:dev` (for develop branch)
    - `sumanjakhar13/weather-app:prod` (for manual prod)
  - Pushes it to Docker Hub

---

## 🐳 Docker Instructions

### Pull the Docker Image:
```bash
# For development image
docker pull sumanjakhar13/weather-app:dev

# For production image
docker pull sumanjakhar13/weather-app:prod
```

### Run the Docker Container:
```bash
docker run -it sumanjakhar13/weather-app:dev
```

---

## 🧪 Run Tests

To run tests manually:
```bash
python test_app.py
```

---

## 📦 Linting

I used `flake8` to check for code quality:
```bash
pip install flake8
flake8 .
```

---

## 📝 Notes

- I created a branch called `develop` and used it for development and auto deployments.
- The main branch is used for production. It is manually triggered using GitHub Actions.

---

Thanks for reading. This was a good learning experience for me and I learned how to set up a complete CI pipeline with multiple environments.
