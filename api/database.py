from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# データベースファイルのパス
DATABASE_URL = "sqlite:///./db/wordlist.db"

# データベースエンジンを作成
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# セッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルのベースクラスを作成
Base = declarative_base()

# データベースセッションを生成する依存性注入用の関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()