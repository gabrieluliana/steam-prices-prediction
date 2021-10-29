import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import scipy as sp
from datetime import datetime
       

STEAMGAMEDATA_ATTRIBUTES = [
            "Nome",
            "Desenvolvedor",
            "Distribuidora",
            "Quantidade de review",
            "Review médio",
            "Plataforma",
            "SinglePlayer",
            "Multiplayer",
            "Data de lançamento",
            "Linguagens Interface",
            "Linguagens Dublagem",
            "Linguagens Legenda",
            "Processador",
            "Memória Ram",
            "Placa de Vídeo",
            "Espaço em Disco",
            "Preço"
        ]



class SteamGameData:

    def __init__(self, filename: str):
        """
        Args:
            filename (str, optional): [path para o csv dos dados dos jogos da steam]. Defaults to None.
        """
        self.raw_df = None
        self.df = None

        if filename:
            self.raw_df = self.load_from_file(filename)
        else:
            self.raw_df = self.init_dataframe()


    def load_from_file(self, csv_file: str):
        try:
            df = pd.read_csv(csv_file, na_values='?')
            return df
        except Exception as e:
            print(e)
            return 

    def init_dataframe(self) -> (list(), pd.DataFrame):
        """Inicializacao do dataframe de jogos da Steam

        atributos:

            Nome : Categorico
            Desenvolvedor: Categorico
            Distribuidora: Distribuidora
            Quantidade de review: Numerico
            Review médio: Categorico
            Plataforma: Categorico:
            Multiplayer: Categorico
            Data de lançamento: Numerico
            Linguagens Interface: Numerico
            Linguagens Dublagem: Numerico
            Linguagens Legenda: Numerico
            Processador: Categorico
            Memória Ram: Numerico
            Placa de Vídeo: Categorico
            Espaço em Disco: Numerico
            Preco: Numerico
        """

        return pd.DataFrame(columns=STEAMGAMEDATA_ATTRIBUTES)

    def process_attributes(self):
        try:
            self.df = self.raw_df.copy()
            self._process_price()
            self._rank_attr("Desenvolvedor", num_to_be_ranked=100)
            self._rank_attr("Distribuidora", num_to_be_ranked=100)
            self._process_release_date(2)
            self._process_review()
        except Exception as e:
            print(e)

    def _process_price(self, high_price: float=45, low_price: float=18.00):
        """ Organiza precos em alto, medio em barato

        Args:
            high_price float: [description]. Defaults to 120.00.
            low_price float: [description]. Defaults to 15.00.


        """
        def _classify_price(price: str):
            price = price.replace(',','.')
            print(price)
            try:
                if float(price) >= high_price:
                    return 'Alto'
                elif float(price) <= low_price:
                    return 'Baixo'
                else:
                    return 'Médio'
            except:
                return price
        self.df['Preço'] = self.raw_df['Preço'].apply(_classify_price)
        return

    def _process_review(self):
        """ Organiza precos em alto, medio em barato

        Args:
            high_price float: [description]. Defaults to 120.00.
            low_price float: [description]. Defaults to 15.00.


        """
        def _not_enough_review(review: str):
            if review[0].isdigit():
                return "poucos reviews"
            else:
                return review
        self.df['Review Médio'] = self.raw_df['Review Médio'].apply(_not_enough_review)
        return
     
    
    def _rank_attr(self, attribute: str, num_to_be_ranked: int=5):
        """Rankeia as empresas que mais sao frequentes, restante entra na categoria outros


        Args:
            attribute (str): name of attribute to be ranked
            num_to_be_ranked (int): . Defaults to 10.
        """
        def ignore_not_ranked(most_frequently: [str]):
            def _ignore_not_ranked(value: str):
                if value not in most_frequently:
                    return "Outros"
                else:
                    return value
            return _ignore_not_ranked

        most_frequently = self.df[attribute].value_counts()[:num_to_be_ranked].index.tolist()
        func = ignore_not_ranked(most_frequently)
        self.df[attribute] = self.raw_df[attribute].apply(func)


    def _process_release_date(self, olderthan: int=2):
        """Transforma data de lancamento  para categoria "LANCAMENTO" ou "ANTIGO" dado uma entrada em meses

        Args:
            olderthan (int): [quantidade de meses pra o jogo ser considerado lancamento ou nao]. Defaults to 24.
        """

        def old_or_new(release_date: str):
            year = int(release_date[-4:])
            if year <= datetime.today().year - olderthan:
                return "antigo"
            else:
                return "novo"
            
        self.df['Data de Lançamento'] = self.raw_df['Data de Lançamento'].apply(old_or_new)


    @property
    def attributes(self):
        try:
            return list(self.df.columns.values)
        except Exception as e:
            print(e)
            return None

    @property
    def raw_attributes(self):
        return list(self.raw_df.columns.values)

    @property
    def column(self, attribute):
        try:
            return self.df[attribute]
        except Exception as e:
            print(e)
            return None


