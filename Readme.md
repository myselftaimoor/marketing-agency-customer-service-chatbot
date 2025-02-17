# Digipex Solutions Chatbot

This is a chatbot built with Flask, providing responses to frequently asked questions (FAQ) using Natural Language Processing (NLP) and machine learning models like TF-IDF and KNN. The chatbot is designed to assist users with inquiries related to Digipex Solutions' services and portfolios, such as video editing, website designing, graphic designing, and mobile application development.

## Features

- **FAQ Matching:** The chatbot uses a combination of fuzzy matching and TF-IDF with KNN to provide relevant responses.
- **Flask API:** The application is served via Flask, making it easy to integrate with web applications.
- **Gunicorn Support:** Designed for production deployment with Gunicorn for better performance and scalability.

## Prerequisites

Before running this application, ensure that you have the following installed:

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/digipex-chatbot.git
   cd digipex-chatbot

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure the FAQ CSV file (```FAQ.csv```) is located in the root of the project directory.

## Running Locally
To deploy in production, we recommend using Gunicorn. Follow these steps:

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run the application using Gunicorn:
   ```bash
   gunicorn app:app
   ```

3. The app will now be served on port 8000 by default.

## API Endpoint

### POST `/chatbot`

Send a JSON request to the `/chatbot` endpoint to get a response from the chatbot.

#### Request Body

```json
{
  "query": "Can I see your video editing portfolio?"
}
```
#### Response Body:

```json
{
  "query": "Can I see your video editing portfolio?",
  "answer": "You can explore our video editing and production portfolio here: https://digipexsolutions.com/video-editing/"
}
```

#### Error Responses
- 400 Bad Request: Invalid or missing query in the request.
- 500 Internal Server Error: If an error occurs while processing the request.

## Deployment on Render

1. Sign up or log in to Render.
2. Click **New Web Service** and select your GitHub or GitLab repository.
3. Render will automatically detect the Python environment and install dependencies from `requirements.txt`.
4. Set the **Start Command** as:

    ```bash
    gunicorn app:app
    ```

5. After deployment, you can access your live chatbot API.

## Files and Directories

- **app.py**: The main Flask application file.
- **FAQ.csv**: The CSV file containing frequently asked questions and answers.
- **Procfile**: Specifies how the application should be run (for Render).
- **requirements.txt**: Lists all dependencies for the project.
- **README.md**: Project documentation (this file).

## Dependencies

The project requires the following Python libraries:

- Flask
- pandas
- nltk
- scikit-learn
- fuzzywuzzy
- gunicorn

You can install these dependencies using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project uses:

- **Flask** for building the API.
- **pandas** for handling FAQ data.
- **nltk** for text processing.
- **scikit-learn** for machine learning and natural language processing.
- **fuzzywuzzy** for fuzzy string matching.

## Author
Muhammad Taimoor Khan (Data Scientist & COO, Digipex Solutions)

![Digipex Solutions Logo](https://digipexsolutions.com/))












