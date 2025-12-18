# 1. Base image (Python installed)
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirments.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirments.txt

# 5. Copy project code
COPY . .

# 6. Expose port 8000
EXPOSE 8000

# 7. Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
