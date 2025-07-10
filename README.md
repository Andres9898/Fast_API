# FarmAmigo Backend

FarmAmigo is a supplier portal for agricultural products.

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database
- AWS account for S3 and Cognito
- Email server for sending emails

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/farmamigo_backend.git
   cd farmamigo_backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edit .env with your actual values

flask db init
flask db migrate
flask db upgrade

python run.py



this project is for create for backend to Image Models input IA

## Technology Stack

Tecnologies used in the project (including cloud platform)

1. Ubuntu
1. Docker
1. Python
    * [FastAPI](https://fastapi.tiangolo.com)

## Project Structure

```

```

## Environment Variable




### Quick Start

1.  Build and Run python app container
    1.  Build insided the folder [src](./src/) with the command:
        ```bash
        docker build . -t python-2
        ```
    1.  Run the Container App:
        *   For interactive terminal session with the host local files (for modification and test in real team, not need re-build) run
            Linux
            ```bash
            $ docker run -it --rm --name=backend-2 -p 5000:5000 -v $(pwd):"/home/realtime" python-2 bash
            ```


            or

            ```bash
            $ docker run -it \
                --rm \
                --name backend \
                -p 5000:5000 \
                -v $(pwd):"/home/realtime" \
                python-2 bash
            ```
            For run the application inside the terminal run:

            ```bash
            cd realtime/src/ 
            uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
            ```

        *   For non interactive run

            ```bash
            docker run --rm -d --name=backend -p 8000:8000 python-2
            ```

        flags:

        * `--rm`&nbsp;&nbsp;&nbsp;&nbsp;    Erase the docker after stop
        * `-d`&nbsp;&nbsp;&nbsp;&nbsp;      Run container in background and print container ID
        * `-it`&nbsp;&nbsp;&nbsp;&nbsp;      Interactive session
        * `--name`&nbsp;&nbsp;&nbsp;&nbsp;   Containers name
        * `-p`&nbsp;&nbsp;&nbsp;&nbsp;       Publish a container's port(s) to the host (e.g., `-p <host port>:<container port>`)


        more information flags in [docker container run options](https://docs.docker.com/reference/cli/docker/container/run/#options)

<!-- Bibliografy -->
[1]: https://example          "example documentation"
[2]: https://pjreddie.com/darknet/yolo/ "YOLO: Real-Time Object Detection"
