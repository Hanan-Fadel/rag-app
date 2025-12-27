# RAG Application

A Retrieval Augmented Generation (RAG) application built with FastAPI for processing and chunking documents for vector storage and retrieval.

## Features

- 📄 **Document Upload**: Upload and manage documents (PDF, TXT) for processing
- 🔪 **Text Chunking**: Split documents into chunks with configurable size and overlap
- 💾 **MongoDB Storage**: Store processed chunks and metadata in MongoDB
- 🔄 **Project Management**: Organize documents by projects with automatic project creation
- ⚡ **Async API**: Built with FastAPI for high-performance async operations

## Technology Stack

- **Framework**: FastAPI
- **Database**: MongoDB (via Motor/Motor Async)
- **Language**: Python 3.11+
- **Document Processing**: LangChain
- **File Handling**: aiofiles, PyMuPDF

## Prerequisites

- Python 3.11 or higher
- MongoDB 8.2+ (can be run via Docker Compose)
- pip package manager

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rag-app
```

### 2. Set Up Python Environment

You can use any Python environment manager (conda, pyenv, venv):

**Using venv (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Using conda:**
```bash
conda create -n rag-app python=3.11
conda activate rag-app
```

### 3. Install Dependencies

```bash
cd src
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
APP_NAME=RAG Application
APP_VERSION=1.0.0
OPEN_API_KEY=your_openai_api_key_here

FILE_ALLOWED_TYPES=["pdf", "txt"]
FILE_MAX_SIZE=10485760
FILE_DEFAULT_CHUNK_SIZE=8192

MONGODB_URL=mongodb://localhost:27017
MONGODB_DATABASE=rag_db
```

### 5. Start MongoDB (Docker Compose)

```bash
cd ../docker
cp .env.example .env  # Configure MongoDB credentials if needed
docker-compose up -d
```

### 6. Run the Application

From the `src` directory:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

The API will be available at:
- API: http://localhost:5000
- Interactive API docs: http://localhost:5000/docs
- Alternative API docs: http://localhost:5000/redoc

## API Endpoints

### Base

- `GET /api/v1/` - Get application info (name and version)

### Data

- `POST /api/v1/data/upload/{project_id}` - Upload a document for a project
  - **Path Parameters**: `project_id` (string)
  - **Body**: multipart/form-data with `file` field
  - **Response**: File upload confirmation with `file_id`

- `POST /api/v1/data/process/{project_id}` - Process an uploaded file into chunks
  - **Path Parameters**: `project_id` (string)
  - **Body**:
    ```json
    {
      "file_id": "string",
      "chunk_size": 100,
      "overlap_size": 20,
      "do_reset": 0
    }
    ```
  - **Response**: Processing confirmation with number of inserted chunks

## Project Structure

```
rag-app/
├── src/
│   ├── controllers/          # Business logic controllers
│   ├── helpers/              # Configuration and utilities
│   ├── models/               # Database models and schemas
│   ├── routes/               # API route handlers
│   ├── assets/               # Uploaded files storage
│   ├── main.py               # FastAPI application entry point
│   └── requirements.txt      # Python dependencies
├── docker/
│   ├── docker-compose.yml    # MongoDB service configuration
│   └── .env.example          # Docker environment variables template
├── LICENSE
└── README.md
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `APP_NAME` | Application name | Yes |
| `APP_VERSION` | Application version | Yes |
| `OPEN_API_KEY` | OpenAI API key | Yes |
| `FILE_ALLOWED_TYPES` | List of allowed file extensions | Yes |
| `FILE_MAX_SIZE` | Maximum file size in bytes | Yes |
| `FILE_DEFAULT_CHUNK_SIZE` | Default chunk size for file reading | Yes |
| `MONGODB_URL` | MongoDB connection string | Yes |
| `MONGODB_DATABASE` | Database name | Yes |

## Development

### Running with Hot Reload

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

### MongoDB Connection

The application connects to MongoDB using the connection string specified in `MONGODB_URL`. Make sure MongoDB is running before starting the application.

Default connection (local): `mongodb://localhost:27017`

## Docker Management

### Stop All Working Containers

To stop all running containers:

```bash
cd docker
docker-compose down
```

Or stop all Docker containers system-wide:

```bash
docker stop $(docker ps -q)
```

### Remove All Stopped Containers

To remove all stopped containers:

```bash
cd docker
docker-compose down --remove-orphans
```

Or remove all stopped containers system-wide:

```bash
docker container prune -f
```

### Remove Downloaded Images

To remove images used by this project:

```bash
cd docker
docker-compose down --rmi all
```

Or remove all unused images system-wide:

```bash
docker image prune -a -f
```

### Remove All Volumes

To remove volumes for this project (⚠️ **WARNING**: This will delete all MongoDB data):

```bash
cd docker
docker-compose down -v
```

Or remove all unused volumes system-wide:

```bash
docker volume prune -f
```

### Complete Cleanup (All Steps Combined)

To stop containers, remove containers, images, and volumes in one command:

```bash
cd docker
docker-compose down -v --rmi all --remove-orphans
```

Or perform each step individually:

```bash
cd docker

# 1. Stop all working containers
docker-compose down

# 2. Remove all stopped containers
docker-compose down --remove-orphans

# 3. Remove downloaded images
docker-compose down --rmi all

# 4. Remove all volumes (⚠️ WARNING: deletes all data)
docker-compose down -v
```

### Start Fresh

To start with a completely clean state:

```bash
cd docker

# Stop and remove everything
docker-compose down -v --rmi all --remove-orphans

# Start fresh
docker-compose up -d
```

### Useful Docker Commands

```bash
# View running containers
docker-compose ps

# View logs
docker-compose logs -f

# View MongoDB logs specifically
docker-compose logs -f mongodb

# Restart services
docker-compose restart

# View container status
docker ps -a
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

For more information, visit the interactive API documentation at http://localhost:5000/docs when the server is running.
