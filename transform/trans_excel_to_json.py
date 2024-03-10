import pandas as pd

# 读取Excel文件
excel_path = './datasets/excel/power_generation_identification_dataset_api2.xlsx'
df = pd.read_excel(excel_path, header=None, skiprows=1)  # 假设Excel文件只有一列且没有标题行

# 初始化一个列表来存储处理后的行
processed_lines = []

# 定义输出JSON文件的路径
output_json_path = './datasets/json/train.json'
# 打开输出文件准备写入
with open(output_json_path, 'w', encoding='utf-8') as f:
    # 写入数组开始标记
    f.write('[')
    # 初始化标记，用于追踪是否是第一个对象，以便于正确放置逗号
    first_object = True
    for index, row in df.iterrows():
        # 获取当前行的数据
        json_str = row[0]
        # 将字符串中的"true"和"false"替换为Python风格的"True"和"False"
        json_str = json_str.replace('true', 'True').replace('false', 'False')
        # 对于数组中的第一个对象之前不加逗号，之后的每个对象前加逗号
        if first_object:
            first_object = False
        # 写入处理后的JSON字符串
        f.write(json_str + ',\n')
    # 写入数组结束标记
    f.write(']')

print(f"Processed JSON lines have been saved to: {output_json_path}")
