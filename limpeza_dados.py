import pandas as pd
import os

def carregar_dados(caminho_arquivo):
    
    print(f"Carregando os dados de: {caminho_arquivo}")
    return pd.read_csv(caminho_arquivo)

def inspecionar_dados(df):
    # Para exibir informações básicas sobre a estrutura do DataFrame
    print("\n--- Inspeção Inicial ---")
    print(f"Total de registros (linhas): {df.shape[0]}")
    print(f"Total de variáveis (colunas): {df.shape[1]}")
    
    print("\n Tipos de dados e valores nulos por coluna:")
    print(df.info())
    
    # Verifica se há valores nulos explicitamente
    nulos = df.isnull().sum()
    if nulos.sum() == 0:
        print("\n Nenhum valor nulo encontrado na base")
    else:
        print("\n Valores nulos encontrados:")
        print(nulos[nulos > 0])

def executar_limpeza(df):
    #Aplica os tratamentos de limpeza e padronização nos dados
    print("\n Iniciando a limpeza dos dados...")
    
    # 1. Remover linhas completamente duplicadas (boa prática sempre)
    linhas_antes = df.shape[0]
    df = df.drop_duplicates()
    linhas_depois = df.shape[0]
    if linhas_antes != linhas_depois:
        print(f" Removidas {linhas_antes - linhas_depois} linhas duplicadas.")
    else:
        print(" Nenhuma linha duplicada encontrada.")
        
    # 2. Padronizar textos (remover espaços em branco invisíveis nas pontas)
    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].str.strip()
    print(" Textos das colunas categóricas padronizados.")
    
    # 3. Tratar nulos (Considerando que o dataset tenha nulos, podemos preencher ou dropar)
    df = df.dropna()
    
    return df

def main():
    # Caminhos essênciais 
    ARQUIVO_ORIGEM = "./bases/Teen_Mental_Health_Dataset.csv"
    PASTA_DESTINO = "./bases/processed"
    ARQUIVO_DESTINO = os.path.join(PASTA_DESTINO, "dados_limpos.csv")
    
    try:
        # Executa o pipeline de limpeza
        df_bruto = carregar_dados(ARQUIVO_ORIGEM)
        inspecionar_dados(df_bruto)
        
        df_limpo = executar_limpeza(df_bruto)
        
        # Garante que a pasta processed existe antes de salvar
        os.makedirs(PASTA_DESTINO, exist_ok=True)
        df_limpo.to_csv(ARQUIVO_DESTINO, index=False)
        
        print(f"\nSucesso! Dados limpos e salvos em: {ARQUIVO_DESTINO}")
        print(f"Formato final da base: {df_limpo.shape[0]} linhas e {df_limpo.shape[1]} colunas.")
        
    except FileNotFoundError:
        print(f"\n Erro: Arquivo de origem não encontrado {ARQUIVO_ORIGEM}.")
        print("Verifique se o nome do arquivo na pasta './bases' está exatamente igual.")
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()