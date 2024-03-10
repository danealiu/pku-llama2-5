import datasets

  
# 加载samsum数据集  
#dataset = datasets.load_dataset("https://hf-mirror.com/datasets/samsum")
# 将 https://hf-mirror.com/datasets/samsum/blob/main/samsum.py 放到  ~/.cache/huggingface/datasets/samsum/samsum.py
dataset = datasets.load_dataset("https://hf-mirror.com/datasets/samsum")
# dataset = datasets.load_dataset("~/.cache/huggingface/datasets/samsum/samsum.py")


print(dataset)
  
# 显示数据集的一些信息  
print(dataset)  
  
# 如果你想查看一些样本，你可以这样做：  
for sample in dataset["train"][:5]:  
    print(sample)