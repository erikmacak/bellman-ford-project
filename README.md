# 🧠 Bellman-Ford Algoritmus – Vizualizační nástroj

## 🇨🇿 Popis projektu (Czech)

Tato aplikace implementuje **Bellman-Fordův algoritmus** pro nalezení nejkratších cest z jednoho počátečního vrcholu ke všem ostatním v orientovaném grafu. Výsledky jsou zobrazeny jak **textově (vzdálenosti ke každému uzlu)**, tak i **graficky pomocí knihoven `matplotlib` a `networkx`**.

---

## ✨ Hlavní funkce

- 📂 Načítání grafu ze souboru
- 🖱️ Výběr počátečního vrcholu přes grafické rozhraní
- 🧮 Výpočet nejkratších cest pomocí Bellman-Fordova algoritmu
- ⚠️ Detekce záporných cyklů v grafu
- 📊 Grafické znázornění s barevným zvýrazněním dosažitelných vrcholů

---

## 🧾 Formát vstupních dat

Každý řádek ve vstupním souboru má následující formát:
```uzel1 uzel2 váha```

**Příklad:**
```A B 4```
```B C -2```

---

## ✅ Výstupní formát
```A: 0```
```B: 4```
```C: 2```

Součástí výstupu je také **vizuální znázornění grafu**.

---

## 🛠️ Jak aplikaci spustit

1. Ujisti se, že máš nainstalovaný **Python 3.7 nebo vyšší**
2. Nainstaluj potřebné knihovny:
    pip install networkx matplotlib
3. Spusť aplikaci:
    python app.py

---

# 🌐 Project Description (English)

This application implements the **Bellman-Ford algorithm** to find the shortest paths from a single starting node to all other nodes in a directed graph. Results are displayed both **as text (distances)** and **graphically using `matplotlib` and `networkx`**.

---

## ✨ Features

- 📂 Load graph from a file  
- 🖱️ Select the starting node through a GUI  
- 🧮 Compute shortest paths using the Bellman-Ford algorithm  
- ⚠️ Detect negative-weight cycles  
- 📊 Visualize the graph with color-highlighted reachable nodes  

---

## 🧾 Input File Format

Each line in the input file should follow this format:
```node1 node2 weight```

**Example:**
```A B 4```
```B C -2```

---

## ✅ Output Format
```A: 0```
```B: 4```
```C: 2```

Includes a **visual representation of the graph**.

---

## 🛠️ How to Run the App

1. Make sure you have **Python 3.7 or higher** installed  
2. Install required libraries:
    pip install networkx matplotlib
3. Run the application:
    python app.py