# -*- coding:utf-8 -*-
import json
import os

list = {
    "int" : "int",
    "smallint" : "int",
    "bigint" : "int",

    "bit" : "boolean",

    "nvarchar(4)" : "string",
    "nvarchar(6)" : "string",
    "nvarchar(8)" : "string",
    "nvarchar(10)" : "string",
    "nvarchar(12)" : "string",
    "nvarchar(16)" : "string",
    "nvarchar(20)" : "string",
    "nvarchar(24)" : "string",
    "nvarchar(32)" : "string",
    "nvarchar(48)" : "string",
    "nvarchar(128)" : "string",
    "nvarchar(1024)" : "string",
    "nvarchar(MAX)" : "string",

    "varchar(8)" : "string",
    "varchar(10)" : "string",
    "varchar(12)" : "string",
    "varchar(16)" : "string",
    "varchar(32)" : "string",
    "varchar(40)" : "string",
    "varchar(64)" : "string",
    "varchar(128)" : "string",
    "varchar(200)" : "string",
    "varchar(1024)": "string",
    "varchar(MAX)" : "string",

    "smalldatetime": "string"
}

def parse_file(file):
    rFile = open(file, "r")
    allLine = rFile.readlines()
    rFile.close()

    comlumn = []
    for line in allLine:
        comlumn.append(line.strip('\n'))
    return comlumn

def output(comlumn):
    str = '","'.join(comlumn)
    str = '"'+str+'"'
    return str

def output2():
    wFile = open('out.dat', "w")
    type = parse_file('type.dat')
    name = parse_file('name.dat')

    for i in range(len(type)):
        type_value = list.get(type[i])
        if type_value == None:
            print type[i]
        line = {"type":type_value,"name":name[i]}
        wFile.write(json.dumps(line, indent=4) + ',\n')
    wFile.seek(-3, os.SEEK_END)
    wFile.truncate()
    wFile.close()

def parse_json(file):
    flag = 1
    rFile = open(file, "r")
    json_value = json.load(rFile)
    for value in json_value["job"]["content"][0]["writer"]["parameter"]["column"]:
        if flag:
            print ' '+value['name']+' '+value["type"]
            flag = 0
        else:
            print ',' + value['name'] + ' ' + value["type"]

parse_json('D:\\tables\\host.json')