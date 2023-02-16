model_list = ['resnet50', 'vgg16', 'resnet101', 'seresnet50', 'densenet', 'mobilenet_v2',
              'efficientnet', 'shufflenet_v2', 'repvgg', 'swin_transformer', 'vit']

model_op_list = {
    'resnet50': ['sgd', 'randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'sum', 'mean', 'mul', 'div'],
    'resnet101': ['sgd', 'randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'sum', 'mean', 'mul', 'div'],
    'seresnet50': ['sgd', 'randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'adaptive_avg_pool2d', 'sigmoid', 'linear', 'cross_entropy', 'sum', 'mean', 'mul', 'div'],
    # densenet is too large to train on 1 GPU
    'densenet': ['randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'max_pool2d', 'cat', 'avg_pool2d'],

    'mobilenet_v2': ['sgd', 'randperm', 'conv2d', 'add', 'batch_norm', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'hardtanh', 'sum', 'mean', 'mul', 'div'],
    'efficientnet': ['sgd', 'randperm', 'conv2d', 'add', 'batch_norm', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'linspace', 'pad', 'sigmoid', 'sum', 'mean', 'mul', 'div'],
    'vgg16': ['sgd', 'randperm', 'conv2d', 'relu', 'batch_norm', 'max_pool2d', 'linear', 'dropout', 'cross_entropy', 'sum', 'mean', 'add', 'mul', 'div'],
    'shufflenet_v2': ['randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'max_pool2d', 'cat', 'transpose', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'sum', 'mean', 'sgd', 'mul', 'div'],
    'repvgg': ['randperm', 'conv2d', 'add', 'batch_norm', 'relu', 'adaptive_avg_pool2d', 'linear', 'cross_entropy', 'sum', 'mean', 'sgd', 'mul', 'div'],
    'swin_transformer': ['linspace', 'arange', 'randperm', 'one_hot', 'mul', 'add', 'conv2d', 'transpose', 'layer_norm', 'dropout',
                         'pad', 'permute', 'linear', 'matmul', 'softmax', 'gelu', 'roll', 'sub', 'ne', 'masked_fill', 'eq', 'rand', 'div', 'floor', 'unfold', 'linear', 'adaptive_avg_pool2d', 'neg',
                         'log_softmax', 'sum', 'mean', 'norm', 'stack', 'reciprocal', 'clamp', 'adamw', 'addcmul', 'sqrt', 'addcdiv'],
    'vit': ['randperm', 'one_hot', 'mul', 'add', 'conv2d', 'transpose', 'expand', 'cat', 'dropout', 'layer_norm', 'linear',
            'permute', 'matmul', 'gelu', 'tanh', 'neg', 'log_softmax', 'sum', 'div', 'mean', 'norm', 'stack', 'reciprocal', 'clamp', 'adamw', 'addcmul', 'sqrt', 'addcdiv']
}
