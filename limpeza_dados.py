import pandas as pd
import os

def carregar_dados(caminho_arquivo):
    """Carrega o dataset a partir do caminho especificado."""
    print(f"Carregando os dados de: {caminho_arquivo}")
    return pd.read_csv(caminho_arquivo)

def inspecionar_dados(df):
    """
    Realiza uma inspeção inicial na estrutura do DataFrame.
    Justificativa: Esta etapa é essencial na Análise Exploratória de Dados (EDA) 
    para compreender as dimensões da base e os tipos de dados contidos, além de 
    fornecer a primeira visão sobre a presença de valores nulos (missing values).
    """
    print("\n--- Inspeção Inicial ---")
    print(f"Total de registros (linhas): {df.shape[0]}")
    print(f"Total de variáveis (colunas): {df.shape[1]}")
    
    print("\n Tipos de dados e valores nulos por coluna:")
    print(df.info())
    
    # Verifica se há valores nulos explicitamente
    nulos = df.isnull().sum()
    if nulos.sum() == 0:
        print("\n[V] Validação: Nenhum valor nulo encontrado na base.")
    else:
        print("\n[!] Valores nulos encontrados:")
        print(nulos[nulos > 0])

def executar_limpeza(df):
    """
    Aplica os tratamentos de limpeza, padronização e validação nos dados.
    Justificativa Geral: A etapa de limpeza garante a integridade dos dados,
    evitando que outliers, registros duplicados ou valores fora do escopo lógico 
    (ex: idades impossíveis) distorçam os resultados das análises estatísticas.
    """
    print("\n--- Iniciando a limpeza e validação dos dados ---")
    
    # 1. Remoção de duplicatas
    # Justificativa: Linhas idênticas podem representar envios duplicados de formulários,
    # o que daria peso em dobro para um mesmo indivíduo, enviesando médias e agregações.
    linhas_antes = df.shape[0]
    df = df.drop_duplicates()
    linhas_depois = df.shape[0]
    if linhas_antes != linhas_depois:
        print(f"[-] Removidas {linhas_antes - linhas_depois} linhas duplicadas.")
    else:
        print("[V] Duplicatas: Nenhuma linha duplicada encontrada.")
        
    # 2. Padronização de strings
    # Justificativa: Variáveis categóricas como "Male " e "Male" são tratadas como distintas 
    # pela máquina. O strip remove espaços em branco invisíveis nas extremidades, garantindo 
    # o agrupamento correto em funções como groupby.
    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].str.strip()
    print("[V] Padronização: Textos das colunas categóricas foram padronizados (strip aplicados).")
    
    # 3. Tratamento de nulos
    # Justificativa: Modelos estatísticos e certas plotagens falham ao encontrar valores nulos.
    # Neste caso, como optamos pela exclusão (dropna), garantimos análises pareadas corretas.
    nulos_antes = df.shape[0]
    df = df.dropna()
    nulos_depois = df.shape[0]
    if nulos_antes != nulos_depois:
        print(f"[-] Removidas {nulos_antes - nulos_depois} linhas com valores nulos.")
    else:
        print("[V] Nulos: Nenhum valor nulo estava presente para ser removido.")

    # 4. Verificação Lógica de Domínio (Integridade)
    # Justificativa: Mesmo sem nulos, os dados podem conter anomalias lógicas resultantes de
    # erros de digitação (ex: idade = 150). Validar limites físicos/lógicos garante a veracidade.
    print("\n--- Verificação de Integridade (Ranges Lógicos) ---")
    
    erros_dominio = 0
    # Checagem de Idade (dataset é sobre adolescentes)
    if not df['age'].between(10, 25).all():
        print("[!] Alerta: Existem idades fora do range esperado para adolescentes (10-25).")
        erros_dominio += 1
    
    # Checagem das escalas de saúde mental (devem estar entre 1 e 10)
    escalas = ['stress_level', 'anxiety_level', 'addiction_level']
    for escala in escalas:
        if not df[escala].between(1, 10).all():
            print(f"[!] Alerta: A coluna {escala} possui valores fora da escala 1 a 10.")
            erros_dominio += 1
            
    # Checagem de Depressão (deve ser binário 0 ou 1)
    if not df['depression_label'].isin([0, 1]).all():
        print("[!] Alerta: A coluna depression_label possui valores diferentes de 0 e 1.")
        erros_dominio += 1
        
    if erros_dominio == 0:
        print("[V] Integridade: Todas as variáveis numéricas respeitam seus domínios lógicos restritos.")
    
    return df

def main():
    # Caminhos essenciais 
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
        
        print(f"\nSucesso! Dados validados e salvos em: {ARQUIVO_DESTINO}")
        print(f"Formato final da base de análise: {df_limpo.shape[0]} linhas e {df_limpo.shape[1]} colunas.")
        
    except FileNotFoundError:
        print(f"\n Erro: Arquivo de origem não encontrado {ARQUIVO_ORIGEM}.")
        print("Verifique se o nome do arquivo na pasta './bases' está exatamente igual.")
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()