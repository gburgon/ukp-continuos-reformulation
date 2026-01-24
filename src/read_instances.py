import pandas as pd
def ler_instancia_eduk(caminho):
    with open(caminho, "r") as f:
        linhas = f.readlines()
    # lê n e c
    n = int([l for l in linhas if l.strip().startswith("n:")][0].split(":")[1])
    capacity = int([l for l in linhas if l.strip().startswith("c:")][0].split(":")[1])

    # encontra índice de início e fim dos dados
    idx_ini = [i for i, l in enumerate(linhas) if "begin data" in l][0] + 1
    idx_fim = [i for i, l in enumerate(linhas) if "end data" in l][0]

    # lê os pares peso valor
    dados = [l.strip().split() for l in linhas[idx_ini:idx_fim]]
    df = pd.DataFrame(dados, columns=["weights", "values"]).astype(float)

    weights = df["weights"].to_numpy()
    values = df["values"].to_numpy()

    return n, capacity, weights, values