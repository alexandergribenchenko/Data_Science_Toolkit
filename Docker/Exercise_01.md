# Exercise 01.

# Dockerfile: 

FROM 

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY print.py ./

CMD ["python3, "./print.py"]


# Python file
print(





https://www.youtube.com/watch?v=uvTl6GefR9o&list=PLrJvjnSL5aF7YtpEFzc6qdLt7y0BdJVyY&index=9