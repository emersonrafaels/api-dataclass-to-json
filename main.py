from src.models.models import Fornecedor, Produto
from src.utils.utils import to_json, is_json
from dataclasses import asdict
from typing import List

# Exemplos de uso para casos não-lista (objeto único)
def exemplo_objeto():
    """
    Exemplo de conversão de um objeto único (Produto) para JSON e validação.
    """
    fornecedor = Fornecedor(3, "Fornecedor Único")
    produto = Produto("Borracha", fornecedor)
    
    print("Exemplo Produto único:")
    
    # Convertendo o objeto produto para JSON
    json_produto = to_json(produto)
    print(json_produto)
    
    # Validando se o JSON é válido
    print("É JSON válido?", is_json(json_produto))

# Exemplos de uso para casos lista
def exemplo_lista():
    """
    Exemplo de conversão de uma lista de objetos (Produto) para JSON e validação.
    """
    lista_produtos = [
        Produto("Caderno", Fornecedor(4, "Fornecedor Papel")),
        Produto("Régua", Fornecedor(5, "Fornecedor Medidas"))
    ]
    
    print("Exemplo Lista de Produtos:")

    # Convertendo a lista de produtos para JSON
    json_lista = to_json(lista_produtos)
    print(json_lista)
    
    # Validando se o JSON é válido
    print("É JSON válido?", is_json(json_lista))
    
def exemplo_lista_produtos_fornecedores():

    # Lista de fornecedores
    fornecedores: List[Fornecedor] = [
        Fornecedor(1, "Fornecedor XPTO"),
        Fornecedor(2, "Fornecedor ABC")
    ]
    
    # Lista de produtos
    produtos: List[Produto] = [
        Produto("Caneta", fornecedores[0]),
        Produto("Lápis", fornecedores[1])
    ]
    
    # Convertendo para json
    json_produtos_fornecedores = to_json(produtos)
    print(json_produtos_fornecedores)
    
    # Validando se o JSON é válido
    print("É JSON válido?", is_json(json_produtos_fornecedores))

# Exemplos originais separados em funções

# Chamada dos exemplos
exemplo_objeto()
exemplo_lista()
exemplo_lista_produtos_fornecedores()
