"""
    !=> Numba Method Vectorization

    ?=> https://numba.pydata.org/numba-doc/dev/reference/jit-compilation.html#numba.guvectorize 
"""
import numpy as np
import math
from numba import vectorize, guvectorize


@vectorize
def VectorizedLog(A):
    """
        Normalde tek değer kabul eden bir method, vectorize edilerek çok boyutlu matrisler için kullanılabilir hale geldi.
    """
    return math.log10(A)


@guvectorize(["void(float64[:], float64[:], float64[:])"], "(n),(n)->(n)", target="parallel")
def AddVectors(a, b, result):
    """
        => Guvectorize ise preallocated bir alana sonuçları yazarak element-wise matrix işlemi yerine, her eleman için ayrı işlem yapılması gereken yerlerde kullanışlıdır. 

        => Önemli parametreler: 
            - NumPy generalized-ufunc signature verilmelidir: "(n),(n)->(n)"
            - Metodun parametre ve return değeri tipi: ["void(float64[:], float64[:], float64[:])"]

        => Ayrıca target="parallel" argümanı ile daha performanslı çalıştırılabilir.
    """ 
    for i in range(len(a)):
        result[i] = a[i] + b[i]


if '__main__' == __name__:
    #! Vectorize
    A = np.array(
        [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]
        ]
    )

    try:
        x = math.log10(A)
    except Exception as e:
        print("Hata: ", e)


    result = VectorizedLog(A)
    print("Sonuç:\n ", result)


    #! GuVectorize
    size = 10
    vector_a = np.random.rand(size)
    vector_b = np.random.rand(size)

    # Sonucu almak için boş bir dizi oluştur
    result = np.zeros_like(vector_a)

    AddVectors(vector_a, vector_b, result)

    # Sonuç
    print("\nVector A:", vector_a)
    print("Vector B:", vector_b)
    print("Result:", result)