from itertools import combinations,accumulate
from collections import defaultdict
burger={
  "hamburgueria": {
    "mes": "Agosto",
    "ano": 2024,
    "vendas": [
      {
        "dia": 1,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 100,
            "faturamento": 500.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 750.00
      },
      {
        "dia": 2,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 80,
            "faturamento": 400.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 40,
            "faturamento": 80.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 630.00
      },
      {
        "dia": 3,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 90,
            "faturamento": 450.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 40,
            "faturamento": 120.00
          }
        ],
        "lucro": 670.00
      },
      {
        "dia": 4,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 110,
            "faturamento": 550.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 30,
            "faturamento": 60.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 760.00
      },
      {
        "dia": 5,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 100,
            "faturamento": 500.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 60,
            "faturamento": 120.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 70,
            "faturamento": 210.00
          }
        ],
        "lucro": 830.00
      },
      {
        "dia": 6,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 90,
            "faturamento": 450.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 70,
            "faturamento": 140.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 60,
            "faturamento": 180.00
          }
        ],
        "lucro": 770.00
      },
      {
        "dia": 7,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 95,
            "faturamento": 475.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 85,
            "faturamento": 170.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 795.00
      },
      {
        "dia": 8,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 120,
            "faturamento": 600.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 40,
            "faturamento": 80.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 40,
            "faturamento": 120.00
          }
        ],
        "lucro": 800.00
      },
      {
        "dia": 9,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 75,
            "faturamento": 375.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 70,
            "faturamento": 140.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 665.00
      },
      {
        "dia": 10,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 85,
            "faturamento": 425.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 60,
            "faturamento": 180.00
          }
        ],
        "lucro": 705.00
      }
      
    ]
  }
}
burger={
  "hamburgueria": {
    "mes": "Agosto",
    "ano": 2024,
    "vendas": [
      {
        "dia": 1,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 100,
            "faturamento": 500.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 750.00
      },
      {
        "dia": 2,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 80,
            "faturamento": 400.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 40,
            "faturamento": 80.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 630.00
      },
      {
        "dia": 3,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 90,
            "faturamento": 450.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 40,
            "faturamento": 120.00
          }
        ],
        "lucro": 670.00
      },
      {
        "dia": 4,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 110,
            "faturamento": 550.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 30,
            "faturamento": 60.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 760.00
      },
      {
        "dia": 5,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 100,
            "faturamento": 500.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 60,
            "faturamento": 120.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 70,
            "faturamento": 210.00
          }
        ],
        "lucro": 830.00
      },
      {
        "dia": 6,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 90,
            "faturamento": 450.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 70,
            "faturamento": 140.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 60,
            "faturamento": 180.00
          }
        ],
        "lucro": 770.00
      },
      {
        "dia": 7,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 95,
            "faturamento": 475.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 85,
            "faturamento": 170.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 795.00
      },
      {
        "dia": 8,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 120,
            "faturamento": 600.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 40,
            "faturamento": 80.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 40,
            "faturamento": 120.00
          }
        ],
        "lucro": 800.00
      },
      {
        "dia": 9,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 75,
            "faturamento": 375.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 70,
            "faturamento": 140.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 50,
            "faturamento": 150.00
          }
        ],
        "lucro": 665.00
      },
      {
        "dia": 10,
        "itens": [
          {
            "nome": "Cheeseburger",
            "preco": 5.00,
            "quantidade_vendida": 85,
            "faturamento": 425.00
          },
          {
            "nome": "Sprite",
            "preco": 2.00,
            "quantidade_vendida": 50,
            "faturamento": 100.00
          },
          {
            "nome": "Batata Frita",
            "preco": 3.00,
            "quantidade_vendida": 60,
            "faturamento": 180.00
          }
        ],
        "lucro": 705.00
      }
      
    ]
  }
}
# calcular o total do lucro do mes 
def lucro_total():
  lucro_total = [item["lucro"] for item in burger["hamburgueria"]["vendas"]]
  return sum(lucro_total)

lucro_mensal = lucro_total()
print(lucro_mensal )
#calcular o acumulado mensal desse lucro 
def acumulo_mensal ():
  lucro_hambugueria = [item["lucro"] for item in burger["hamburgueria"]["vendas"]]
  dict_lucro = defaultdict(list)
  dict_lucro["lucro_acumulado"]=list(accumulate(lucro_hambugueria))
  return dict_lucro
acumulo_burger_lucro=acumulo_mensal()
print(acumulo_burger_lucro)

#combinacoes de itens 
def combinacoes_itens():
  itens =["cheeseburger","sprite","batata frita"]
  combinacoes = list(combinations(itens,2))
  print(combinacoes)

combinacoes_itens()

#media de faturamento 
def mediana_faturamento():
  faturamento_total = []
  for venda in burger["hamburgueria"]["vendas"]:
    for item in venda["itens"]:
      faturamento_total.append(item["faturamento"])
  faturamento_total.sort(reverse=True)

  #mediana
  faturamento_ordenado = sorted(faturamento_total)
  tamanho = len(faturamento_ordenado)
  if tamanho % 2 == 0:
    mediana = (faturamento_ordenado[tamanho // 2 - 1] + faturamento_ordenado[tamanho // 2]) / 2
    print(mediana)
  else:
    mediana = faturamento_ordenado[tamanho // 2]
    print(mediana)

mediana_faturamento()
