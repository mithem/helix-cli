#!/usr/bin/env python3
from tasks import Task
from projects import Project
import add, remove, change, helper, sys, pickle, os, control
import bcolors as bc

items = control.ItemHandler.loadItems()

try:
    print(bc.col.OKGREEN + "\nStarted" + bc.col.ENDC)
    while True:
        control.executeCommand(input().split(" "))
except KeyboardInterrupt:
    control.exitHelix(True)