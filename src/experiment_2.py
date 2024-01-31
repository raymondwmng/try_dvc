from datetime import datetime
import sys
import yaml

def try_experiment_2(expt_names=[]):
    expt_time = datetime.now()
    print(f"I am trying experiment {'|'.join(expt_names)}")
    print(f"Time now is {expt_time}")

    with open("./data/output_2.log","w") as fo:
        fo.write(f"Conducted experiment {'|'.join(expt_names)} at {expt_time}\n")
    

if __name__=='__main__':
    # expt_name=sys.argv[1]
    with open('./params.yaml') as f:
        params=yaml.safe_load(f)
    expt_names=params['experiment_2']['names']
    try_experiment_2(expt_names)
