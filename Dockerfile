# # Use official Python base image
# FROM python:3.11-slim

# # Set work directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy code
# COPY . .

# # Expose port (FastAPI default)
# EXPOSE 8000

# # Set environment variables (optional)
# ENV PYTHONUNBUFFERED=1

# # Run the FastAPI app
# CMD ["uvicorn", "laas_api.main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.11-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Optional: Remove test, docs, or dev files after COPY . .
RUN rm -rf tests docs .git

# If your app is pure Python, you're done!
EXPOSE 8000
CMD ["uvicorn", "laas_api.main:app", "--host", "0.0.0.0", "--port", "8000"]