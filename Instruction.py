from enum import Enum, auto

class InstructionCostCategory(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class InstructionCategory(Enum):
    READ_FILE = auto()
    WRITE_FILE = auto()
    AI_PROCESS = auto()
    REPORT = auto()
    FINISH = auto()

class Instruction:
    def __init__(self):
        self.name = None
        self.args = {}
        self.cost = None

class ReadFileInstruction(Instruction):
    def __init__(self, _path:str, _to_variable_name:str):
        super().__init__()
        self.name = InstructionCategory.READ_FILE
        self.cost = InstructionCostCategory.MEDIUM
        self.args = {
            'path' : _path,
            'to_variable' : _to_variable_name
        }

class WriteFileInstruction(Instruction):
    def __init__(self, _path:str, _from_variable_name:str):
        super().__init__()
        self.name = InstructionCategory.WRITE_FILE
        self.cost = InstructionCostCategory.MEDIUM
        self.args = {
            'path' : _path,
            'from_variable' : _from_variable_name
        }

class AiProcessInstruction(Instruction):
    def __init__(self, _task:str, _to_variable_name:str):
        super().__init__()
        self.name = InstructionCategory.AI_PROCESS
        self.cost = InstructionCostCategory.HIGH
        self.args = {
            'task' : _task,
            'to_variable' : _to_variable_name
        }

class ReportInstruction(Instruction):
    def __init__(self, _message:str):
        super().__init__()
        self.name = InstructionCategory.REPORT
        self.cost = InstructionCostCategory.LOW
        self.args = {
            'message' : _message
        }
    