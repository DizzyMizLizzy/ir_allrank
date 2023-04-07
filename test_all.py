import os
import subprocess

folders = ['listwise']
folds = [1, 2, 3, 4, 5]
configs = ['listwise_approxNDCG.json']

for folder in folders:
    for fold in folds:
        for config in configs:
            config_path = f'configs_2\\{folder}\\fold{fold}\\{config}'
            run_id = 'test_appoxNDCG'
            job_dir = f'test_mq2008\{folder}\\{config}\\fold{fold}'
            model_dir = f'D:\\Programming\\Assignments\\IR\\project\\run\\ir_allrank\\allrankrun_MQ2008\\{folder}\\{config}\\fold{fold}\\results\\run_1\\model.pkl'

            if os.path.exists(config_path):
                print(f'Testing {config} for fold {fold}...')
                cmd = f'python3 test.py --config-file-name {config_path} --run-id {run_id} --job-dir {job_dir} --model {model_dir}'
                result = subprocess.run(cmd, shell=True, text=True)

                if result.returncode != 0:
                    print(f'Error running {config} for fold {fold} in {folder}')
                    exit(1)
            else:
                print(f'Configuration file {config} does not exist in {folder}\\fold{fold}')
