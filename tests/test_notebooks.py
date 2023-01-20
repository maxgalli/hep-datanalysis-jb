# https://github.com/matthewfeickert/Statistics-Notes/blob/main/tests/test_notebooks.py
import papermill as pm
import pytest


@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
    }

def test_probability(common_kwargs):
    pm.execute_notebook("book/probability.ipynb", **common_kwargs)

def test_pdfs(common_kwargs):
    pm.execute_notebook("book/probabilityDistributions.ipynb", **common_kwargs)

def test_errors(common_kwargs):
    pm.execute_notebook("book/errors.ipynb", **common_kwargs)

def test_montecarlo(common_kwargs):
    pm.execute_notebook("book/monteCarlo.ipynb", **common_kwargs)

def test_inference(common_kwargs):
    pm.execute_notebook("book/inference.ipynb", **common_kwargs)

def test_likelihood(common_kwargs):
    pm.execute_notebook("book/likelihood.ipynb", **common_kwargs)