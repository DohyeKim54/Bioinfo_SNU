import pandas as pd
import numpy as np

base_list=['A','G','C','T']
for i in range(len(pileupdf)):
  matches = pileupdf.iloc[i]['matches']
  if not matches or pileupdf.iloc[i].isnull().sum():
    pass
  else:
    Shannon=0
    p_list=[]
    for base in base_list:
      p_base = matches.upper().count(base)/len(matches)
      p_list.append(p_base)
      if p_base != 0:
        Shannon+=-p_base*np.log2(p_base)
    if Shannon > 0.7:
      print(i, p_list, Shannon)
# >> 여기까지 .py file로 만들어서 저장 후 리눅스(Ubuntu) shell에서 실행
# Shannon entropy > 0.7인 position 확인 - 24개 locus