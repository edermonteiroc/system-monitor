from getsystem import get_CPU_model

def test_get_cpu_model():
    assert isinstance(get_CPU_model(), str)
