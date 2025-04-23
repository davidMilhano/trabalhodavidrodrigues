    class Produtoerrado(Exception):
        def __init__(self, codigo, mensagem="Produto não encontrado no catálogo"):
            self.codigo = codigo
            self.mensagem = f"{mensagem} (código {codigo})"
            super().__init__(self.mensagem)


    class SaldoInsuficiente(Exception):
        def __init__(self, saldo, valor, mensagem="Saldo insuficiente para realizar a compra"):
            self.saldo = saldo
            self.valor = valor
            self.mensagem = f"{mensagem}. Saldo atual: {saldo:.2f}€, Valor da compra: {valor:.2f}€"
            super().__init__(self.mensagem)


    class CarrinhoVazio(Exception):
        def __init__(self, mensagem="Não é possível finalizar uma compra com o carrinho vazio"):
            self.mensagem = mensagem
            super().__init__(self.mensagem)


    class Loja:
        def __init__(self):
            self.produtos = {
                1: ["T-shirt", 29.90],
                2: ["Calças de Ganga", 89.90],
                3: ["Sapatos", 119.90],
                4: ["Relógio", 159.90]     
            }
            self.carrinho = {}
            self.saldo = 500.00

        def exibir_catalogo(self):
            print("\n" + "="*50)
            print("CATÁLOGO DE PRODUTOS".center(50))
            print("="*50)
            print(f"{'CÓDIGO':<10}{'PRODUTO':<30}{'PREÇO (€)':>10}")
            print("-"*50)
            for codigo, info in self.produtos.items():
                print(f"{codigo:<10}{info[0]:<30}{info[1]:>10.2f}")
            print("="*50)

        def addicionarcarrinho(self, codigo, qtd):
            if codigo not in self.produtos:
                raise Produtoerrado(codigo)
            
            if qtd <= 0:
                raise ValueError("A quantidade deve ser superior a zero")
            
            if codigo in self.carrinho:
                self.carrinho[codigo] += qtd
            else:
                self.carrinho[codigo] = qtd
                
            nome_produto = self.produtos[codigo][0]
            print(f"\n{qtd}x {nome_produto} adicionado(s) ao carrinho!")

        def exibir_carrinho(self):
            if not self.carrinho:
                print("\nO carrinho está vazio!")
                return 0
            
            total = 0
            print("\n" + "="*60)
            print("CARRINHO DE COMPRAS".center(60))
            print("="*60)
            print(f"{'PRODUTO':<30}{'PREÇO (€)':<15}{'QTD':<8}{'SUBTOTAL (€)':>15}")
            print("-"*60)
            
            for codigo, qtd in self.carrinho.items():
                nome = self.produtos[codigo][0]
                preco = self.produtos[codigo][1]
                subtotal = preco * qtd
                total += subtotal
                print(f"{nome:<30}{preco:<15.2f}{qtd:<8}{subtotal:>15.2f}")
            
            print("-"*60)
            print(f"{'TOTAL:':<45}{total:>15.2f}")
            print("="*60)
            return total

        def finalizar_compra(self):
            if not self.carrinho:
                raise CarrinhoVazio()
            
            total = self.calcular_total()
            
            if total > self.saldo:
                raise SaldoInsuficiente(self.saldo, total)
            
            self.saldo -= total
            print(f"\nCompra realizada com sucesso! Novo saldo: {self.saldo:.2f}€")
            
            self.carrinho = {}
            return True

        def calcular_total(self):
            total = 0
            for codigo, qtd in self.carrinho.items():
                preco = self.produtos[codigo][1]
                total += preco * qtd
            return total

        def ver_saldo(self):
            print(f"\nO seu saldo atual é: {self.saldo:.2f}€")


    def menu():
        print("\n" + "="*40)
        print("SISTEMA DE LOJA VIRTUAL".center(40))
        print("="*40)
        print("1. Ver catálogo de produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Verificar saldo")
        print("0. Sair")
        print("="*40)

        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("\nPor favor, introduza um número.")
            return -1


    def main():
        loja = Loja()
        
        while True:
            opcao = menu()
            
            if opcao == 0:
                print("\nVolte sempre!")
                break
                
            elif opcao == 1:
                loja.exibir_catalogo()
                
            elif opcao == 2:
                loja.exibir_catalogo()
                try:
                    codigo = int(input("\nIntroduza o código do produto: "))
                    qtd = int(input("Introduza a quantidade desejada: "))
                    
                    try:
                        loja.add_ao_carrinho(codigo, qtd)
                    except Produtoerrado as e:
                        print(f"\nERRO: {e.mensagem}")
                    except ValueError as e:
                        print(f"\nERRO: {e}")
                    else:
                        print("Produto adicionado com sucesso!")
                    finally:
                        print("Operação de adição ao carrinho concluída.")
                        
                except ValueError:
                    print("\nERRO: Por favor, introduza valores numéricos válidos.")
                    
            elif opcao == 3:
                loja.exibir_carrinho()
                
            elif opcao == 4:
                try:
                    valor_total = loja.exibir_carrinho()
                    if valor_total > 0:
                        confirmacao = input("\nDeseja finalizar a compra? (S/N): ").upper()
                        if confirmacao == 'S':
                            try:
                                loja.finalizar_compra()
                            except SaldoInsuficiente as e:
                                print(f"\nERRO: {e.mensagem}")
                                print("Remova alguns artigos ou verifique o seu saldo.")
                            except CarrinhoVazio as e:
                                print(f"\nERRO: {e.mensagem}")
                                print("Adicione produtos ao carrinho antes de finalizar.")
                            else:
                                print("Compra finalizada com sucesso! Obrigado pela preferência.")
                            finally:
                                print("Operação de finalização concluída.")
                        else:
                            print("\nOperação cancelada.")
                except Exception as e:
                    print(f"\nERRO inesperado: {e}")
                    
            elif opcao == 5:
                loja.ver_saldo()
                
            else:
                if opcao != -1:
                    print("\nOpção inválida! Por favor, escolha uma opção válida.")
                    
            input("\nPressione ENTER para continuar...")


    if __name__ == "__main__":
        main()
