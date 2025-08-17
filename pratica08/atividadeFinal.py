# Atividade Prática 08
# Comparação de Métricas de Classificação em IA
# Calcular e comparar diferentes métricas de classificação (Precisão, Recall, F1-Score, AUC-ROC) usando um modelo de aprendizado de máquina em Python.

# Sugestão
# Usar o conjundo de dados (dataset) load_breast_cancer disponível na biblioteca scikit-learn;
# Utilize o algoritmo Random Forest;
# Dividir o conjunto de dados em 70% para treino e 30% para teste, garantindo a reprodutibilidade dos dados com 'random_state=42';
# Variável target (vetor) composta de 0 (maligno) ou 1 (benigno)

# Objetivo
# Analisar o desempenho do modelo de classificação por meio das métricas selecionadas, discutindo os resultados obtidos para essa situação médica.

# Sugestão de dependências
# scikit-learn==1.4.0
# pandas==2.2.0
# numpy==1.26.3
# matplotlib==3.8.2
# seaborn==0.13.1



# Dependências
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix, roc_curve
)

# 1. Carregar dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)  # 0 = maligno, 1 = benigno

# 2. Divisão treino/teste (70/30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Treinar Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Predições
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # Probabilidade classe positiva (benigno)

# 5. Métricas
accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall    = recall_score(y_test, y_pred)
f1        = f1_score(y_test, y_pred)
auc       = roc_auc_score(y_test, y_prob)

print("=== Métricas de Classificação ===")
print(f"Acurácia : {accuracy:.4f}")
print(f"Precisão : {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-Score : {f1:.4f}")
print(f"AUC-ROC  : {auc:.4f}")

# 6. Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()

# 7. Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.4f}")
plt.plot([0,1], [0,1], linestyle="--", color="gray")
plt.xlabel("Taxa de Falsos Positivos (FPR)")
plt.ylabel("Taxa de Verdadeiros Positivos (TPR)")
plt.title("Curva ROC - Random Forest")
plt.legend()
plt.show()
