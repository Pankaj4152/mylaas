from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class TokenizeResponse(BaseModel):
    tokens: list[str]

class LemmatizeRequest(BaseModel):
    word: str

class LemmatizeResponse(BaseModel):
    lemma: str

class ImageResizeRequest(BaseModel):
    image: str  # For demo: image path or dummy string
    size: tuple[int, int]

class ImageResizeResponse(BaseModel):
    result: str

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str