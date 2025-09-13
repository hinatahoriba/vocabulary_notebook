from pydantic import BaseModel

# 単語帳の日本語の追加時に使用するスキーマ
class Japanese(BaseModel):
    Japanese: str

# 単語帳の取得時に使用するスキーマ
class Word(BaseModel):
    id: int
    Japanese: str
    English: str

    # SQLAlchemyモデルからインスタンスを作成するための設定
    class Config:
        orm_mode = True