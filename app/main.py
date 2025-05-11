from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframe

if __name__ == '__main__':
    df_list = extract_from_excel(
        r'C:\Users\Uso Pessoal\desktop\estudos\jornada_dados\estrutura_projeto\data'
    )
    df = concat_dataframe(df_list)
    load_excel(
        df,
        r'C:\Users\Uso Pessoal\desktop\estudos\jornada_dados\estrutura_projeto\data\output',
        'output',
    )
