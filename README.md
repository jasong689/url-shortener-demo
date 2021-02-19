## URL Shortener Demo

Running this project requires Docker

1. Clone the repository
2. Create an .env file containing `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `SECRET_KEY` variables
3. Run `docker-compose up`

The webserver listens on localhost:8080. To generate a new short url navigate to http://localhost:8080/form/ or to generate a short url with a custom short code navigate to http://localhost:8080/form-custom/

Navigating to any valid short url (http://localhost:8080/short_code) will redirect you to the original url
