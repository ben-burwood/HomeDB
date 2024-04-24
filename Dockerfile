FROM python

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Copy Project to Docker Directory
COPY . .

# Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Django App Port
EXPOSE 8000

# Start Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]