from contextlib import nullcontext as does_not_raise
from packaging_with_uv_elliotwutingfeng import hello_world


def test_hello_world():
    with does_not_raise():
        hello_world()
