import os
import logging
from command import Command

class CommandRunner:
    def __init__(self, input_file_path, output_dir_path):
        self.input_file_path = input_file_path
        self.output_dir_path = output_dir_path
    
    def create_log_file(self, log_file_path, program_name):
        logger = logging.getLogger(program_name)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file_path)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
    
    def run_commands(self):
        
        if not os.path.exists(self.output_dir_path):
            os.mkdir(self.output_dir_path)
        
        with open(self.input_file_path, 'r') as programs_file:
            program_name = os.path.splitext(os.path.basename(self.input_file_path))[0]
            log_file_path = os.path.join(self.output_dir_path, 'run_results.log')
            log_file = self.create_log_file(log_file_path, program_name)

            count = 0
            for line in programs_file:
                count += 1
                command_file_path = os.path.join(self.output_dir_path, f'{count}.log')
                    
                command = Command(line.strip())
                returncode ,result = command.execute()

                if returncode == 0:
                    log_file.info(f'{returncode} - success')
                else:
                    with open(command_file_path, 'a') as command_file:

                        if result:
                            command_file.write(result)

                    log_file.info(f'{returncode} - {command_file_path}')