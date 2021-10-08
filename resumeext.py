from nltk.util import pr
from resume_parser import resumeparse

from pyresparser import ResumeParser
import pandas as pd
import os
import spacy
a = spacy.load('en_core_web_sm')
print(a)

# dir_list = os.listdir(r'/home/cheems/Desktop/indee/extraction/SampleResume.pdf')
#print(dir_list)

res_list = []
# paths = r'C:\Users\hp\Desktop\New folder (3)\datasets'
paths = r'/home/cheems/Desktop/indee/extraction/SampleResume.pdf'
c = 0
# for i in paths:
#     c = c + 1
#     if c == 5000:
#         break
pfinal = os.path.join(paths)
data = ResumeParser(pfinal).get_extracted_data()
res_list.append(data)

print(len(res_list))

df = pd.DataFrame(res_list)
print(df)