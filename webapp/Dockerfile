FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask

# Copy the entire app directory to the container
COPY . /srv

# Set the working directory to /srv
WORKDIR /srv

# Set the FLASK_APP environment variable
ENV FLASK_APP=app

# Expose the Flask app on port 5000
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
