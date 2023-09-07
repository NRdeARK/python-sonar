def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

def txt(x):
    x = " ".join([i[::-1] for i in x.split() ])
    return x

def test_txt():
    assert txt("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert txt("tan tana tannn") == "nat anat nnnat"    
    assert txt("buddy kung") == "yddub gunk"
    assert txt("L0L 1S Tr4ash") == "L0L S1 hs4rT"
     