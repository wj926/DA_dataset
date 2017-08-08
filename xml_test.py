# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 14:32:32 2015

@author: slcf
"""

#from xml.etree.ElementTree import parse
#import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import pickle

## f.readlines()
category = 'kitchen/'
f = open("C:/Users/Woojin/Documents/GitHub/DomainAdaptation/Data/original amazon/electronics/all_new.review","rb")

## exception 
#try:%
tree = ET.parse(f)
#except xml.etree.ElementTree.ParseError as e:
#    print e
#    a = str(e)
#    r1 = a[5]    
    
f.close()
note = tree.getroot()

rev_data = [];
rev_tx_rating = [];

for rev_xml in note.getiterator("review"):
    rev_data.append(rev_xml.findtext("review_text"))
    rev_tx_rating.append(rev_xml.findtext("rating"))

rev_rating = []
for i in rev_tx_rating:
    rev_rating.append(float(i))
    
    
## file save

f = open("C:/Users/Woojin/Documents/GitHub/DomainAdaptation/Data/original amazon/electronics/elec_all_preprocessed.txt",'wb')
pickle.dump(rev_data,f)
f.close()

f = open("C:/Users/Woojin/Documents/GitHub/DomainAdaptation/Data/original amazon/electronics/delec_all_label.txt",'wb')
pickle.dump(rev_rating,f)
f.close()
