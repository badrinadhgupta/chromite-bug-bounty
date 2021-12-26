from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any
from random import randint
import random


class uatg_csrbox_misam(IPlugin):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, core_yaml, isa_yaml) -> bool:
    	
        return 
        
    def generate_asm(self) -> Dict[str, str]:
	
        for i in range(0,2):
          x1 = random.randrange(0,2**16+1)
          x2 = random.randrange(0,2**16+1)
          asm += f'\tli x1, {hex(x1)}\n\tli x2, {hex(x2)}\n\tmul x3, x1, x2\n\tmulh x4, x1, x2\n\tmulhu x5, x1, x2\n\tmulhsu x6, x1, x2\n\tdiv x7, x1, x2\n\tdivu x8, x1, x2\n\tcsrrc x30, misa, 0x1000\n\tmul x9, x1, x2\n\tmulh x10, x1, x2\n\tmulhu x11, x1, x2\n\tmulhsu x12, x1, x2\n\tdiv x13, x1, x2\n\tdivu x14, x1, x2\n\tbeq x9, x3, trap\n\tbeq x10, x4, trap\n\tbeq x11, x5, trap\n\tbeq x12, x6, trap\n\tbeq x13, x7, trap\n\tbeq x14, x8, trap\n'
        asm += 'trap:\n\taddi x31, x0, 1\n'

        compile_macros = []

        return [{
            'asm_code': asm,
            'asm_sig': '',
            'compile_macros': compile_macros
        }]

    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv
