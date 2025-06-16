# Weather App - CI Pipeline with GitHub Actions

This project is a simple **Weather App** built with Python. It shows current weather information based on the city name entered by the user. This repository includes a **CI pipeline** using **GitHub Actions** that builds, tests, and publishes a Docker image to Docker Hub.

---

## Repository Structure

```
weather-app/
│
├── app.py                   # Entry point for the app
├── weather.py               # Logic to call OpenWeatherMap API
├── test_weather.py          # Unit tests for the app
├── Dockerfile               # Docker build file
├── requirements.txt         # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml           # GitHub Actions CI workflow
```

---

## How to Build and Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

City name field is prompted here. The app will fetch and display the weather.

---

## How to Test the CI Pipeline

1. `.github/workflows/ci.yml` — this file contains the pipeline steps.
2. When we **push code or create a pull request**, GitHub Actions will:
   - Install dependencies
   - Run unit tests (4 tests must pass)
   - Build a Docker image
   - ⬆Push it to Docker Hub

### You can view the pipeline status under the "Actions" tab in the repository.

---

## Pull the Docker Image (Optional)

If we want to run the Docker image:

```bash
docker pull sumanjakhar13/weather-app:latest

docker run -it sumanjakhar13/weather-app
```

---

## Jenkins Pipeline (If Applicable)

If you implemented Jenkins as a bonus:

- The Jenkinsfile is in the root directory.
- It includes the same stages: Build, Test, and Docker Upload.
- Make sure Jenkins is connected to your GitHub repo and Docker is installed on the Jenkins server.

To run:
1. Push code changes to GitHub
2. Jenkins will auto-trigger the pipeline or run it manually from the Jenkins UI

---

## Author

Created by Suman Kumari Jakhar
