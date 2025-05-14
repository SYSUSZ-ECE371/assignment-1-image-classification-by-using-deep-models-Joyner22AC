import os
import shutil
import random

# Configuration
random.seed(42) 
src_dataset = r'C:\Users\23945\Desktop\Ex1\flower_dataset'
dst_dataset = r'C:\Users\23945\Desktop\Ex1\flower_dataset_imagenet'
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
split_ratio = 0.8

# Create destination directories
train_dir = os.path.join(dst_dataset, 'train')
val_dir = os.path.join(dst_dataset, 'val')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Create annotation files
with open(os.path.join(dst_dataset, 'classes.txt'), 'w') as f:
    f.write('\n'.join(class_names))

train_ann = open(os.path.join(dst_dataset, 'train.txt'), 'w')
val_ann = open(os.path.join(dst_dataset, 'val.txt'), 'w')

# Process each class
for label, cls in enumerate(class_names):
    src_cls_dir = os.path.join(src_dataset, cls)
    if not os.path.exists(src_cls_dir):
        print(f"Warning: Missing class directory {cls}, skipping...")
        continue
    
    # Get all image files
    images = [f for f in os.listdir(src_cls_dir) 
             if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)
    split_idx = int(len(images) * split_ratio)
    
    # Create target directories
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)
    
    # Process training set
    for img in images[:split_idx]:
        src = os.path.join(src_cls_dir, img)
        dst = os.path.join(train_dir, cls, img)
        shutil.copy(src, dst)
        train_ann.write(f'{cls}/{img} {label}\n')
    
    # Process validation set
    for img in images[split_idx:]:
        src = os.path.join(src_cls_dir, img)
        dst = os.path.join(val_dir, cls, img)
        shutil.copy(src, dst)
        val_ann.write(f'{cls}/{img} {label}\n')

# Close annotation files
train_ann.close()
val_ann.close()