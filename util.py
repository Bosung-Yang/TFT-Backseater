import pandas as pd
import ast

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

#preprocess_augment()

def remove_redundancy():
    def remove_redundant_name(x):
        return x[:len(x)//2]
    def remove_redundant_type(x):
        new_x = []
        for item in x:
            print(item)
            if item[:len(item)//2] == item[len(item)//2:]:
                new_x.append(item[:len(item)//2])
            else:
                new_x.append('Economy')
        return new_x

    df = pd.read_csv('./data/augment.csv')
    df['Type'] = df['Type'].apply(ast.literal_eval)
    df['Augment'] = df['Augment'].apply(remove_redundant_name)
    df['Type'] = df['Type'].apply(remove_redundant_type)
    print(df)
    df.to_csv('./data/augment-preprocessed.csv', index=False)
    
#remove_redundancy()