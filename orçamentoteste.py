import random
import urllib.parse
import webbrowser

meu_whatsapp = "5541987494310"
numero_pedido = random.randint(1000, 9999)

contrato_orvex = """
Contrato de Locação
(Recomendado ler as condições)
​Entregas: Realizadas das 8h às 12h na data marcada (sem horários agendados). Para salões, condomínios ou horários específicos, avise no ato da contratação. Entrega e retirada apenas no térreo (se não houver elevador).
​Uso adequado: Proibido o uso de mesas e cadeiras em pisos de terra ou grama (causam sujeira excessiva). Não utilize fitas dupla face nas mesas, pois danificam o material.
​Reserva das mesas: Taxa fixa de R$ 30,00 pelo pedido inteiro (parte do sinal), com o restante pago na entrega.
​Toalhas (Serviço Terceirizado): Cobrado separadamente. Para confirmar, é preciso pagar 50% do valor das toalhas antecipadamente (não estornável em caso de desistência); os outros 50% são pagos junto com o restante das mesas na entrega.
​Cancelamento e Alterações: O sinal não é estornado em caso de desistência, mas pode ser usado em outra data em até 1 mês (válido para avisos com até 48h de antecedência). Reduções na quantidade de itens também devem ser feitas com até 48h de antecedência.
​Conservação e Devolução: Os itens devem ser devolvidos na mesma quantidade e estado. Danos ou extravios serão cobrados.
​Atrasos na Retirada: Os horários devem ser cumpridos rigorosamente para não atrapalhar os clientes do dia seguinte (sujeito à cobrança de uma nova diária).
p​OBS.: Estando de acordo, efetue o pagamento do sinal (R$ 30,00 + 50% das toalhas, se houver) para concluirmos a reserva."""

print("=" * 80)
print("Orvex".center(80))
print("=" * 80)

print("OLÁ SEJA BEM VINDO(A), A seguir faremos algumas perguntas para gerar deu orçamento")
nome = input("Qual o seu nome?")
telefone_cliente = input("Qual o seu whatsapp (ex: 55+(DDD)+n°telefone)? ")
if not telefone_cliente.startswith("55"):
    telefone_cliente = "55" + telefone_cliente

cep_cliente = input("Digite o CEP de entrega (apenas números): ").strip()
endereco = input("Endereço?")
data = input("Data do evento?")
quant_toalhas = int(input("Quantidade de toalhas?" ))
quant_mesas = int(input("quantidade de mesas?" ))

taxa_de_entrega = 40
mesas = quant_mesas * 25
toalhas =  quant_toalhas * 12
total = taxa_de_entrega + mesas + toalhas

print("=" * 80)
print(f"ORÇAMENTO".center(50))
print("Pedido n°{numero_pedido}")
print("=" * 80)

print(f"1- Mesas= R${mesas:.2f}")
print(f"2- toalhas= R${toalhas:.2f}")
print(f"3- Taxa de entrega= {taxa_de_entrega:.2f}")

print(f"Total= R${mesas + toalhas + taxa_de_entrega:.2f}")

while True:
    reserva = input("Deseja concluir a reserva? (1)SIM (2)Não" )
    if reserva == "1":
        print(contrato_orvex)
        print("\n" + "=" * 80)
        print(f"PAGAMENTO DO SINAL - PEDIDO Nº {numero_pedido}".center(60))
        print("=" * 80)
        print("Para confirmar a reserva, por favor, realize o Pix:")
        print("Chave Pix (CNPJ): 00.000.000/0001-00")
        print(f"Valor do sinal: R$ 30,00 + {toalhas / 2:.2f} das toalhas (se houver)")
        print("=" * 80)

        texto_para_voce = f"Olá! Segue o comprovante do Pedido #{numero_pedido} de {nome}. Valor: R$ {total:.2f}. Endereço: {endereco}"
        link_para_voce = f"https://wa.me/{meu_whatsapp}?text={urllib.parse.quote(texto_para_voce)}"
        
        
        texto_para_cliente = f"""Olá {nome}!  
Recebemos a confirmação do seu pedido na Orvex Locações. 
Seu pedido Nº é: #{numero_pedido}
Data do evento: {data}
Endereço de entrega: {endereco}
Total do pedido: R$ {total:.2f}

Obrigado por fechar com a gente! Qualquer dúvida estamos à disposição."""
        
        link_para_cliente = f"https://wa.me/55{telefone_cliente}?text={urllib.parse.quote(texto_para_cliente)}"
        
        input("\nPressione ENTER para enviar os dados para o WhatsApp...")
        
        webbrowser.open(link_para_voce)
        
        webbrowser.open(link_para_cliente)
        
        print("\n" + "=" * 80)
        print(f"PEDIDO Nº {numero_pedido} FINALIZADO COM SUCESSO!".center(80))
        print("=" * 80)
        print("As abas do WhatsApp foram abertas para você enviar as mensagens.")
        print("Obrigado por usar o sistema da Orvex Locações!")
        print("=" * 80)
        
        break

        # texto_zap = f"Olá! Segue o comprovante do Pedido #{numero_pedido} no valor total de R$ {total:.2f}. Endereço: {endereco}"
        
        # mensagem_codificada = urllib.parse.quote(texto_zap)
        # link_whatsapp = f"https://wa.me/{meu_whatsapp}?text={mensagem_codificada}"
        
        # input("\nPressione ENTER para abrir o WhatsApp e enviar o comprovante...")
        
        # webbrowser.open(link_whatsapp)
        
        # print("\n" + "=" * 80)
        # print(f"PEDIDO Nº {numero_pedido} ENVIADO PARA O WHATSAPP! 🎉".center(60))
        # print("=" * 80)
        # print("Assim que você confirmar o Pix por lá, a reserva estará garantida.")
        # print("Obrigado por escolher a Orvex Locações!")
        # print("=" * 80)
        
        # break

        # input("Pressione ENTER após enviar o comprovante de pagamento...")
        # print("\n" + "=" * 60)
        # print(f"PEDIDO Nº {numero_pedido} FINALIZADO COM SUCESSO! 🎉".center(60))
        # print("=" * 60)
        # print("Recebemos a confirmação. Sua reserva na Orvex Locações está garantida!")
        # print("Foi um prazer atende-lo(a), Orvex agradece e deseja um ótimo dia.")
        # print("=" * 60)

    elif reserva == "2":
        print("Foi um prazer atende-lo(a), Orvex agradece ótimo dia."())
        break
    else:
        print("Opção inválida! Digite a opção 1 ou 2")
    