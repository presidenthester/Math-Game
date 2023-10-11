import random
from enum import Enum

class ProblemOperandType(Enum):
    SINGLE_DIGIT  = 1  
    DOUBLE_DIGIT  = 2
    TRIPLE_DIGIT  = 3
    QUAD_DIGIT    = 4
    

class EquationMaker:

    OPERAND_RANGES = {
        ProblemOperandType.SINGLE_DIGIT: (0, 9),
        ProblemOperandType.DOUBLE_DIGIT: (10, 99),
        ProblemOperandType.TRIPLE_DIGIT: (100, 999),
        ProblemOperandType.QUAD_DIGIT: (1000, 9999)
   
    }

    
    def get_operands(self, operand_types):
        if not operand_types:
            raise ValueError("Operand types list must not be empty")
        
        operands = []
        for operand_type in operand_types:
            if operand_type not in self.OPERAND_RANGES:
                raise ValueError(f"Invalid operand type: {operand_type}")

            min_range, max_range = self.OPERAND_RANGES[operand_type]
            operand = random.randint(min_range, max_range)
            operands.append(operand)
            
        self.sorted_operands = sorted(operands, reverse=True)
        
        return self.sorted_operands
    
    
    def generate_addition(self):

        self.correct_sum = sum(self.sorted_operands)
        self.correct_answer = self.correct_sum
        
        self.problem = ""
        for i, operand in enumerate(self.sorted_operands):
            if i == len(self.sorted_operands) - 1:
                self.problem += f"{operand}\n\033[4m\033[0m"
            else:
                self.problem += f"{operand}\n\033[4m+"
                
        return self.problem, self.correct_sum
    
    def generate_subtraction(self):
        
        self.difference = self.sorted_operands[0]
        
        for operand in self.sorted_operands[1:]:
            self.difference -= operand
            self.correct_answer = self.difference

        
        self.problem = ""
        for i, operand in enumerate(self.sorted_operands):
            if i == len(self.sorted_operands) - 1:
                self.problem += f"{operand}\n\033[4m\033[0m"
            else:
                self.problem += f"{operand}\n\033[4m-"
                
        return self.problem, self.difference   

    
    def generate_multiply(self):
        
        self.product = self.sorted_operands[0]
        
        for operand in self.sorted_operands[1:]:
            self.product *= operand
            self.correct_answer = self.product
        
        self.problem = ""
        for i, operand in enumerate(self.sorted_operands):
            if i == len(self.sorted_operands) - 1:
                self.problem += f"{operand}\n\033[4m\033[0m"
            else:
                self.problem += f"{operand}\n\033[4mx"
                
                
                
    
    
    
    def get_answer(self):
        
        print("Solve the equation")
        print("")
        print(self.problem)
        user_answer = int(input("Enter your answer: "))  
        
        if user_answer == self.correct_answer:
            print("That is correct")
        else:
            print("That is wrong")
    
gen = EquationMaker()
gen.get_operands([ProblemOperandType.SINGLE_DIGIT, ProblemOperandType.DOUBLE_DIGIT])
gen.generate_multiply()
gen.get_answer()







