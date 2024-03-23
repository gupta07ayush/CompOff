# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install Flask gunicorn

# Copy all files from the current directory into the container
COPY . .

# Expose the port that your app runs on
EXPOSE 5000

# Set the WEBSITES_PORT environment variable
ENV WEBSITES_PORT=5000

# Command to run the Flask application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
