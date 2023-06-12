import pandas as pd
import re

pileup = pd.read_csv('eCLIP-PCBP1.pileup', sep='\t', names=['chrom', 'pos', '_ref', 'count', 'basereads', 'quals'])
pileup.tail()

toremove = re.compile('[1-9nN<>\$\*#-]|\^~[A-Za-z]')
pileup['matches'] = pileup['basereads'].apply(lambda x: toremove.sub('', x))

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth', 1000)
pileupdf = pileup[['chrom', 'pos', 'count', 'matches']].copy()

print(pileupdf)
# >> 여기까지 .py file로 만들어서 저장 후 리눅스(Ubuntu) shell에서 실행
# pileupdf 형태 확인 - 특수문자 제거는 잘 되었으나 대소문자 섞여있고 read number가 낮은 편