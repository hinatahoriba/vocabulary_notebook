from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# データベースのベースクラスを生成
Base = declarative_base()

# WordListテーブルのモデル
class WordList(Base):
    __tablename__ = "WordList"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Japanese = Column(String, unique=True)
    English = Column(String)