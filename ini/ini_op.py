#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: lingyue.wkl
#desc: use to read ini
#---------------------
#2012-02-18 created

#---------------------
import sys
import configparser


class Config:
    def __init__(self, path):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def set(self, filed, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True


def read_config(config_file_path, field, key):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path)
        result = cf.get(field, key)
    except:
        print('No {key} of {field} in {config_file_path} '.format(key=key,field=field,config_file_path=config_file_path))
        sys.exit('Reading failed.')
    return result


def write_config(config_file_path, field, key, value):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path)
        cf.set(field, key, value)
        cf.write(open(config_file_path, 'w'))
    except:
        sys.exit(1)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('\
        Please input enough parameters: \n \
        Read: FILE_PATH FIELD KEY \n \
        Write: FILE_PATH FIELD KEY VALUE \n \
        ')
        sys.exit(0)

    config_file_path = sys.argv[1]
    field = sys.argv[2]
    key = sys.argv[3]
    if len(sys.argv) == 4:
        print( read_config(config_file_path, field, key))
    else:
        value = sys.argv[4]
        write_config(config_file_path, field, key, value)
