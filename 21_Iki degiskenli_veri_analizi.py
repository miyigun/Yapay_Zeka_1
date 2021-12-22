import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#python'da uyarıları kapatalım
import warnings
warnings.filterwarnings("ignore")

#veriyi içeri aktaracağız
veri=pd.read_csv("olimpiyatlar_temizlenmis.csv")

erkek=veri[veri.cinsiyet=="M"]
print(erkek.head(2))

kadin=veri[veri.cinsiyet=="F"]
print(kadin.head(1))

plt.figure()
plt.scatter(kadin.boy,kadin.kilo,alpha=0.4,label="Kadın")
plt.scatter(erkek.boy,erkek.kilo,alpha=0.4,label="Erkek")
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Boy ve Kilo Arasındaki İlişki")
plt.legend()
plt.show()
