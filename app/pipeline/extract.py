# Bibliotecas
import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas

import pandas as pd  # biblioteca para trabalhar arquivos


def extract_from_excel(path: str) -> pd.DataFrame:
    """
    Função para ler os arquivos de uma pasta e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """

    lista_arquivo = glob.glob(os.path.join(path, '*x.xlsx'))
    df_list = []

    for arquivo in lista_arquivo:
        df_list.append(pd.read_excel(arquivo, engine='openpyxl'))

    # df = pd.concat(df_list)

    return df_list


if __name__ == '__main__':
    path = r'C:\Users\Uso Pessoal\desktop\estudos\jornada_dados\estrutura_projeto\data'
    df = extract_from_excel(path=path)
    print('hello word')
    print(df)
