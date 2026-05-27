import os

def test_all_lab3_plots_exist():
    
    import lab3.main
    
    assert os.path.exists('iris_scatter.png')
    assert os.path.exists('co2_dynamics.png')
    assert os.path.exists('wine_scatter.png')
    assert os.path.exists('elnino_dynamics.png')
