# Sistema Bancário Simples
Este é um sistema bancário simples desenvolvido em Python que permite a realização de operações básicas como depósito, saque e consulta de extrato. O sistema é executado em um loop que exibe um menu interativo para o usuário.

## Funcionalidades
* **Depositar**: Adiciona um valor ao saldo da conta.
* **Sacar**: Subtrai um valor do saldo da conta, respeitando o limite de saques diários e o saldo disponível.
* **Extrato**: Exibe todas as movimentações realizadas e o saldo atual da conta.
* **Limite de Saques**: Limita o número de saques diários a três saques, com um valor máximo de R$ 500,00 por saque.

## Requisitos
Python 3.6 ou superior

## Instalação
Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/sistema-bancario.git
cd sistema-bancario
```

## Execução
Para executar o sistema, basta rodar o arquivo main.py:

```bash
python main.py
```
Ao iniciar, o sistema exibe um menu com as seguintes opções:
* **[d] Depositar**: Informe um valor para adicionar à conta.
* **[s] Sacar**: Informe um valor para retirar da conta. Respeite os limites de saque.
* **[e] Extrato**: Exibe todas as movimentações realizadas.
* **[q] Sair**: Sai do sistema.
Exemplo de Execução

```text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 200
Depósito realizado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 200.00
Saldo: R$ 1200.00
==========================================
```

## Estrutura do Código
O código está organizado da seguinte forma:

## Classe ```Conta```

A classe ```Conta``` é responsável por representar a conta bancária e realizar operações básicas.

**Atributos**:
* **agencia**: Número da agência.
* **conta**: Número da conta.
* **saldo**: Saldo disponível na conta.
* **extrato**: Lista que armazena todas as transações realizadas.
* **limite_saques**: Número máximo de saques diários.
* **valor_limite**: Limite máximo de saque por operação.

**Métodos**:
* **depositar(valor)**: Adiciona um valor ao saldo da conta e registra a transação no extrato.
* **sacar(valor)**: Subtrai um valor do saldo, verifica o limite de saques e registra a transação no extrato.
* **imprimir_extrato()**: Exibe todas as movimentações realizadas na conta.

## Melhorias Futuras
* Implementar autenticação de usuários.
* Adicionar suporte para múltiplas contas por usuário.
* Criar um sistema de taxas de juros e rendimentos para contas.
* Permitir transferência entre contas.

## Contribuição
Contribuições são bem-vindas! Se você deseja melhorar o projeto, sinta-se à vontade para abrir um *Pull Request* ou uma *Issue* no repositório.
