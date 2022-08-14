#!/usr/bin/python3

import os
import re
import asyncio
import requests
import configparser


class ShellyConfig:
    def __init__(self):
        self.settings = []
        pass


    def parse_command_line(self):
        pass


    def load_config(self):
        with open("sample.conf") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                #print(line_num, line)
                if line.startswith("#"):
                    continue
                try:
                    match, setting, value = line.split(maxsplit=2)
                except ValueError:
                    continue

                print(match, setting, value)

                # Validate

                # Add to the config plan
                self.settings.append(match, setting, value)
                    
                


    def run(self):
        self.load_config()
        

if __name__ == "__main__":
    ShellyConfig().run()
    

# End of file.
