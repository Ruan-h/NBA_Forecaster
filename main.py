import csv
import numpy as np
import scipy.stats as st
from scipy.stats import t, norm
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



data = """
1	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/12/2025
2024-25
OKCOKC
@
WASWAS
12
12
2
1
1
0
3
6
50.0
1
1
100.0
5
5
100.0
73.2
1
1
0
1
+12
2	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/10/2025
2024-25
OKCOKC
@
NYKNYK
12
13
3
0
0
0
5
8
62.5
0
0
0
3
3
100.0
69.7
0
3
0
0
+14
3	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/8/2025
2024-25
OKCOKC
@
CLECLE
12
8
2
2
1
0
3
10
30.0
0
3
0.0
2
2
100.0
36.8
0
2
0
1
+7
4	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/5/2025
2024-25
OKCOKC
vs
BOSBOS
12
11
3
2
0
0
3
6
50.0
0
1
0.0
5
5
100.0
67.1
0
3
0
2
-3
5	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/3/2025
2024-25
OKCOKC
vs
NYKNYK
12
14
0
1
0
0
5
6
83.3
1
1
100.0
3
3
100.0
95.6
0
0
1
1
+3
6	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
1/2/2025
2024-25
OKCOKC
vs
LACLAC
12
7
1
5
0
0
2
5
40.0
0
0
0
3
3
100.0
55.4
0
1
1
0
-8
7	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/31/2024
2024-25
OKCOKC
vs
MINMIN
9
10
3
1
0
0
4
6
66.7
0
0
0
2
2
100.0
72.7
1
2
1
0
-3
8	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/29/2024
2024-25
OKCOKC
vs
MEMMEM
9
11
1
4
0
0
4
4
100.0
1
1
100.0
2
2
100.0
112.7
0
1
0
0
+9
9	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/28/2024
2024-25
OKCOKC
@
CHACHA
11
9
0
4
0
0
4
6
66.7
1
1
100.0
0
0
0
75.0
0
0
0
1
+9
10	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/26/2024
2024-25
OKCOKC
@
INDIND
12
6
0
2
0
1
2
8
25.0
0
1
0.0
2
2
100.0
33.8
0
0
0
1
-10
11	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/23/2024
2024-25
OKCOKC
vs
WASWAS
8
2
1
1
0
2
1
3
33.3
0
0
0
0
0
0
33.3
1
0
2
0
-4
12	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/20/2024
2024-25
OKCOKC
@
MIAMIA
12
10
3
1
0
0
4
6
66.7
1
2
50.0
1
1
100.0
77.6
1
2
2
0
+5
13	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/19/2024
2024-25
OKCOKC
@
ORLORL
12
13
2
3
1
2
5
6
83.3
0
0
0
3
3
100.0
88.8
0
2
1
0
+1
14	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/14/2024
2024-25
OKCOKC
vs
HOUHOU
12
4
3
1
4
0
1
8
12.5
0
4
0.0
2
2
100.0
22.5
0
3
1
1
-2
15	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/10/2024
2024-25
OKCOKC
vs
DALDAL
12
16
3
1
0
0
5
9
55.6
2
4
50.0
4
4
100.0
74.3
0
3
0
2
+8
16	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/7/2024
2024-25
OKCOKC
@
NOPNOP
12
16
0
4
0
0
7
7
100.0
1
1
100.0
1
2
50.0
101.5
0
0
1
0
+12
17	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/5/2024
2024-25
OKCOKC
@
TORTOR
12
13
2
2
0
2
5
12
41.7
0
6
0.0
3
3
100.0
48.8
0
2
1
0
+17
18	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/3/2024
2024-25
OKCOKC
vs
UTAUTA
12
6
3
4
2
0
3
9
33.3
0
3
0.0
0
0
0
33.3
1
2
0
2
+7
19	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
12/1/2024
2024-25
OKCOKC
@
HOUHOU
12
6
3
1
0
0
2
7
28.6
1
4
25.0
1
2
50.0
38.1
1
2
1
0
-5
20	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/29/2024
2024-25
OKCOKC
@
LALLAL
8
6
0
2
0
0
3
7
42.9
0
2
0.0
0
0
0
42.9
0
0
0
0
+9
21	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/27/2024
2024-25
OKCOKC
@
GSWGSW
12
12
4
1
1
0
6
8
75.0
0
2
0.0
0
0
0
75.0
0
4
1
1
+16
22	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/25/2024
2024-25
OKCOKC
@
SACSAC
11
12
2
4
0
0
5
7
71.4
2
3
66.7
0
0
0
85.7
0
2
2
1
+4
23	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/20/2024
2024-25
OKCOKC
vs
PORPOR
12
4
2
1
0
0
1
6
16.7
0
0
0
2
2
100.0
29.1
0
2
1
0
-2
24	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/19/2024
2024-25
OKCOKC
@
SASSAS
8
7
0
1
1
0
3
3
100.0
1
1
100.0
0
0
0
116.7
0
0
2
1
+8
25	Shai Gilgeous-Alexander	
Shai Gilgeous-Alexander
11/17/2024
2024-25
OKCOKC
vs
DALDAL
12
13
1
1
0
1
6
7
85.7
0
0
0
1
2
50.0
82.5
0
1
0
0
-5
"""


def process_data(raw_data):
    rows = raw_data.strip().split("\n")
    clean_rows = []

    for i in range(0, len(rows), 28):
        entry = rows[i:i + 28]
        if len(entry) == 28:
            entry[0] = entry[0].split("\t")[0] 


            if entry[5] == "@":
                opponent_type = "Away"
            elif entry[5] == "vs":
                opponent_type = "Home"
            else:
                opponent_type = "Unknown"

            
            clean_rows.append([
                entry[0],  # Game ID
                entry[1],  # Player Name
                entry[2],  # Game Date
                entry[3],  # Season
                entry[4],  # Team
                opponent_type,  # Tipo de oponente
                entry[6],  # Opponent Team
                entry[7],  # Minutes Played
                entry[8],  # Points
                entry[9], # Rebounds
                entry[10], # Assists
                entry[11], # Steals
                entry[12], # Blocks
                entry[13], # Field Goals Made
                entry[14], # Field Goals Attempted
                entry[15], # Field Goal Percentage
                entry[16], # Three Pointers Made
                entry[17], # Three Pointers Attempted
                entry[18], # Three Pointer Percentage
                entry[19], # Free Throws Made
                entry[20], # Free Throws Attempted
                entry[21], # Free Throw Percentage
                entry[22], # True Shooting Percentage (TS%)
                entry[23], # Offensive Rebounds (OREB)
                entry[24], # Defensive Rebounds (DREB)
                entry[25], # Turnovers (TOV)
                entry[26], # Personal Fouls (PF)
                entry[27], # Plus/Minus (+/-)
            ])
    return clean_rows



headers = [
    "Game ID", "Player Name", "Game Date", "Season", "Team", "Opponent Type", "Opponent Team",
    "Minutes Played", "Points", "Rebounds", "Assists", "Steals", "Blocks", "FG Made",
    "FG Attempted", "FG %", "3P Made", "3P Attempted", "3P %", "FT Made", "FT Attempted", "FT %",
    "TS%", "OREB", "DREB", "TOV", "PF", "+/-"
]

table_data = process_data(data)

output_file = "nba_shai_1q_stats.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)

print(f"Os dados foram processados e salvos em {output_file}.")


csv_file = output_file


pontos = []


with open(csv_file, mode='r') as file:
    
    csv_reader = csv.DictReader(file)
    
  
    for row in csv_reader:
    
        pontos.append(int(row["Points"]))
print("Pontos:")
print(pontos)


def distribuicao_normal(amostras, x):
    try:
        media = np.mean(amostras)
        desvio_padrao = np.std(amostras)
        if desvio_padrao == 0:
          raise ZeroDivisionError("Desvio padrão amostral igual a zero")
        pdf = st.norm.pdf(x, loc=media, scale=desvio_padrao)
        prob_menos_que_x = st.norm.cdf(x, loc=media, scale=desvio_padrao)
        prob_mais_que_x = 1 - prob_menos_que_x
        return (pdf, prob_menos_que_x, prob_mais_que_x)
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Um erro ocorreu: {e}")
        return None


def distribuicao_t_student(amostras, x):
    try:
        n = len(amostras)
        graus_liberdade = n - 1
        if graus_liberdade <= 0:
            raise ValueError("Número de amostras insuficiente para calcular os graus de liberdade")
        media = np.mean(amostras)
        desvio_padrao = np.std(amostras)
        if desvio_padrao == 0:
          raise ZeroDivisionError("Desvio padrão amostral igual a zero")
        t_score = (x - media) / desvio_padrao
        prob_menos_que_x = st.t.cdf(t_score, df=graus_liberdade)
        prob_mais_que_x = 1 - prob_menos_que_x
        return (t_score, prob_menos_que_x, prob_mais_que_x)
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        return None
    except ValueError as e:
        print(f"Erro de valor: {e}")
        return None
    except Exception as e:
        print(f"Um erro ocorreu: {e}")
        return None


def intervalo_confianca(amostras, nivel_confianca=0.95):
    try:
        media = np.mean(amostras)
        n = len(amostras)
        graus_liberdade = n - 1
        if graus_liberdade <= 0:
            raise ValueError("Número de amostras insuficiente para calcular os graus de liberdade")
        desvio_padrao = np.std(amostras, ddof=1)
        if desvio_padrao == 0:
          raise ZeroDivisionError("Desvio padrão amostral igual a zero")

        t = st.t.ppf((1 + nivel_confianca) / 2, graus_liberdade)
        margem_erro = t * (desvio_padrao / np.sqrt(n))
        limite_inferior = media - margem_erro
        limite_superior = media + margem_erro
        return (limite_inferior, limite_superior)
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        return None
    except ValueError as e:
        print(f"Erro de valor: {e}")
        return None
    except Exception as e:
        print(f"Um erro ocorreu: {e}")
        return None

x = 10
nivel_confianca = 0.95
retorno_normal = distribuicao_normal(pontos, x)
if retorno_normal is not None:
    pdf_normal, prob_menos_que_x_normal, prob_mais_que_x_normal = retorno_normal
    print(f"PDF da distribuição normal em x = {x}: {pdf_normal:.4f}")
    print(f"Probabilidade da distribuição amostral de pontuar menos que {x} pontos (Normal): {prob_menos_que_x_normal:.2f}")
    print(f"Probabilidade de distribuição amostral de pontuar mais que {x} pontos (Normal): {prob_mais_que_x_normal:.2f}")

retorno_t = distribuicao_t_student(pontos, x)
if retorno_t is not None:
    t_student, prob_menos_que_x_t, prob_mais_que_x_t = retorno_t
    print(f"Valor T de Student: {t_student:.2f}")
    print(f"Probabilidade de marcar menos de {x} pontos (T de Student): {prob_menos_que_x_t:.2f}")
    print(f"Probabilidade de marcar mais de {x} pontos (T de Student): {prob_mais_que_x_t:.2f}")


ic_t = intervalo_confianca(pontos, nivel_confianca)
if ic_t is not None:
    lim_inf_t, lim_sup_t = ic_t
    print(f"Intervalo de Confiança ({nivel_confianca*100:.0f}%): ({lim_inf_t:.2f}, {lim_sup_t:.2f})")



def pegar_assistencias(csv_file):
    assistencias = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            assistencias.append(int(row["Assists"]))
    return assistencias

assistencias = pegar_assistencias(csv_file)
print("Assitencias:")
print(assistencias)


x = 2
retorno_normal = distribuicao_normal(assistencias, x)
if retorno_normal is not None:
    pdf_normal, prob_menos_que_x_normal, prob_mais_que_x_normal = retorno_normal
    print(f"PDF da distribuição normal em x = {x}: {pdf_normal:.4f}")
    print(f"Probabilidade da distribuição amostral de marcar menos que {x} assistencia: {prob_menos_que_x_normal:.2f}")
    print(f"Probabilidade de distribuição amostral de marcar mais que {x} assistencias: {prob_mais_que_x_normal:.2f}")

retorno_t = distribuicao_t_student(assistencias, x)
if retorno_t is not None:
    t_student, prob_menos_que_x_t, prob_mais_que_x_t = retorno_t
    print(f"Valor T de Student: {t_student:.2f}")
    print(f"Probabilidade de marcar menos de {x} assistencias (T de Student): {prob_menos_que_x_t:.2f}")
    print(f"Probabilidade de marcar mais de {x} assistencias (T de Student): {prob_mais_que_x_t:.2f}")


ic_t = intervalo_confianca(assistencias, nivel_confianca)
if ic_t is not None:
    lim_inf_t, lim_sup_t = ic_t
    print(f"Intervalo de Confiança ({nivel_confianca*100:.0f}%): ({lim_inf_t:.2f}, {lim_sup_t:.2f})")


def pegar_pontos_home(csv_file):
    pontos_home = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Opponent Type'] == 'Home':
                pontos_home.append(int(row['Points']))
    return pontos_home

pontos_home = pegar_pontos_home(csv_file)
print("Pontos em Casa")
print(pontos_home)

x = 10
retorno_normal = distribuicao_normal(pontos_home, x)
if retorno_normal is not None:
    pdf_normal, prob_menos_que_x_normal, prob_mais_que_x_normal = retorno_normal
    print(f"PDF da distribuição normal em x = {x}: {pdf_normal:.4f}")
    print(f"Probabilidade da distribuição amostral de pontuar em casa menos que {x} pontos (Normal): {prob_menos_que_x_normal:.2f}")
    print(f"Probabilidade de distribuição amostral de pontuar em casa mais que {x} pontos (Normal): {prob_mais_que_x_normal:.2f}")

retorno_t = distribuicao_t_student(pontos_home, x)
if retorno_t is not None:
    t_student, prob_menos_que_x_t, prob_mais_que_x_t = retorno_t
    print(f"Valor T de Student: {t_student:.2f}")
    print(f"Probabilidade de marcar em casa menos de {x} pontos (T de Student): {prob_menos_que_x_t:.2f}")
    print(f"Probabilidade de marcar em casa mais de {x} pontos (T de Student): {prob_mais_que_x_t:.2f}")


ic_t = intervalo_confianca(pontos_home, nivel_confianca)
if ic_t is not None:
    lim_inf_t, lim_sup_t = ic_t
    print(f"Intervalo de Confiança ({nivel_confianca*100:.0f}%): ({lim_inf_t:.2f}, {lim_sup_t:.2f})")



def extrair_pontos_e_tipo_oponente(arquivo_csv):
    matriz = []
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pontos = int(row["Points"])
            tipo_oponente = row["Opponent Type"]
            matriz.append([pontos, tipo_oponente])
    return matriz

def extrair_assistencias_e_tipo_oponente(arquivo_csv):
    matriz = []
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            assistencias = int(row["Assists"])
            tipo_oponente = row["Opponent Type"]
            matriz.append([assistencias, tipo_oponente])
    return matriz


pontos_resultante = extrair_pontos_e_tipo_oponente(csv_file)
assistencias_resultant = extrair_assistencias_e_tipo_oponente(csv_file)

df_pontos = pd.DataFrame(pontos_resultante, columns=["Pontos", "Local"])

df_assistencias = pd.DataFrame(assistencias_resultant, columns=["Assistencias", "Tipo_Oponente"])

plt.figure(figsize=(8, 6))
sns.boxplot(x="Local", y="Pontos", data=df_pontos, hue="Local", dodge=False, palette="coolwarm")
plt.title("Distribuição de Pontos por Local de Jogo", fontsize=16)
plt.xlabel("Local do Jogo", fontsize=12)
plt.ylabel("Pontos Marcados", fontsize=12)
y_ticks = range(df_pontos["Pontos"].min(), df_pontos["Pontos"].max() + 1, 2)
plt.yticks(y_ticks)

plt.figure(figsize=(8, 6))
sns.boxplot(x="Tipo_Oponente", y="Assistencias", data=df_assistencias, palette="coolwarm")
plt.title("Distribuição de Assistências por Tipo de Oponente", fontsize=16)
plt.xlabel("Tipo de Oponente", fontsize=12)
plt.ylabel("Assistências", fontsize=12)

plt.show()