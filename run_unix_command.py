#!/usr/bin/python

import os
import re
import subprocess

DEBUG = False

def _run_cmd(cmd, process=None):
    if process == None:
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        new_process = subprocess.Popen(cmd, stdin=process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.stdout.close()
        return new_process

def _decode_cmd(process):
    assert process is not None
    output, error = process.communicate()
    if DEBUG: print(output)
    if error.decode("ascii") != "":
        print("An error occurred, stopping progress\n")
        print(error.decode("ascii"))
        exit()
    if DEBUG: print(output.decode("ascii"))
    return output.decode("ascii")

def _cmd_to_array(str_cmd):
    splitted_cmd = str_cmd.split("|")
    cmd = []
    for parts_without_pipe in splitted_cmd :
        splitted_part_without_pipe = [p for p in re.split(r"( |\'[\s\S]*?\'|'.*?')", parts_without_pipe) if p.strip()]
        if DEBUG: print(splitted_part_without_pipe)
        seperate_cmd = []
        for constructs_for_cmd in splitted_part_without_pipe:
            constructs_for_cmd = constructs_for_cmd.replace("'", "")
            seperate_cmd.append(constructs_for_cmd)
        cmd.append(seperate_cmd)
    return cmd

def run_unix_cmd(str_cmd):
    """
    Input: string - unix command to execute
    example given: "ps -eaf | grep jboss"
    Output: result of executed command
    """
    cmd = _cmd_to_array(str_cmd)
    process = None
    for partial_command_to_run in cmd:
        if DEBUG: print(partial_command_to_run)
        process = _run_cmd(partial_command_to_run, process)
    return _decode_cmd(process)

