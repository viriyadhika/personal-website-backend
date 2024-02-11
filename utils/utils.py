from utils.constants import COMPANY_DIRECTORY, JOB_DIRECTORY

def generate_input_file(input_file_prefix: str, index: int):
  return JOB_DIRECTORY + '/' + input_file_prefix + str(index) + '.html'

def generate_company_file(input_file):
  return COMPANY_DIRECTORY + '/' + input_file + '.html'