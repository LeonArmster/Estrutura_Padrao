import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Receber um dataframe e salvar como excel

    args:
    dataframe (pd.DataFrame): Dataframe a ser salvo como excel
    output_path (Str): caminho onde salvará o arquivo
    file_name (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"

    """
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Arquivo Salvo com sucesso'
