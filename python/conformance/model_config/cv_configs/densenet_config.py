from ...config import Genfunc
from ...dtype import Dtype

densenet_config = {
    'mean': dict(
        name=["mean"],
        interface=["torch.Tensor"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(64, 3, 7, 7), (64,), (128, 64, 1, 1), (128,), (32, 128, 3, 3), (96,), (128, 96, 1, 1), (128, 128, 1, 1), (160,), (128, 160, 1, 1), (192,), (128, 192, 1, 1), (224,), (128, 224, 1, 1), (256,), (128, 256, 1, 1), (288,), (128, 288, 1, 1), (320,), (128, 320, 1, 1), (352,), (128, 352, 1, 1), (384,), (128, 384, 1, 1), (416,), (128, 416, 1, 1), (448,), (128, 448, 1, 1), (480,), (128, 480, 1, 1), (512,), (128, 512, 1, 1), (544,), (128, 544, 1, 1), (576,), (128, 576, 1, 1), (608,), (128, 608, 1, 1), (640,), (128, 640, 1, 1), (672,), (128, 672, 1, 1), (704,), (128, 704, 1, 1), (736,), (128, 736, 1, 1), (768,), (128, 768, 1, 1), (800,), (128, 800, 1, 1), (832,), (128, 832, 1, 1), (864,), (128, 864, 1, 1), (896,), (128, 896, 1, 1), (928,), (128, 928, 1, 1), (960,), (128, 960, 1, 1), (992,), (128, 992, 1, 1), (256, 512, 1, 1), (1024,), (512, 1024, 1, 1), (1000, 1024), (1000,), ()],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'normal_': dict(
        name=["normal_"],
        no_output_ref=True,
        para=dict(
            size=[(1000, 1024)],
            mean=[0],
            std=[0.01],
        ),
    ),

    'fill_': dict(
        name=["fill_"],
        interface=["torch.Tensor"],
        para=dict(
            value=[0],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(1000,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'randperm': dict(
        name=["randperm"],
        no_output_ref=True,
        para=dict(
            n=[1281167],
        ),
    ),

    'flip': dict(
        name=["flip"],
        interface=["torch.Tensor"],
        para=dict(
            dims=[(1,)],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(256, 3, 224, 224)],
                    "dtype": [Dtype.uint8],
                    "gen_fn": Genfunc.randint,
                },
            ],
        ),
    ),

    'sub': dict(
        name=["sub"],
        interface=["torch.Tensor"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(256, 3, 224, 224)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["other"],
                    "shape": [(3, 1, 1)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'div': dict(
        name=["div"],
        interface=["torch.Tensor"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(256, 3, 224, 224)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["other"],
                    "shape": [(3, 1, 1)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'conv2d': dict(
        name=["conv2d"],
        para=dict(
            bias=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            stride=[(2, 2), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)],
            padding=[(3, 3), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
            dilation=[(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)],
            groups=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 3, 224, 224), (256, 64, 56, 56), (256, 128, 56, 56), (256, 96, 56, 56), (256, 128, 56, 56), (256, 160, 56, 56), (256, 192, 56, 56), (256, 224, 56, 56), (256, 256, 56, 56), (256, 128, 28, 28), (256, 128, 28, 28), (256, 160, 28, 28), (256, 192, 28, 28), (256, 224, 28, 28), (256, 256, 28, 28), (256, 288, 28, 28), (256, 320, 28, 28), (256, 352, 28, 28), (256, 384, 28, 28), (256, 416, 28, 28), (256, 448, 28, 28), (256, 480, 28, 28), (256, 512, 28, 28), (256, 256, 14, 14), (256, 128, 14, 14), (256, 288, 14, 14), (256, 320, 14, 14), (256, 352, 14, 14), (256, 384, 14, 14), (256, 416, 14, 14), (256, 448, 14, 14), (256, 480, 14, 14), (256, 512, 14, 14), (256, 544, 14, 14), (256, 576, 14, 14), (256, 608, 14, 14), (256, 640, 14, 14), (256, 672, 14, 14), (256, 704, 14, 14), (256, 736, 14, 14), (256, 768, 14, 14), (256, 800, 14, 14), (256, 832, 14, 14), (256, 864, 14, 14), (256, 896, 14, 14), (256, 928, 14, 14), (256, 960, 14, 14), (256, 992, 14, 14), (256, 1024, 14, 14), (256, 512, 7, 7), (256, 128, 7, 7), (256, 544, 7, 7), (256, 576, 7, 7), (256, 608, 7, 7), (256, 640, 7, 7), (256, 672, 7, 7), (256, 704, 7, 7), (256, 736, 7, 7), (256, 768, 7, 7), (256, 800, 7, 7), (256, 832, 7, 7), (256, 864, 7, 7), (256, 896, 7, 7), (256, 928, 7, 7), (256, 960, 7, 7), (256, 992, 7, 7)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["weight"],
                    "requires_grad": [True],
                    "shape": [(64, 3, 7, 7), (128, 64, 1, 1), (32, 128, 3, 3), (128, 96, 1, 1), (128, 128, 1, 1), (128, 160, 1, 1), (128, 192, 1, 1), (128, 224, 1, 1), (128, 256, 1, 1), (128, 128, 1, 1), (32, 128, 3, 3), (128, 160, 1, 1), (128, 192, 1, 1), (128, 224, 1, 1), (128, 256, 1, 1), (128, 288, 1, 1), (128, 320, 1, 1), (128, 352, 1, 1), (128, 384, 1, 1), (128, 416, 1, 1), (128, 448, 1, 1), (128, 480, 1, 1), (256, 512, 1, 1), (128, 256, 1, 1), (32, 128, 3, 3), (128, 288, 1, 1), (128, 320, 1, 1), (128, 352, 1, 1), (128, 384, 1, 1), (128, 416, 1, 1), (128, 448, 1, 1), (128, 480, 1, 1), (128, 512, 1, 1), (128, 544, 1, 1), (128, 576, 1, 1), (128, 608, 1, 1), (128, 640, 1, 1), (128, 672, 1, 1), (128, 704, 1, 1), (128, 736, 1, 1), (128, 768, 1, 1), (128, 800, 1, 1), (128, 832, 1, 1), (128, 864, 1, 1), (128, 896, 1, 1), (128, 928, 1, 1), (128, 960, 1, 1), (128, 992, 1, 1), (512, 1024, 1, 1), (128, 512, 1, 1), (32, 128, 3, 3), (128, 544, 1, 1), (128, 576, 1, 1), (128, 608, 1, 1), (128, 640, 1, 1), (128, 672, 1, 1), (128, 704, 1, 1), (128, 736, 1, 1), (128, 768, 1, 1), (128, 800, 1, 1), (128, 832, 1, 1), (128, 864, 1, 1), (128, 896, 1, 1), (128, 928, 1, 1), (128, 960, 1, 1), (128, 992, 1, 1)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'add': dict(
        name=["add"],
        interface=["torch.Tensor"],
        para=dict(
            other=[1],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [()],
                    "dtype": [Dtype.int64],
                    "gen_fn": Genfunc.randint,
                },
            ],
        ),
    ),

    'batch_norm': dict(
        name=["batch_norm"],
        para=dict(
            training=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            momentum=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            eps=[1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 64, 112, 112), (256, 64, 56, 56), (256, 128, 56, 56), (256, 96, 56, 56), (256, 160, 56, 56), (256, 192, 56, 56), (256, 224, 56, 56), (256, 256, 56, 56), (256, 128, 28, 28), (256, 160, 28, 28), (256, 192, 28, 28), (256, 224, 28, 28), (256, 256, 28, 28), (256, 288, 28, 28), (256, 320, 28, 28), (256, 352, 28, 28), (256, 384, 28, 28), (256, 416, 28, 28), (256, 448, 28, 28), (256, 480, 28, 28), (256, 512, 28, 28), (256, 256, 14, 14), (256, 128, 14, 14), (256, 288, 14, 14), (256, 320, 14, 14), (256, 352, 14, 14), (256, 384, 14, 14), (256, 416, 14, 14), (256, 448, 14, 14), (256, 480, 14, 14), (256, 512, 14, 14), (256, 544, 14, 14), (256, 576, 14, 14), (256, 608, 14, 14), (256, 640, 14, 14), (256, 672, 14, 14), (256, 704, 14, 14), (256, 736, 14, 14), (256, 768, 14, 14), (256, 800, 14, 14), (256, 832, 14, 14), (256, 864, 14, 14), (256, 896, 14, 14), (256, 928, 14, 14), (256, 960, 14, 14), (256, 992, 14, 14), (256, 1024, 14, 14), (256, 512, 7, 7), (256, 128, 7, 7), (256, 544, 7, 7), (256, 576, 7, 7), (256, 608, 7, 7), (256, 640, 7, 7), (256, 672, 7, 7), (256, 704, 7, 7), (256, 736, 7, 7), (256, 768, 7, 7), (256, 800, 7, 7), (256, 832, 7, 7), (256, 864, 7, 7), (256, 896, 7, 7), (256, 928, 7, 7), (256, 960, 7, 7), (256, 992, 7, 7), (256, 1024, 7, 7)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["running_mean"],
                    "shape": [(64,), (64,), (128,), (96,), (160,), (192,), (224,), (256,), (128,), (160,), (192,), (224,), (256,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (256,), (128,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,), (512,), (128,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["running_var"],
                    "shape": [(64,), (64,), (128,), (96,), (160,), (192,), (224,), (256,), (128,), (160,), (192,), (224,), (256,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (256,), (128,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,), (512,), (128,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["weight"],
                    "requires_grad": [True],
                    "shape": [(64,), (64,), (128,), (96,), (160,), (192,), (224,), (256,), (128,), (160,), (192,), (224,), (256,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (256,), (128,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,), (512,), (128,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["bias"],
                    "requires_grad": [True],
                    "shape": [(64,), (64,), (128,), (96,), (160,), (192,), (224,), (256,), (128,), (160,), (192,), (224,), (256,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (256,), (128,), (288,), (320,), (352,), (384,), (416,), (448,), (480,), (512,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,), (512,), (128,), (544,), (576,), (608,), (640,), (672,), (704,), (736,), (768,), (800,), (832,), (864,), (896,), (928,), (960,), (992,), (1024,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'relu': dict(
        name=["relu"],
        para=dict(
            inplace=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(256, 64, 112, 112), (256, 64, 56, 56), (256, 128, 56, 56), (256, 96, 56, 56), (256, 160, 56, 56), (256, 192, 56, 56), (256, 224, 56, 56), (256, 256, 56, 56), (256, 128, 28, 28), (256, 160, 28, 28), (256, 192, 28, 28), (256, 224, 28, 28), (256, 256, 28, 28), (256, 288, 28, 28), (256, 320, 28, 28), (256, 352, 28, 28), (256, 384, 28, 28), (256, 416, 28, 28), (256, 448, 28, 28), (256, 480, 28, 28), (256, 512, 28, 28), (256, 256, 14, 14), (256, 128, 14, 14), (256, 288, 14, 14), (256, 320, 14, 14), (256, 352, 14, 14), (256, 384, 14, 14), (256, 416, 14, 14), (256, 448, 14, 14), (256, 480, 14, 14), (256, 512, 14, 14), (256, 544, 14, 14), (256, 576, 14, 14), (256, 608, 14, 14), (256, 640, 14, 14), (256, 672, 14, 14), (256, 704, 14, 14), (256, 736, 14, 14), (256, 768, 14, 14), (256, 800, 14, 14), (256, 832, 14, 14), (256, 864, 14, 14), (256, 896, 14, 14), (256, 928, 14, 14), (256, 960, 14, 14), (256, 992, 14, 14), (256, 1024, 14, 14), (256, 512, 7, 7), (256, 128, 7, 7), (256, 544, 7, 7), (256, 576, 7, 7), (256, 608, 7, 7), (256, 640, 7, 7), (256, 672, 7, 7), (256, 704, 7, 7), (256, 736, 7, 7), (256, 768, 7, 7), (256, 800, 7, 7), (256, 832, 7, 7), (256, 864, 7, 7), (256, 896, 7, 7), (256, 928, 7, 7), (256, 960, 7, 7), (256, 992, 7, 7), (256, 1024, 7, 7)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'max_pool2d': dict(
        name=["max_pool2d"],
        para=dict(
            kernel_size=[3],
            stride=[2],
            padding=[1],
            dilation=[1],
            ceil_mode=[False],
            return_indices=[False],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 64, 112, 112)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'cat': dict(
        name=["cat"],
        interface=["torch"],
        para=dict(
            dim=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["tensors"],
                    "shape": [((256, 64, 56, 56),), ((256, 64, 56, 56), (256, 32, 56, 56)), ((256, 64, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56)), ((256, 64, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56)), ((256, 64, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56)), ((256, 64, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56)), ((256, 64, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56), (256, 32, 56, 56)), ((256, 128, 28, 28),), ((256, 128, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 128, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28), (256, 32, 28, 28)), ((256, 256, 14, 14),), ((256, 256, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 256, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14), (256, 32, 14, 14)), ((256, 512, 7, 7),), ((256, 512, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7)), ((256, 512, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7), (256, 32, 7, 7))],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
            seq_name='tensors',
        ),
    ),

    'avg_pool2d': dict(
        name=["avg_pool2d"],
        para=dict(
            kernel_size=[2, 2, 2],
            stride=[2, 2, 2],
            padding=[0, 0, 0],
            ceil_mode=[False, False, False],
            count_include_pad=[True, True, True],
            divisor_override=[None, None, None],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 128, 56, 56), (256, 256, 28, 28), (256, 512, 14, 14)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'adaptive_avg_pool2d': dict(
        name=["adaptive_avg_pool2d"],
        para=dict(
            output_size=[(1, 1)],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 1024, 7, 7)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'linear': dict(
        name=["linear"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 1024)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["weight"],
                    "requires_grad": [True],
                    "shape": [(1000, 1024)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["bias"],
                    "requires_grad": [True],
                    "shape": [(1000,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'cat_1': dict(
        name=["cat"],
        interface=["torch"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["tensors"],
                    "shape": [((1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,))],
                    "dtype": [Dtype.int64],
                    "gen_fn": Genfunc.randint,
                },
            ],
            seq_name='tensors',
        ),
    ),

    'cross_entropy': dict(
        name=["cross_entropy"],
        para=dict(
            reduction=['none'],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "requires_grad": [True],
                    "shape": [(256, 1000)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["target"],
                    "shape": [(256,)],
                    "dtype": [Dtype.int64],
                    "gen_fn": Genfunc.randint,
                },
            ],
        ),
    ),

    'sum': dict(
        name=["sum"],
        interface=["torch.Tensor"],
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(256,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'div_1': dict(
        name=["div"],
        interface=["torch.Tensor"],
        para=dict(
            other=[256, 1],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [(), ()],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'mul': dict(
        name=["mul"],
        interface=["torch.Tensor"],
        para=dict(
            other=[1.0],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [()],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'add_1': dict(
        name=["add"],
        interface=["torch.Tensor"],
        para=dict(
            other=[0],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["input"],
                    "shape": [()],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'sgd': dict(
        name=["sgd"],
        interface=["CustomizedTest"],
        para=dict(
            nesterov=[False for i in range(67)],
            lr=[0.1 for i in range(67)],
            momentum=[0.9 for i in range(67)],
            weight_decay=[0.0001 for i in range(67)],
            dampening=[0 for i in range(67)],
        ),
        tensor_para=dict(
            args=[
                {
                    "ins": ["param", "param_grad"],
                    "shape": [(64, 3, 7, 7), (64,), (128, 64, 1, 1), (128,), (32, 128, 3, 3), (96,), (128, 96, 1, 1), (128, 128, 1, 1), (160,), (128, 160, 1, 1), (192,), (128, 192, 1, 1), (224,), (128, 224, 1, 1), (256,), (128, 256, 1, 1), (288,), (128, 288, 1, 1), (320,), (128, 320, 1, 1), (352,), (128, 352, 1, 1), (384,), (128, 384, 1, 1), (416,), (128, 416, 1, 1), (448,), (128, 448, 1, 1), (480,), (128, 480, 1, 1), (512,), (128, 512, 1, 1), (544,), (128, 544, 1, 1), (576,), (128, 576, 1, 1), (608,), (128, 608, 1, 1), (640,), (128, 640, 1, 1), (672,), (128, 672, 1, 1), (704,), (128, 704, 1, 1), (736,), (128, 736, 1, 1), (768,), (128, 768, 1, 1), (800,), (128, 800, 1, 1), (832,), (128, 832, 1, 1), (864,), (128, 864, 1, 1), (896,), (128, 896, 1, 1), (928,), (128, 928, 1, 1), (960,), (128, 960, 1, 1), (992,), (128, 992, 1, 1), (256, 512, 1, 1), (1024,), (512, 1024, 1, 1), (1000, 1024), (1000,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
                {
                    "ins": ["buf"],
                    "shape": [(64, 3, 7, 7), (64,), (128, 64, 1, 1), (128,), (32, 128, 3, 3), (96,), (128, 96, 1, 1), (128, 128, 1, 1), (160,), (128, 160, 1, 1), (192,), (128, 192, 1, 1), (224,), (128, 224, 1, 1), (256,), (128, 256, 1, 1), (288,), (128, 288, 1, 1), (320,), (128, 320, 1, 1), (352,), (128, 352, 1, 1), (384,), (128, 384, 1, 1), (416,), (128, 416, 1, 1), (448,), (128, 448, 1, 1), (480,), (128, 480, 1, 1), (512,), (128, 512, 1, 1), (544,), (128, 544, 1, 1), (576,), (128, 576, 1, 1), (608,), (128, 608, 1, 1), (640,), (128, 640, 1, 1), (672,), (128, 672, 1, 1), (704,), (128, 704, 1, 1), (736,), (128, 736, 1, 1), (768,), (128, 768, 1, 1), (800,), (128, 800, 1, 1), (832,), (128, 832, 1, 1), (864,), (128, 864, 1, 1), (896,), (128, 896, 1, 1), (928,), (128, 928, 1, 1), (960,), (128, 960, 1, 1), (992,), (128, 992, 1, 1), (256, 512, 1, 1), (1024,), (512, 1024, 1, 1), (1000, 1024), (1000,)],
                    "dtype": [Dtype.float32],
                    "gen_fn": Genfunc.randn,
                },
            ],
        ),
    ),

    'arange': dict(
        name=["arange"],
        interface=["torch"],
        para=dict(
            end=[50000],
        ),
    ),

}
