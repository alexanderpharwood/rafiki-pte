class StyleSheet:
    def __init__(self):
        self.identifier = None
        self.rules = []
        self.pseudoRules = {}

    def setIdentifier(self, identifier):
        self.identifier = identifier
    
    def setRule(self, rule, value):
        self.rules.append([rule, value])

    def setPseudoRule(self, pseudoFlag, rule, value):
        if self.pseudoRules.get(pseudoFlag) == None:
            self.pseudoRules[pseudoFlag] = []
        self.pseudoRules[pseudoFlag].append([rule, value])

    def compileRules(self):
        compiledRules = ""
        for rule in self.rules:
            compiledRules += rule[0] + ":" + rule[1] + ";"

        if self.identifier == None:
            return compiledRules
        
        return self.identifier + "{" + compiledRules + "}"
    
    def compilePseudoRules(self):
        compiled = ""
        for pseudo, rules in self.pseudoRules.items():
            compiledPseudo = self.identifier + ":" + pseudo + "{"
            for rule in rules:
                compiledPseudo += rule[0] + ":" + rule[1] + ";"
            compiledPseudo += "}"
            compiled += compiledPseudo
        
        return compiled

    def compile(self):
        return self.compileRules() + self.compilePseudoRules()
    

