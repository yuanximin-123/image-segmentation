import os
import subprocess

# 可以生成更完整的
input_folder = "datasets/before"  # 输入文件夹路径，包含多个JSON标记文件
output_folder = "datasets/SegmentationClass"  # 输出文件夹路径，用于保存PNG图像

# 遍历输入文件夹中的JSON标记文件
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        # 构建输入JSON文件的完整路径
        input_path = os.path.join(input_folder, filename)

        # 构建输出PNG图像文件的完整路径
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_filename)

        # 使用labelme_json_to_dataset命令行工具进行转换
        command = f"labelme_json_to_dataset {input_path} -o {output_path}"
        subprocess.run(command, shell=True)