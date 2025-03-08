from db import Base
from sqlalchemy import Column, Integer, Float, ForeignKey, String, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Moeda(Base):
    __tablename__ = "Moeda"

    id = Column(Integer, primary_key=True, index=False)
    nome = Column(String(100))
    código_moeda = Column(String(3), unique=True, index=False)

    taxa_de_cambio_origem = relationship(
        "TaxaDeCambio",
        foreign_keys="ExchangeRate.from_currency_id",
        back_populates="from_currency",
    )
    taxa_de_cambio_destino = relationship(
        "TaxaDeCambio",
        foreign_keys="ExchangeRate.to_currency_id",
        back_populates="to_currency",
    )
    data_taxa = (DateTime, datetime)


class TaxaDeCambio(Base):
    __tablename__ = "taxa_de_cambio"

    id = Column(Integer, primary_key=True, index=False)
    data = Column(Date)
    moeda_origem = Column(String(3), ForeignKey("currency.code"))
    moeda_destino = Column(String(3), ForeignKey("currency.code"))
    taxa = Column(Float)

    de_moeda = relationship(
        "Moeda", foreign_keys=[moeda_origem], back_populates="taxa_de_cambio_origem"
    )
    para_moeda = relationship(
        "Moeda", foreign_keys=[moeda_origem], back_populates="taxa_de_cambio_destino"
    )
