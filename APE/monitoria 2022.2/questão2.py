try:
    n = int(input("digite um número"))
    assert int(n) == n and n > 0, "valor digitado inválido"
    soma = 0
    for johnner in range(1,n+1):
        soma += johnner

    print(soma)
except AssertionError as ae:
    print(ae)
except ValueError:
    print("valor digitado inválido")




