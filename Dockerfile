# Use the official Python image as the base image
FROM python:3.9-slim

# Install system dependencies (including Nmap)
RUN apt-get update && apt-get install -y \
    nmap \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker's caching for dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["fastapi", "run", "scanner/main.py"]