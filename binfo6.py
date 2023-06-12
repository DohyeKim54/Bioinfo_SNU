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
    if Shannon > 0.7 and len(matches) > 3:
      print(i, p_list, Shannon)
# >> 여기까지 .py file로 만들어서 저장 후 리눅스(Ubuntu) shell에서 실행
# Shannon entropy > 0.7, read number > 3인 position 확인 - 5개 locus
'''
68 [0.0, 0.0, 0.75, 0.25] 0.8112781244591328
88 [0.2, 0.8, 0.0, 0.0] 0.7219280948873623
110 [0.25, 0.0, 0.75, 0.0] 0.8112781244591328
715 [0.2, 0.0, 0.0, 0.8] 0.7219280948873623
738 [0.4, 0.0, 0.0, 0.6] 0.9709505944546686
'''