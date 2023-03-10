from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass

class Game(Base):
    __tablename__ = 'roblox_game'

    id: Mapped[int] = mapped_column(primary_key=True)
    group: Mapped[str]
    title: Mapped[str]
    active_players: Mapped[int]
    total_up_votes: Mapped[int]
    total_down_votes: Mapped[int]
    description: Mapped[Optional[str]]
