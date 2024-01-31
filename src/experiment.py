from datetime import datetime
import sys

def try_experiment(expt_name=""):
    expt_time = datetime.now()
    print("I am trying experiment {expt_name}")
    print(f"Time now is {expt_time}")

    with open("./data/output.log","w") as fo:
        fo.write(f"Conducted experiment {expt_name} at {expt_time}\n")
    

if __name__=='__main__':
    expt_name=sys.argv[1]
    try_experiment(expt_name)