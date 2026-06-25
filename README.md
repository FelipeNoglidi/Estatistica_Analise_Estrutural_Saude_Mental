<h1 align="center">📊 Saúde Mental de Jovens nas Redes Sociais</h1>
<p align="center">
  <strong>Trabalho de Probabilidade e Estatística</strong><br>
  Uma análise de dados sobre como o uso de telas e redes sociais afeta o bem-estar mental dos adolescentes
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/>
</p>

---

## 🎯 Sobre o Trabalho

Este projeto analisa, de forma visual e baseada em dados, como o comportamento digital de adolescentes (13–19 anos) se relaciona com indicadores de **estresse**, **ansiedade** e **depressão**.

A pergunta central que guia todo o trabalho é:

> *"Usar muito as redes sociais realmente prejudica a saúde mental dos jovens — e o que mais pode estar contribuindo para isso?"*

---

## 📦 O que está neste repositório?

```
📁 Analise-Estatistica-Saude-Mental-Jovens/
│
├── 📓 Trabalho_Estatistica.ipynb   ← O trabalho completo (abra por aqui!)
├── 🧹 limpeza_dados.py             ← Script que preparou a base de dados antes da análise
│
├── 📁 bases/
│   ├── Teen_Mental_Health_Dataset.csv   ← Base original, baixada do Kaggle
│   └── processed/
│       └── dados_limpos.csv             ← Base já tratada, usada nas análises
│
├── 📄 Trabalho___Probabilidade_e_Estatística (1).pdf  ← Enunciado do trabalho
│
└── 🎥 apresentacao_trabalho/
    └── apresentacao_trabalho_estatistica.mp4   ← Vídeo de apresentação do trabalho
```

---

## 🗂️ Estrutura do Trabalho (o que você vai encontrar no notebook)

O notebook é dividido em **4 partes**, cada uma com sua proposta:

### Parte 1 — Estatísticas Descritivas e Correlações
> *Quem são os adolescentes desta base? Quais são os números gerais?*

Aqui construímos o **perfil da amostra**: distribuições de idade, horas em redes sociais, horas de sono, nível de estresse, ansiedade e dependência digital. Também exploramos as primeiras correlações entre essas variáveis.

### Parte 2 — Análise Visual com Foco em Sono e Tela
> *O tempo de tela antes de dormir está ligado à ansiedade?*

Nesta parte investigamos, com gráficos de dispersão e barras, como o comportamento noturno (uso de tela antes de dormir) se conecta ao sono e à ansiedade dos jovens.

### Parte 3 — Grupos de Risco e Depressão
> *Quem são os jovens com maior risco de depressão?*

A parte mais reveladora do trabalho. Aqui cruzamos múltiplas variáveis ao mesmo tempo para identificar **perfis de risco**: jovens que dormem pouco **e** usam muito as redes apresentaram uma taxa de indicativo de depressão muito acima da média.

### Parte 4 — Análises Complementares
> *E quanto à idade? E o desempenho escolar? E o gênero?*

Cinco análises adicionais que fecham as lacunas: o impacto da idade, do gênero, do desempenho acadêmico e de outras combinações de fatores de risco sobre a saúde mental.

---

## 🔍 Principais Descobertas

| Achado | O que os dados mostraram |
|--------|--------------------------|
| 😴 **Sono é o fator-chave** | Dormir menos de 6h aparece nos **dois** perfis de maior risco identificados |
| 📱 **Uso intenso de redes + pouco sono** | Jovens nesse grupo têm ~22x mais chance de indicativo de depressão |
| 😰 **Estresse alto + pouco sono** | Segundo perfil de risco identificado, independente do uso de redes |
| 🌙 **Tela antes de dormir** | Associada a mais ansiedade e menos horas dormidas |
| 🎓 **Desempenho acadêmico** | Não apresentou correlação relevante com uso de redes ou sono |
| 👦👧 **Gênero e idade** | Não foram determinantes para o risco — o que importa são os **comportamentos** |

> 💡 **Conclusão central:** nenhuma variável sozinha explica o risco. O perigo aparece quando **dois ou mais fatores** se combinam no mesmo adolescente.

---

## 🎥 Apresentação em Vídeo

O vídeo com a apresentação completa do trabalho está disponível na pasta [`apresentacao_trabalho/`](./apresentacao_trabalho/apresentacao_trabalho_estatistica.mp4).

---

## ▶️ Como executar o notebook

### Opção 1 — Google Colab (recomendado, sem instalar nada)
1. Faça o upload do arquivo `Trabalho_Estatistica.ipynb` no [Google Colab](https://colab.research.google.com/)
2. Execute a primeira célula de código — ela instala tudo e baixa os dados automaticamente
3. Rode as demais células em sequência

### Opção 2 — Rodar localmente
1. Clone ou baixe este repositório
2. Execute as células do notebook em sequência — a célula de configuração instalará as dependências automaticamente

---

## 📊 Base de Dados

- **Fonte:** [Teen Mental Health Dataset — Kaggle](https://www.kaggle.com/datasets/algozee/teenager-menthal-healy)
- **Tamanho:** 1.200 registros de adolescentes (13–19 anos)
- **Variáveis principais:** idade, gênero, horas em redes sociais, horas de sono, nível de estresse, ansiedade, dependência digital, desempenho acadêmico, indicativo de depressão.
