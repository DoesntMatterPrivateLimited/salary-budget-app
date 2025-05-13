# Salary Budget Planner (with Chart UI)

A Flask web app to help users plan their monthly budget based on salary input. It categorizes expenses and shows a pie chart visualization.

## Features

- Dynamic budget allocation based on salary range
- Switch-case style logic for clean code
- Pie chart visual showing budget distribution
- Dockerized for easy deployment

## Run with Docker

```bash
docker build -t salary-budget-app .
docker run -p 5000:5000 salary-budget-app
