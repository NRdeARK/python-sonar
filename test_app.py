def func(x):
    x = " ".join([i[::-1] for i in x.split() ])
    return x

def test_answer():
    assert func("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert func("tan tana tannn") == "nat anat nnnat"    
    assert func("buddy kung") == "yddub gunk"
    assert func("L0L 1S Tr4ash") == "L0L S1 hs4rT"
     