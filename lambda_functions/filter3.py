"""Filtering list of text items"""
teams = ["Spartak", "CSKA", "Zenit", "ROSTOV", "AMKAR"]
short = list(filter(lambda x: len(x) < 5, teams))
print(short)