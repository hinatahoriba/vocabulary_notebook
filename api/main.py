from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, translate
from .database import engine, get_db

# データベースのテーブルを作成
models.Base.metadata.create_all(bind=engine)

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

@app.get("/words/")
def get_words(db: Session = Depends(get_db)):
    """
    単語を全て取得します。
    """
    words = db.query(models.WordList).all()
    return words

@app.post("/word/", response_model=schemas.Word)
def create_todo(Japanese: schemas.Japanese, db: Session = Depends(get_db)):
    """
    新しい単語を追加します。
    """
    db_word= models.WordList(Japanese=Japanese.Japanese, English = translate.translate_japanese_to_english(Japanese.Japanese))
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word