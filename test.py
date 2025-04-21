

# import os
# import shutil
#
# # 源文件夹（包含多个子文件夹）
# source_root = "datasets/SegmentationClass"  # 修改为你的源文件夹路径
# # 目标文件夹（存放重命名后的图片）
# destination_folder = "VOCdevkit/VOC2007/SegmentationClass"  # 修改为你的目标文件夹路径
#
# # 确保目标文件夹存在
# os.makedirs(destination_folder, exist_ok=True)
#
# # 遍历源文件夹下的所有子文件夹
# for folder_name in os.listdir(source_root):
#     folder_path = os.path.join(source_root, folder_name)
#     if os.path.isdir(folder_path):  # 只处理文件夹
#         label_path = os.path.join(folder_path, "label.png")  # 假设图片名称为 "label"
#
#         if os.path.exists(label_path):  # 确保文件存在
#             # 去掉文件夹名的 .png 后缀（如果有的话）
#             clean_folder_name = folder_name.removesuffix(".png")
#
#             # 获取 label 图片的扩展名（如果无扩展名，默认 .png）
#             ext = os.path.splitext(label_path)[-1] or ".png"
#             new_file_name = f"{clean_folder_name}{ext}"  # 以清理后的文件夹名命名
#
#             # 目标文件路径
#             new_file_path = os.path.join(destination_folder, new_file_name)
#
#             # 复制并重命名文件
#             shutil.copy(label_path, new_file_path)
#             print(f"已处理: {label_path} -> {new_file_path}")
#         else:
#             print(f"警告: {label_path} 不存在")
#
# print("批量重命名完成！")

import os

# 图片所在的文件夹
image_folder = "VOCdevkit\VOC2007\JPEGImages"  # 修改为你的图片文件夹路径
# 输出的 txt 文件路径
output_txt = "VOCdevkit/VOC2007/ImageSets/Segmentation/train.txt"  # 修改为你的目标 txt 文件路径

# 获取所有图片文件（假设常见格式为 jpg、png、jpeg、bmp、gif 等）
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
image_files = [os.path.splitext(f)[0] for f in os.listdir(image_folder) if os.path.splitext(f)[-1].lower() in image_extensions]

# 将文件名（无后缀）写入 txt，每行一个
with open(output_txt, "w", encoding="utf-8") as f:
    for image_name in image_files:
        f.write(image_name + "\n")

print(f"图片文件名（无后缀）已写入 {output_txt}")
