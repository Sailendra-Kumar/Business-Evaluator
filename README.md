# 💼 Business Report Generator using Gemini + Streamlit

This is a simple web application built with **Streamlit** and **Google's Gemini 1.5 Flash** model that generates detailed business reports based on a user-provided **idea** and **description**.

## 🚀 Features

- Input your **business idea** and a **brief description**
- Automatically generates a structured business report including:
  - Business Overview
  - Market Research
  - Launch and Scale Plan
  - Ways to Raise Capital
- Clean and interactive UI with **Streamlit**
- Powered by **Gemini 1.5 Flash** via Google Generative AI

## 🧠 How It Works

1. The user enters a business idea and a description.
2. The app sends the prompt to the Gemini model with a system instruction for structured output.
3. The model returns a formatted business report which is displayed on the screen.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/business-report-generator.git
cd business-report-generator
```

### 2. Install Dependencies

Make sure you have Python 3.9+ and install the required libraries:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**:

```
streamlit
google-generativeai
```

### 3. Set Your Google API Key

Replace `'Your_API_Key'` in the code with your actual [Google Generative AI API key](https://makersuite.google.com/app/apikey):

```python
genai.configure(api_key='Your_API_Key')
```

Alternatively, you can use an environment variable:

```python
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

And set it in your terminal:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🖼️ App Interface

- **Title Input**: Business idea (e.g., "AI-based Personal Trainer")
- **Description Input**: A short paragraph about your idea
- **Submit Button**: Generates the business report using Gemini

## 📄 Example Prompt

```
Title: Eco-Friendly Food Delivery
Description: A delivery platform that focuses on zero-waste packaging and carbon-neutral logistics.
```

## 📦 Output Example

- **Business Overview**: ...
- **Market Research**: ...
- **Launch and Scale**: ...
- **Ways to Raise Capital**: ...

## 📌 Notes

- Make sure your API key has access to Gemini 1.5 Flash.
- Consider setting up API usage limits or error handling for production use.

## 📃 License

MIT License

---

Created with 💡 by Sailendra Kumar
