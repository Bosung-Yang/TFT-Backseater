import pandas as pd

def preprocess_augment():
    with open('./data/augment.txt','r') as f:
        lines = f.readlines()
    
    Augment = []
    Tier = []
    Types = []

    DefinedTypes = ['StrategicStrategic', 'GoldEconomy', 'CombatCombat', 'ScalingScaling', 'TraitsTrait', 'ItemsItems']

    idx = 0
    while idx < len(lines):
        types = []
        Augment.append(lines[idx].strip())
        idx +=1
        Tier.append(lines[idx].strip())
        idx +=1

        while idx < len(lines):
            if lines[idx].strip() in DefinedTypes:
                types.append(lines[idx].strip())
                idx += 1
            else:
                #idx +=1
                break
        Types.append(types)
    #print(Augment, Tier, Types)
#    print(len(Augment), len(Tier), len(Type))
    
    df = pd.DataFrame({'Augment':Augment, 'Tier':Tier, 'Type':Types})
    print(df)
    df.to_csv('./data/augment.csv', index=False)

preprocess_augment()