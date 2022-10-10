import pandas as pd
import numpy as np
from reports.models import Police
from datetime import datetime

df=pd.read_csv('data.csv', sep=',')
df=df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.fillna('')
df['bp'] = df['bp'].astype(str)
#df['bp'] = df['bp'].astype(np.int64)
#print(df.dtypes)
#print(df['rank'].unique())
#print(df.count())

prob = []
ranks = []
batches = []
districts = []
polices = []
for row in df.iterrows():
    row[1]['bp'] = row[1]['bp'].split('.')[0]
    serial = row[1]['serial']
    bp = row[1]['bp']
    if bp == '':
        prob.append(row[1])
        continue
    
    dob = row[1]['dob']
    try:
        dob = datetime.strptime(dob, '%d-%m-%y')
        
    except:
        try:
            dob = datetime.strptime(dob, '%d-%m-%Y')
            
        except:
            try:
                dob = datetime.strptime(dob, '%y-%m-%d')
                
            except:
                try:
                    dob = datetime.strptime(dob, '%Y-%m-%d')
                    
                except:
                    try:
                        dob = datetime.strptime(dob, '%d/%m/%y')
                        
                    except:
                        try:
                            dob = datetime.strptime(dob, '%d/%m/%Y')
                            
                        except:
                            try:
                                dob = datetime.strptime(dob, '%d.%m.%y')
                                
                            except:
                                try:
                                    dob = datetime.strptime(dob, '%d.%m.%Y')
                                    
                                except:
                                    try:
                                        dob = datetime.fromisoformat(dob)
                                        
                                    except:
                                        prob.append(row[1])
                                        continue
                                            
    #if dob >= datetime.now():
    #    prob.append(dob)
    
    name_bangla = row[1]['name']
    name_english = row[1]['name']
    if (name_bangla == ''):
        prob.append(row[1])
        continue
    
    rank = row[1]['rank']
    addl_ig_variants = ['Addl. IGP', 'Addl. IG', 'Adl IG', 'Addl. IG (CC)']
    if rank in addl_ig_variants:
        rank = 'Addl. IG'
    addl_sp_variants = ['Addl.SP', 'Addl. SP', 'Addl SP']
    if rank in addl_sp_variants:
        rank = 'Addl. SP'
    sp_variants = ['SP', 'SP (CC)']
    if rank in sp_variants:
        rank = 'SP'
    ranks.append(rank)

    # Duplicates
    if (bp in ['7205112377', '8112147769', '8212147698']):
        prob.append(row[1])
        continue

    batch = row[1]['batch'].split(' ')[0]
    batches.append(batch)

    district = row[1]['district']
    if ('/' in district):
        prob.append(row[1])
        continue
    districts.append(district)

    present = row[1]['present']
    past = row[1]['past']
    comments = row[1]['comment']
    mobile = row[1]['mobile']
    if (len(mobile) > 50):
        prob.append(row[1])
        continue
    edu = row[1]['edu']
    merit = row[1]['serial']

    # District problem
    if (bp in ['8517180828', '8316180532', '8917180831', '9018225249', '9218224213', '8617180829', '9017180832', '8517180827', '8817180830', '9218220592']):
        prob.append(row[1])
        continue
    
    polices.append(Police(
        police_name_english=name_english,
        police_name_bangla=name_bangla,
        police_dob=dob,
        police_rank=rank,
        police_id=bp,
        police_batch=batch,
        police_district=district,
        police_past=past,
        police_present=present,
        police_comments=comments,
        police_mobile=mobile,
        police_edu=edu,
        police_merit=merit,
    ))

#print(prob)
#print(list(set(ranks)))
#print(list(set(batches)))
#print(list(set(districts)))
#print(polices)
Police.objects.bulk_create(polices)
