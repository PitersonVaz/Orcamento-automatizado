# Sistema de Automacao de Orcamentos e Reservas (Orvex Locacoes)

Sistema de automacao comercial desenvolvido em Python para uso interno da Orvex Locacoes. A aplicacao automatiza a geracao de orcamentos para locacao de materiais de eventos, apresentacao de termos contratuais, calculo de taxa de reserva e disparo de mensagens formatadas via WhatsApp Web.

---

## O Problema
O atendimento manual para orcamento de locacoes gerava erros em calculos de taxas, demora na emissao dos termos de contrato e tempo excessivo na digitacao das informacoes do pedido para envio ao cliente via WhatsApp.

## A Solucao
Uma aplicacao de terminal (CLI) que coleta os dados do evento, realiza os calculos matematicos do orcamento com precisao e utiliza a API de links do WhatsApp (`wa.me`) para abrir automaticamente mensagens formatadas para a empresa e para o cliente.

### Funcionalidades Principais:
- Geracao de numero de pedido unico e aleatorio.
- Calculo automatico do orcamento (mesas, toalhas e taxa de entrega).
- Calculo do valor do sinal de reserva Pix.
- Exibicao automatica do contrato e regras de locacao.
- Abertura automatica de abas no navegador com links diretos do WhatsApp.

---

## Tecnologias Utilizadas
- Python 3 (Modulos nativos: `random`, `urllib.parse`, `webbrowser`)

---

## Estrutura do Projeto
- `main.py`: Script principal contendo a logica do menu, calculos do orcamento e integracao com WhatsApp.
-
