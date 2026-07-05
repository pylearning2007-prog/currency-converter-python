# 💱 Currency Converter

A simple Currency Converter built with **Python** and the **ExchangeRate API**. This application converts currencies using live exchange rates and saves the conversion history to a text file.

## ✨ Features

* 🌍 Convert one currency to another
* 📡 Uses live exchange rates from ExchangeRate API
* ✅ Validates currency codes
* 🔢 Validates user input
* 🌐 Handles internet connection errors
* 💾 Saves conversion history to a text file

## 🛠️ Requirements

* Python 3.x
* requests library

Install the required library:

```bash
pip install requests
```

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/pylearning2007-prog/currency-converter-python.git
```

2. Open the project folder:

```bash
cd currency-converter-python
```

3. Open `currency_converter.py` and replace:

```python
api_key = "YOUR_API_KEY"
```

with your own ExchangeRate API key.

4. Run the program:

```bash
python currency_converter.py
```

## 📂 Project Structure

```
currency-converter-python/
│── currency_converter.py
│── README.md
│── requirements.txt
│── .gitignore
```

## 💻 Sample Output

```text
Enter From currency : INR
Enter To currency : USD
Enter the amount : 100

100.00 INR = 1.17 USD
```

## 📚 Technologies Used

* Python
* Requests Library
* ExchangeRate API

## 👨‍💻 Author

**PY**

GitHub: https://github.com/pylearning2007-prog
