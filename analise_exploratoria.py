import pandas as pd
import matplotlib.pyplot as plt
import os

def configurar_estilo():
    """Aplica configurações globais de estilo para os gráficos."""
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = '#f8f9fa'
    plt.rcParams['font.family'] = 'sans-serif'

def plotar_distribuicao_tela(df, pasta_saida):
    #Gera e salva o histograma do tempo diário de redes sociais.
    plt.figure(figsize=(10, 6))
    
    plt.hist(df['daily_social_media_hours'], bins=12, color='#3498db', edgecolor='white', alpha=0.85)
    
    plt.title('Distribuição do Tempo Diário em Redes Sociais (Adolescentes)', fontsize=14, pad=15, fontweight='bold')
    plt.xlabel('Horas por Dia', fontsize=12)
    plt.ylabel('Quantidade de Jovens', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, '01_distribuicao_tempo_tela.png'), dpi=300)
    plt.close()
    print("✓ Gráfico 01 (Distribuição de Tempo) salvo com sucesso!")

def plotar_sono_vs_estresse(df, pasta_saida):
    #Gera e salva o scatter plot de Horas de Sono vs Nível de Estresse.
    plt.figure(figsize=(10, 6))
    
    plt.scatter(df['sleep_hours'], df['stress_level'], color='#9b59b6', alpha=0.6, s=50, edgecolors='none')
    
    plt.title('Correlação: Horas de Sono vs. Nível de Estresse', fontsize=14, pad=15, fontweight='bold')
    plt.xlabel('Horas de Sono por Noite', fontsize=12)
    plt.ylabel('Nível de Estresse (Escala 1-10)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, '02_sono_vs_estresse.png'), dpi=300)
    plt.close()
    print("✓ Gráfico 02 (Sono vs Estresse) salvo com sucesso!")

def main():
    # Caminhos das pastas
    ARQUIVO_DADOS = "./bases/processed/dados_limpos.csv"
    PASTA_IMAGENS = "./imagens"
    
    # Garante que a pasta para exportar os gráficos exista
    os.makedirs(PASTA_IMAGENS, exist_ok=True)
    
    try:
        # Carrega a base tratada
        df = pd.read_csv(ARQUIVO_DADOS)
        
        configurar_estilo()
        
        print(" Iniciando geração automática dos gráficos...")
        plotar_distribuicao_tela(df, PASTA_IMAGENS)
        plotar_sono_vs_estresse(df, PASTA_IMAGENS)
        
        print(f"\n Pipeline de análise concluído. Gráficos salvos em: '{PASTA_IMAGENS}'")
        
    except FileNotFoundError:
        print(f"Erro: base não encontrada '{ARQUIVO_DADOS}'.")
        print("Rode o arquivo 'limpeza_dados.py' primeiro para gerar a base tratada.")
    except Exception as e:
        print(f" Ocorreu um erro na geração dos gráficos: {e}")

if __name__ == "__main__":
    main()