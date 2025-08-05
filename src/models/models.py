from dataclasses import dataclass

@dataclass
class Fornecedor:
    """Representa um fornecedor com id e nome."""
    id: int
    nome: str

@dataclass
class Produto:
    """Representa um produto com nome e fornecedor associado."""
    nome: str
    fornecedor: Fornecedor
