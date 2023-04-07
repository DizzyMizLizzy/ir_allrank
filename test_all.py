import os
import subprocess

folders = ['pointwise', 'pairwise', 'listwise']
folds = [1, 2, 3, 4, 5]
configs = ['pointwise_mse.json', 'pairwise_ranknet.json', 'listwise_approxNDCG.json', 'listwise_neuralNDCG.json']

for folder in folders:
    for fold in folds:
        for config in configs:
            config_path = f'configs\\{folder}\\fold{fold}\\{config}'
            run_id = 'test_1'
            job_dir = f'test_WeightedRanknet\{folder}\\{config}\\fold{fold}'
            model_dir = f'D:\\Programming\\Assignments\\IR\\project\\run\\ir_allrank\\allrankrun_MSLR-WEB10K\\{folder}\\{config}\\fold{fold}\\results\\run_1\\model.pkl'

            if os.path.exists(config_path):
                print(f'Testing {config} for fold {fold}...')
                cmd = f'python3 test.py --config-file-name {config_path} --run-id {run_id} --job-dir {job_dir} --model {model_dir}'
                result = subprocess.run(cmd, shell=True, text=True)

                if result.returncode != 0:
                    print(f'Error running {config} for fold {fold} in {folder}')
                    exit(1)
            else:
                print(f'Configuration file {config} does not exist in {folder}\\fold{fold}')
