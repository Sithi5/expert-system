from expert_system import main

def test_simple_1():
	assert "B resolved as True" == main(open("files/test_simple_1"), False)

def test_simple_2():
	assert "B resolved as True" == main(open("files/test_simple_2"), False)

def test_simple_3():
	assert "B resolved as True" == main(open("files/test_simple_3"), False)

def test_simple_4():
	assert "B resolved as True" == main(open("files/test_simple_4"), False)

def test_simple_5():
	assert "B resolved as True" == main(open("files/test_simple_5"), False)
