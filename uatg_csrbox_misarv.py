from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any
from random import randint
import random


class uatg_csrbox_misarv(IPlugin):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, core_yaml, isa_yaml) -> bool:
    	self.hart0 = isa_yaml['hart0']
    	self.misa = hart0['misa']
    	self.rv = misa['reset-val']
      return 
        
    def generate_asm(self) -> Dict[str, str]:
	
        asm = ''
        asm+= f'\tli x4, {self.rv}\n'
        for i in range(0,100):
          asm += '\tcsrr x5, misa\n'
          asm += '\tcsrrc x0, misa, x5\n'
          asm += '\tbne misa, x4, trap\n'
        asm+= 'trap:\n\taddi x31, x0,1\n'


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
