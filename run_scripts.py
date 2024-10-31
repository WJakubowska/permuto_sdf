import subprocess


program = './permuto_sdf_py/train_permuto_sdf.py --comp_name comp_3 --no_viewer --exp_info default'


parameters_list = [
    '--dataset nerf --scene chair --config_file /workspace/permuto_sdf/config/train_permuto_sdf_chair.cfg',
    '--dataset nerf --scene drums --config_file /workspace/permuto_sdf/config/train_permuto_sdf_drums.cfg',
    '--dataset nerf --scene ficus --config_file /workspace/permuto_sdf/config/train_permuto_sdf_ficus.cfg',
    '--dataset nerf --scene hotdog --config_file /workspace/permuto_sdf/config/train_permuto_sdf_hotdog.cfg',
    '--dataset nerf --scene materials --config_file /workspace/permuto_sdf/config/train_permuto_sdf_materials.cfg',
    '--dataset nerf --scene mic --config_file /workspace/permuto_sdf/config/train_permuto_sdf_mic.cfg',
    '--dataset nerf --scene ship --config_file /workspace/permuto_sdf/config/train_permuto_sdf_ship.cfg',
    '--dataset nerf --scene lego --config_file /workspace/permuto_sdf/config/train_permuto_sdf_lego.cfg'
]


for i, params in enumerate(parameters_list):

    command = f"python {program} {params}"
    print("Run command: ", command)
    
    output_file = f"output_{i+1}.txt"
    with open(output_file, 'w') as f:
        subprocess.run(command, shell=True, stdout=f, stderr=subprocess.STDOUT, text=True)

    print(f"RUN: {i+1}: SAVE: {output_file}")
