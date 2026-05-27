import os

def test_all_lab3_plots_exist():
    import lab3.main
    
    assert os.path.exists('lab3/iris_scatter.png')
    assert os.path.exists('lab3/co2_dynamics.png')
    assert os.path.exists('lab3/wine_scatter.png')
    assert os.path.exists('lab3/elnino_dynamics.png')
