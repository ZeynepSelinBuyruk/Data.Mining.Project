# Data Mining Midterm Project

## Proje Açıklaması

Bu proje, **imbalansız veri setlerinde sınıf dengesizliğini çözmek** amacıyla kNN tabanlı **sentetik veri üretim** tekniğini uygulamaktadır. Yöntem, azınlık sınıfının en yakın komşularını kullanarak doğrusal interpolasyon ile yapay veri noktaları oluşturur.

## Metodoloji

### 1. Problem
- Gerçek dünya veri setlerinde sık rastlanan **sınıf dengesizliği** sorunu
- Azınlık sınıfın eksik temsil edilmesi model performansını düşürür
- Elde edilen modeller çoğunluk sınıfını öğrenir, azınlık sınıfı tanımayabilir

### 2. Çözüm: KNN-Based Linear Interpolation

Algoritma şu adımları takip eder:

```
1. Azınlık sınıfı (X_min) ve çoğunluk sınıfı (X_maj) ayrılır
2. Gerekli sentetik örnek sayısı hesaplanır: needed = len(X_maj) - len(X_min)
3. Her sentetik örnek için:
   - Rastgele bir azınlık örneği p seçilir
   - p'nin en yakın k komşusu bulunur (k=5)
   - Komşular arasından rastgele biri q seçilir
   - Sentetik nokta: s = p + t(q - p), t  [0,1] (doğrusal interpolasyon)
4. Yeni veri seti oluşturulur: X_balanced = X  Synthetic_Samples
```

### 3. Veri Seti
- **Samples**: 1100 örnek
- **Features**: 2 (2D görselleştirme için)
- **Sınıf Dağılımı**: 90% çoğunluk, 10% azınlık (imbalansız)
- **Test Sayısı**: 5 farklı random state ile tekrarlı deney

## Sonuçlar

### Model Performansı Metrikleri

Projede **Logistic Regression** ile 5 dataset üzerinde değerlendirme yapılmıştır:

| Metrik | Before Oversampling | After Oversampling |
|--------|--------------------|--------------------|
| **Precision** | Düşük |  İyileşme |
| **Recall** | Çok Düşük |  Önemli İyileşme |
| **F1 Score** | Dengesiz |  İyileşme |
| **AUC** | Orta |  İyileşme |

**Temel Bulgu**: Oversampling sonrası **Recall değerleri önemli ölçüde artarak**, azınlık sınıfının daha iyi tanınmasını sağlamıştır.

### Görselleştirmeler

1. **Dataset Dağılımları**: Before/After dağılım karşılaştırması
2. **ROC Eğrileri**: 5 dataset için ROC performans eğrileri
3. **Sınıf Dağılımları**: Before/After sınıf sayıları tablosu

## Kod Yapısı

### `oversample_knn_linear(X, y, minority_label=1, k=5)`
- Imbalansız veri setini dengeli hale getirir
- kNN ile sentetik örnekler oluşturur
- Doğrusal interpolasyon ile yapay veri noktaları oluşturur

**İşleyiş:**
```python
1. Azınlık ve çoğunluk örnekleri ayrılır
2. İhtiyaç duyulan sentetik örnek sayısı hesaplanır
3. Her sentetik örnek için:
   - Rastgele azınlık örneği seçilir
   - KNN ile 5 en yakın komşu bulunur
   - Komşular arasından rastgele biri seçilir
   - Doğrusal interpolasyon: s = p + t*(q-p)
4. Balanced veri seti döndürülür
```

### `evaluate_model(X, y)`
- Veri setini %70 train, %30 test olarak ayırır
- Logistic Regression modeli eğitir
- Dönen metrikler:
  - **Precision**: Tahmin edilen pozitiflerden kaçı gerçekten pozitif?
  - **Recall**: Gerçek pozitiflerden kaçını yakaladık?
  - **F1 Score**: Precision ve Recall'ın harmonik ortalaması
  - **AUC**: ROC eğrisi altında kalan alan

## Kullanılan Kütüphaneler

```python
import numpy as np                          # Sayısal işlemler
from sklearn.datasets import make_classification  # İmbalansız veri seti
from sklearn.neighbors import NearestNeighbors    # KNN algoritması
from sklearn.model_selection import train_test_split  # Train/Test bölme
from sklearn.metrics import (                      # Performans metrikleri
    precision_score, recall_score, f1_score, 
    roc_auc_score, roc_curve
)
from sklearn.linear_model import LogisticRegression  # Sınıflandırıcı
from sklearn.preprocessing import StandardScaler     # Veri normalizasyonu
import pandas as pd                         # Veri analizi ve tablo işlemleri
import matplotlib.pyplot as plt             # Temel görselleştirme
import seaborn as sns                       # Gelişmiş görselleştirme
```

## Çalıştırma

Jupyter Notebook dosyasını açarak hücreleri sırasıyla çalıştırın:

```bash
jupyter notebook Data_Mining_Midterm_Project.ipynb
```

Veya VS Code / JupyterLab'da direkt açıp çalıştırabilirsiniz.

## Sonuçların Yorumu

 **Başarı**: Oversampling tekniği azınlık sınıfının tanınma oranını (Recall) önemli ölçüde artırmıştır.

 **Dikkat**: Yapay veri üretimi model performansını artırsa da, gerçek dünya verisi her zaman daha değerlidir.

 **Alternatif Teknikler**: 
- **SMOTE** (Synthetic Minority Oversampling Technique)
- **ADASYN** (Adaptive Synthetic Sampling)
- **Undersampling** (çoğunluk sınıfını azaltma)
- **Class Weighting** (ağırlıklı sınıflandırma)
- **Threshold Adjustment** (karar eşiği ayarlama)

## Öğrenilen Dersler

1. **Sınıf Dengesizliği**: İmbalansız veriyle çalışırken doğru metrikler (Recall, F1) kullanmak kritiktir
2. **Sentetik Veri**: KNN tabanlı interpolasyon basit ama etkili bir yöntemdir
3. **Tekrarlı Testler**: Farklı random state'ler ile tekrar eden deneylerin sonuçları daha güvenilirdir

## Dosya Yapısı

```
Data.Mining.Project/
 README.md (Bu dosya)
 Data_Mining_Midterm_Project.ipynb (Ana proje dosyası)
 .git/ (Git repository)
```

## Yazar
**Zeynep Selin Buyruk**

## Tarih
Ocak 2026
