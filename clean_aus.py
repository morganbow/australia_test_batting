# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("australia_test_batting.csv")

#career length

df["start_career"] = pd.to_numeric(df["Career Span"].apply(lambda x: x.split("-")[0]))
df["end_career"] = pd.to_numeric(df["Career Span"].apply(lambda x: x.split("-")[1]))

df["career_length"] = (df.end_career - df.start_career) + 1
#career midpoint

df["career_midpoint"] = ((df.end_career + df.start_career) / 2).astype(int)
#remove 0 innings

df = df[df["Runs"] != "-"]
#matches per year: to find schedule intensity

df["matches_per_year"] = pd.to_numeric(df["Matches"]) / df["career_length"] 

## % of 50s converted to 100s

df["50_convergences"] =  (pd.to_numeric(df["100s"])) / (pd.to_numeric(df["100s"]) + pd.to_numeric(df["50s"]))

#remobe - from ave

df = df[df["Average"] != "-"]

# remove * from HS

df["HS"] = df["HS"].apply(lambda x: x.replace("*", ""))


df.to_csv("australia_test_batting_cleaned.csv", index = False)