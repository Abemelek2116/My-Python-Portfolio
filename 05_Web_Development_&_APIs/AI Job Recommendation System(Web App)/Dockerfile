# Use Python 3.11 slim
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Set Python output to unbuffered
ENV PYTHONUNBUFFERED=1

# Expose port 10000 for Render
EXPOSE 10000

# Start the app using Gunicorn
CMD ["gunicorn", "job_recommendation.wsgi:application", "--bind", "0.0.0.0:10000"]
