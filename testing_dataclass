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
    json_produto = to_json(produto)
    print("Exemplo Produto único:")
    print(json_produto)
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
    json_lista = to_json(lista_produtos)
    print("Exemplo Lista de Produtos:")
    print(json_lista)
    print("É JSON válido?", is_json(json_lista))

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

# Converter lista de fornecedores para lista de dicionários
fornecedores_dict = [asdict(f) for f in fornecedores]
# Converter lista de produtos para lista de dicionários
produtos_dict = [asdict(p) for p in produtos]

# Exemplos originais separados em funções
def exemplo_fornecedores():
    """
    Exibe a lista de fornecedores como JSON.
    """
    
    # Lista de fornecedores
    fornecedores: List[Fornecedor] = [
        Fornecedor(1, "Fornecedor XPTO"),
        Fornecedor(2, "Fornecedor ABC")
    ]
    
    print("Fornecedores:")
    print(to_json(fornecedores))

def exemplo_produtos():
    """
    Exibe a lista de produtos como JSON.
    """
    print("Produtos:")
    print(to_json(produtos))

# Chamada dos exemplos
exemplo_fornecedores()
exemplo_produtos()
exemplo_objeto()
exemplo_lista()
