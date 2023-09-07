def t_func(x):
    x = " ".join([i[::-1] for i in x.split() ])
    return x

def test_answer():
    assert t_func("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert t_func("tan tana tannn") == "nat anat nnnat"    
    assert t_func("buddy kung") == "yddub gnuk"
    assert t_func("L0L 1S Tr4sh") == "L0L S1 hs4rT"
     
# test_answer()
print(t_func("L0L 1S Tr4sh"))