# Text & Image Toolkit API

A modular Python library and FastAPI microservice for basic text and image preprocessing tasks, including tokenization, lemmatization, sentiment analysis, and simple image operations.

---

## Features

- **Text Processing:** Tokenization, lemmatization, punctuation removal
- **NLP:** Simple sentiment analysis, named entity recognition (NER)
- **Image Processing:** Dummy image resizing and filtering
- **REST API:** FastAPI-powered endpoints for all features, with API key authentication

---

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd "AIP Library"
pip install -r requirements.txt
```

Or install as a package:

```bash
pip install .
```

---

## Usage as a Python Library

```python
from text_image_toolkit.text import SimpleTokenizer, simple_lemmatizer, remove_punctuation
from text_image_toolkit.image import ImageResizer, ImageFilter
from text_image_toolkit.nlp import SentimentAnalyzer, NERTagger

# Text
tokenizer = SimpleTokenizer()
print(tokenizer.process("Hello World!"))  # ['Hello', 'World!']

print(simple_lemmatizer("cars"))  # car

print(remove_punctuation("Hello, world!"))  # Hello world

# Image
resizer = ImageResizer()
print(resizer.resize("img", (100, 100)))  # Resized image to (100, 100)

filt = ImageFilter()
print(filt.blur("img"))  # Blurred: img

# NLP
sent = SentimentAnalyzer()
print(sent.analyze("This is good!"))  # positive

ner = NERTagger()
print(ner.tag("Alice went to Paris"))  # [('Alice', 'ENTITY'), ('Paris', 'ENTITY')]
```

---

## Usage as an API

### Run the API locally

```bash
uvicorn laas_api.main:app --reload
```

### Docker

Build and run with Docker:

```bash
docker build -t text-image-toolkit-api .
docker run -p 8000:8000 text-image-toolkit-api
```

### API Authentication

All endpoints require an API key via the `x-api-key` header.  
Default key: `supersecret` (set `API_KEY` env variable in production).

### Example API Call

```bash
curl -X POST "http://localhost:8000/tokenize" ^
  -H "Content-Type: application/json" ^
  -H "x-api-key: supersecret" ^
  -d "{\"text\": \"Hello Docker\"}"
```

### Interactive Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## API Endpoints

- `POST /tokenize` — Tokenize text
- `POST /lemmatize` — Lemmatize a word
- `POST /image/resize` — Resize an image (dummy)
- `POST /sentiment` — Sentiment analysis

---

## Testing

```bash
pytest tests/
```

---

## Project Structure

```
AIP Library/
├── laas_api/           # FastAPI app and API schemas
├── text_image_toolkit/ # Core library modules
├── tests/              # Unit tests
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## License

MIT License

---