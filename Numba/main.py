import math
import numpy as np
from numba import jit, njit, float32, int32
from timeit import timeit


"""
    => Sadece python metodunu @njit ile decorate ettik ve metodun hızlanmasını bekliyoruz. Bunu yapmakla eşdeğer: @jit(nopython=True)
    
    => @jit yerine @njit kullandık çünkü yarı python yarısı jit ile derlenmiş bir metot istemiyoruz.
    
    => Yazdığımız metot tamamen numpy ve numba nın anlayacağı şekilde yazıldığından @njit kullanılıp tamamen derlenebilir.

    => cache=True parametresi ile .nbc ve .nbi cache dosyalarını __pycache__ klasöründe oluşturduk. Eğer programda değişiklik yapmıyorsa bu cacheleme hızlı bir başlangıç saylayabilir.

    => Numba'nın CUDA derlemesi şuan da Beta durumundadır ve Cuda kodları için kullanılabilir.
"""
@njit(cache=True)           
def CalculateDecomposition(A: np.ndarray):
    # LU factorisation
    y = [1.0]
    n = A.shape[0]
    
    for i in range(n):
        y[0] = y[0] * A[i, i]
        for j in range(i+1, n):
            A[j][i] = A[j][i]/A[i][i]
            A[j][i+1:] = A[j][i+1:] - (A[j][i] * A[i][i+1:])


@njit                           #! LAZY
def lazy_hypotenuse(side1: int, side2: int) -> float:
    """
        JIT derleyicisine daha önceden parametre bilgisi hakkında bir şey söylemedik.
    """
    return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))


@njit(float32(int32, int32))    #! EAGER @jit(<return>(<argument1>, <argument2>,...))
def eager_hypotenuse(side1: int, side2: int) -> float:
    """
        JIT derleyicisine önceden metodun input ve return değeri hakkında bilgi verdik.
    """
    return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2)) 


if "__main__" == __name__:
    arr = np.random.uniform(size=(100, 100))

    func = lambda: [CalculateDecomposition(arr.copy()) for i in range(1000)]
    ETA = timeit(func, globals=globals(), number=1)
    print(ETA)
