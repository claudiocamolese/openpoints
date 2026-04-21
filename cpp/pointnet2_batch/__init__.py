import torch

try:
    import pointnet2_batch_cuda as pointnet2_cuda
except Exception:
    pointnet2_cuda = None
