# Sett Sarverott @ 2023
#this code is to programmify documentation of experiment in physics style

    ####### TODO: better varnames, hunt and fix bugs, optimalisation for module application, better commentary, manuals, proof-of-work examples

experiment=None

def START(name, silent=False):
    experiment={
        "id": 1, # NOTE: briefcase global experiment counter can be implemented
        "name": name,
        "_quietmode": silent,
        "_complete": False
    }
    experiment["equat"]={}
    experiment["trg-desc"]={}
    experiment["vars"]={}
    experiment["equat-var-used"]={}
    experiment["concl"]=[]
    experiment["data"]=[]
    experiment["equatinfo"]={}

def Description(shortinfo):
    experiment["desc"]=shortinfo

def Target(var, whatIsVar=None):
    experiment["vars"][var]=None
    experiment["equat"][var]=lambda *_: None 
    experiment["equat-var-used"][var]=None
    if whatIsVar is not None:
        experiment["trg-desc"][var]=whatIsVar

def Data(var, value):
    experiment["vars"][var]=value
    experiment["data"].append(var)

def Equation(resultVar, inputVars, funct, equatinfo=None):
    experiment["equat-var-used"][resultVar]=inputVars
    experiment["equat"][resultVar]=funct
    experiment["equatinfo"][resultVar]=equatinfo
    
def Answer():
    processingFlag=False
    while processingFlag:
        for i in experiment["equat-var-used"]:
            if experiment["vars"][i] is None:
                dependencyFlag=True
                for j in experiment["equat-var-used"][i]:
                    if experiment["vars"][j] is None:
                        dependencyFlag=False
    
                if dependencyFlag:
                    processingFlag=True
    if None not in experiment["vars"].items():
        experiment["_complete"]=True

def Conclusion(concl):
    experiment["concl"].append(concl)

def END():
    None
    
