"""Track AI/ML learning topics. Usage: python tracker.py add 'Linear regression' --confidence 2"""
import argparse,csv
from datetime import date,timedelta
from pathlib import Path
DB=Path("topics.csv")
def add(topic,confidence):
 new=not DB.exists()
 with DB.open("a",newline="",encoding="utf-8") as f:
  w=csv.writer(f)
  if new:w.writerow(["topic","confidence_1_to_5","added_on","revise_on"])
  w.writerow([topic,confidence,date.today().isoformat(),(date.today()+timedelta(days=2)).isoformat()])
 print("Added:",topic)
def show():
 if not DB.exists():print("No topics yet.");return
 with DB.open(encoding="utf-8") as f:
  for row in csv.DictReader(f):print(f'{row["topic"]} | confidence {row["confidence_1_to_5"]}/5 | revise {row["revise_on"]}')
p=argparse.ArgumentParser();s=p.add_subparsers(dest="cmd",required=True);a=s.add_parser("add");a.add_argument("topic");a.add_argument("--confidence",type=int,choices=range(1,6),default=3);s.add_parser("list");x=p.parse_args();add(x.topic,x.confidence) if x.cmd=="add" else show()