FROM python:3.11.5

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

# Run the Flask app in the container
CMD ["python", "retail_price_app.py"]