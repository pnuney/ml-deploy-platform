FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed
RUN pip install --no-cache-dir --upgrade pip

# Copy app code and install dependencies
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]