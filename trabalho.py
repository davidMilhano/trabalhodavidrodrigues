    class ErroArtigoIndisponivel(Exception):
    def __init__(self, message):
        super().__init__(message)

class ErroQuantidadeInvalida(Exception):
    def __init__(self, message):
        super().__init__(message)

class ErroSaldoInsuficiente(Exception):
    def __init__(self, message):
        super().__init__(message)

class ErroCestaVazia(Exception):
    def __init__(self, message):
        super().__init__(message)

class SistemaLoja:
    def __init__(self):
        self.artigos = {
            "calças": 22.50,
            "sapatilhas": 100.00,
            "bolo": 13.00,
        }
        self.cesta = {}
        self.saldo = 300.00
        
    def mostrar_artigos(self):
        print("\nArtigos Disponíveis na Loja")
        print("-" * 30)
        for artigo, preco in self.artigos.items():
            print(f"{artigo.capitalize()}: €{preco:.2f}")
        print("-" * 30)
    
    def adicionar_a_cesta(self):
        try:
            artigo = input("Nome do artigo desejado: ").strip().lower()
            if artigo not in self.artigos:
                raise ErroArtigoIndisponivel("Este artigo não está disponível na nossa loja.")
            
            qtd_str = input("Quantidade desejada: ")
            if not qtd_str.isdigit() or int(qtd_str) <= 0:
                raise ErroQuantidadeInvalida("Por favor, indique uma quantidade válida.")
            
            quantidade = int(qtd_str)
            
            if artigo in self.cesta:
                self.cesta[artigo] += quantidade
            else:
                self.cesta[artigo] = quantidade
            
            print(f"{quantidade} x {artigo} adicionado à cesta.")
        
        except (ErroArtigoIndisponivel, ErroQuantidadeInvalida) as erro:
            print(f"Erro: {erro}")
        except Exception:
            print("Ocorreu um erro inesperado.")
    def calcular_total(self):
        total = 0
        for artigo, quantidade in self.cesta.items():
            if artigo in self.artigos:
                total += self.artigos[artigo] * quantidade
        print(f"\nValor total da compra: €{total:.2f}")
        return total
    
    def finalizar_compra(self):
        try:
            if not self.cesta:
                raise ErroCestaVazia("A sua cesta está vazia.")
            
            total = self.calcular_total()
            
            if total > self.saldo:
                raise ErroSaldoInsuficiente("Não tem saldo suficiente para concluir a compra.")
            
            self.saldo -= total
            print(f"\nPagamento concluído com sucesso!")
            print(f"Valor pago: €{total:.2f}")
            print(f"Saldo atual: €{self.saldo:.2f}")
            self.cesta.clear()
        
        except (ErroCestaVazia, ErroSaldoInsuficiente) as erro:
            print(f"Erro: {erro}")
        except Exception:
            print("Ocorreu um erro inesperado.")
    
    def consultar_saldo(self):
        print(f"\nSaldo disponível: €{self.saldo:.2f}")
    
    def executar(self):
        while True:
            print("\nMenu Principal")
            print("1 - Ver artigos disponíveis")
            print("2 - Adicionar artigo à cesta")
            print("3 - Ver total da compra")
            print("4 - Finalizar compra")
            print("5 - Consultar saldo")
            print("0 - Sair")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.mostrar_artigos()
            elif opcao == "2":
                self.adicionar_a_cesta()
            elif opcao == "3":
                self.calcular_total()
            elif opcao == "4":
                self.finalizar_compra()
            elif opcao == "5":
                self.consultar_saldo()
            elif opcao == "0":
                print("A sair do programa. Até à próxima!")
                break
            else:
                print("Opção inválida. Tente novamente.")

