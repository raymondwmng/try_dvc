from datetime import datetime
import sys
import yaml

def try_experiment(expt_name=""):
    expt_time = datetime.now()
    print(f"I am trying experiment {expt_name}")
    print(f"Time now is {expt_time}")

    with open("./data/output.log","w") as fo:
        fo.write(f"Conducted experiment {expt_name} at {expt_time}\n")
    

if __name__=='__main__':
    # expt_name=sys.argv[1]
    with open('./params.yaml') as f:
        params=yaml.safe_load(f)
    expt_name=params['experiment']['name']
    try_experiment(expt_name)
