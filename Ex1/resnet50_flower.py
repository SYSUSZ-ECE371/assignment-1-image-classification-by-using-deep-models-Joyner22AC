# resnet50_flower.py

# 继承基础配置（注意路径需与你的项目结构一致）
_base_ = [
    'C:/Users/23945/Desktop/Ex1/mmpretrain/configs/resnet/resnet50_8xb32_in1k.py'  # 假设基础配置在上级目录的 configs 文件夹中
]

# ------ 1. 修改模型配置：调整分类头类别数 ------
model = dict(
    head=dict(
        num_classes=5,  # 花卉数据集有 5 个类别
        topk=(1,),      # 只计算 top-1 准确率
    )
)

# ------ 2. 修改数据集配置 ------
# 数据集根目录（根据实际路径调整）
data_root = 'C:/Users/23945/Desktop/Ex1/flower_dataset/'

# 训练集配置
train_dataloader = dict(
    dataset=dict(
        ann_file='C:/Users/23945/Desktop/Ex1/flower_dataset/train.txt',          # 训练集标注文件
        data_prefix=data_root + 'train',  # 训练集图片路径
    )
)

# 验证集配置
val_dataloader = dict(
    dataset=dict(
        ann_file='C:/Users/23945/Desktop/Ex1/flower_dataset/val.txt',            # 验证集标注文件
        data_prefix=data_root + 'val',    # 验证集图片路径
    )
)

# 测试集配置（可选）
test_dataloader = val_dataloader  # 如果不需要测试集，直接复用验证集配置

# 修改评估指标（仅使用 top-1 准确率）
val_evaluator = dict(type='Accuracy', topk=(1,))

# ------ 3. 修改学习率策略 ------
# 优化器配置（减小学习率）
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
)

# 训练轮次（减少为 10 轮）
train_cfg = dict(max_epochs=10)

# ------ 4. 加载预训练模型 ------
# 从 Model Zoo 下载预训练权重（例如 ResNet-50）
# 下载链接：https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb32_in1k_20210831-ea4938fc.pth
load_from = 'C:/Users/23945/Desktop/Ex1/resnet50_8xb32_in1k.pth'  # 替换为你的权重路径