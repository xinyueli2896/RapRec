import json

MASKED_DIRTY_TOKENS = ['wet-***', 'f**ked', 'A*s', "f**kin'", 'n****', 'a*s', 'n***a"', 
                'P***ycat', 'f**ker', 'p***ies', 'd**e', '"****', 'motherf**kin', 
                '******', '***', 'b***hes', 'B***h', "sh*t's", 'w**d', 'c******e', 
                'W***es', 'h**s', 'mothaf**ka', 'b**es', 'S**tted', 'P***y', "b***he's", 
                "s**ttin'", 'F**kboy', 'm*******a', 'f**k', 'N**gas', 'S**t', 'F**ked', 
                'Coc*ine', "Abraca-f**kin'-dabra", '*******', 'F**k', 's**t"', "*****n'", 
                "f**k's", "mothaf**kin'", 'n***a', "N***a's", 'd**n', 's**ts', 'ni**a', 
                'ex-d**g', 'B***hes', 'bull****', 'Motherf**ker', 'b**ch', 'motherf**kers', 
                'coc*ine', 'f**king', 's*x', 'c*****e', 'N***as', '****', "s**t's", '*****es', 
                "S**t's", 'h*es', 'motherf**king', "motherf**kin'", 'Ni**a', 'f**kers', 
                'b**ches', 'N***a', 'n**gas', 'n**ga', 'Muhf**kas', 'n*****', 'h*e', 'Godd**n', 
                'p***y', 'Wet-***', "S**ttin'", 'B**ch', 'motherf**ker', 'B*****s', 'f**k-ups', 
                'b***h', '*****', 'f**ks', 'ch**per', 'p**l', 'b***hеs', 'keed**np', 'a**', 'n***as', 
                "f**kin'bottom", "****in'", 'Mothaf**ka', 'godd**n', 'goofy-a*s', 'p**sy', 'd**k', 
                '*****"', 'N**ga', 'muhf**kas', '"f**k', 'd**gs', "m**********n'", "F**kin'", 
                'crazy-a*s', 's**t', 'bulls**t', 'n**k', 'D**n', 'sh*t', 'D**mit', "****'"]

UNMASED_TOKENS = ['wet-ass', 'fucked', 'Ass', "fuckin'", 'n****', 'ass', 'nigga"', 
                'Pussycat', 'fucker', 'pussies', 'dope', '"****', 'motherfuckin', 
                '******', '***', 'bitches', 'Bitch', "shit's", 'weed', 'c******e', 
                'W***es', 'houss', 'mothafucka', 'bitches', 'Shitted', 'Pussy', "bitche's", 
                "shittin'", 'Fuckboy', 'marijuana', 'fuck', 'Niggas', 'Shit', 'Fucked', 
                'Cocaine', "Abraca-fuckin'-dabra", '*******', 'Fuck', 'shit"', "*****n'", 
                "fuck's", "mothafuckin'", 'nigga', "Nigga's", 'damn', 'shits', 'nigga', 
                'ex-drug', 'Bitches', 'bullshit', 'Motherfucker', 'bitch', 'motherfuckers', 
                'cocaine', 'fucking', 'sex', 'cocaine', 'Niggas', '****', "shit's", '*****es', 
                "Shit's", 'holes', 'motherfucking', "motherfuckin'", 'Nigga', 'fuckers', 
                'bitches', 'Nigga', 'niggas', 'nigga', 'Muhfuckas', 'n*****', 'hole', 'Goddamn', 
                'pussy', 'Wet-ass', "Shittin'", 'Bitch', 'motherfucker', 'Bitches', 'fuck-ups', 
                'bitch', '*****', 'fucks', '******', 'pill', 'bitchеs', 'keep', 'a**', 'n***as', 
                "f**kin'bottom", "****in'", 'Mothaf**ka', 'godd**n', 'goofy-a*s', 'pussy', 'dick', 
                '*****"', 'Nigga', 'muhfuckas', '"fuck', 'drugs', "m**********n'", "Fuckin'", 
                'crazy-ass', 'shit', 'bullshit', '****', 'Damn', 'shit', 'then', "fuckin"]

assert len(MASKED_DIRTY_TOKENS) == len(UNMASED_TOKENS)

RM = dict()
for x, y in zip(MASKED_DIRTY_TOKENS, UNMASED_TOKENS):
    RM[x] = y

with open("unmask.json", 'w') as f:
    json.dump(RM, f)

'''RM["wet-***"] = "wet-ass"
RM["f**ked"] = "fucked"
RM["A*s"] = "Ass"
RM["f**kin"] = "fuckin"
RM["a*s"] = "ass"
RM["n***a"] = "nigga"
RM["P***ycat"] = "Pussycat"
RM["f**ker"] = "fucker"
RM["p***ies"] = "panties"
RM["motherf**kin"] = "motherfuckin"
RM["b***hes"] = "bitches"
RM["B***h"] = "Bitch"
RM["sh*t's"] = "shit's"
RM["h**s"] = "house"
RM["mothaf**ka"] = "mothafucka"
RM["b**es"] = "bitches"
RM["S**tted"] = "Shitted"
RM["P***y"] = "pussy"
RM["b***he's"] = "bitche's"
RM["s**ttin"] = "shittin"
RM["F**kboy"] = "Fuckboy"
RM["f**k"] = "fuck"
RM["N**gas"] = "Niggas"
RM["S**t"] = "Shit"'''