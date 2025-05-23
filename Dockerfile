# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy wait-for-it.sh
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Uvicorn
EXPOSE 5000

# Command to run your application using Uvicorn
CMD ["/bin/bash", "-c", "/app/run.sh"]
