from fastapi import FastAPI, Depends
from laas_api.dependencies import verify_api_key


from laas_api.schemas import (
    TextRequest, TokenizeResponse, LemmatizeRequest, LemmatizeResponse,
    ImageResizeRequest, ImageResizeResponse,
    SentimentRequest, SentimentResponse
)
from text_image_toolkit.text import SimpleTokenizer, simple_lemmatizer
from text_image_toolkit.image import ImageResizer
from text_image_toolkit.nlp import SentimentAnalyzer

app = FastAPI(
    title="Text & Image Toolkit API", 
    version="1.0",
    dependencies=[Depends(verify_api_key)]
)

@app.post("/tokenize", response_model=TokenizeResponse)
def tokenize(req: TextRequest):
    tokenizer = SimpleTokenizer()
    tokens = tokenizer.process(req.text)
    return TokenizeResponse(tokens=tokens)

@app.post("/lemmatize", response_model=LemmatizeResponse)
def lemmatize(req: LemmatizeRequest):
    lemma = simple_lemmatizer(req.word)
    return LemmatizeResponse(lemma=lemma)

@app.post("/image/resize", response_model=ImageResizeResponse)
def image_resize(req: ImageResizeRequest):
    resizer = ImageResizer()
    result = resizer.resize(req.image, req.size)
    return ImageResizeResponse(result=result)

@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(req: SentimentRequest):
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze(req.text)
    return SentimentResponse(sentiment=sentiment)