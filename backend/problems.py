
PROBLEMS = {
	"strip" : {
		"aspiradora" : {
			"name" : "aspiradora",
			"initialState" : [
				{
					"name" : "aspiradoraEn",
					"value" : "L"
				},
				{
					"name" : "sucio",
					"value" : "L"
				},
				{
					"name" : "sucio",
					"value" : "R"
				}
			],
			"finalState" : [
				{
					"name" : "limpio",
					"value" : "L"
				},
				{
					"name" : "limpio",
					"value" : "R"
				}
			],
			"actions" : [
				{
					"name" : "moverAspiradoraA",
					"variables" : "X,Y",
					"preconditions" : [
						{
							"name" : "aspiradoraEn",
							"value" : "X"
						}
					],
					"postconditions" : [
						{
							"name" : "aspiradoraEn",
							"value" : "Y"
						},
						{
							"name" : "!aspiradoraEn",
							"value" : "X"
						}
					]
				},
				{
					"name" : "limpiar",
					"variables" : "X",
					"preconditions" : [
						{
							"name" : "sucio",
							"value" : "X"
						},
						{
							"name" : "aspiradoraEn",
							"value" : "X"
						}
					],
					"postconditions" : [
						{
							"name" : "limpio",
							"value" : "X"
						},
						{
							"name" : "!sucio",
							"value" : "X"
						}
					]
				}
			],
			"output" : {}
		}
	},
	"htn": {
    "viajar":{
      "name": "viajar",
      "initialState": [
        {
          "name": "estar",
          "value": ["Manizales"]
        },
        {
          "name": "aeropuerto",
          "value": ["Manizales", "La nubia"]
        },
        {
          "name": "aeropuerto",
          "value": ["Bogota", "El dorado"]
        }
      ],
      "tasks": [
        {
          "name": "viajarEnAvion",
          "value": ["Manizales", "Bogota"]
        }
      ],
      "methods" : [
        {
          "name" : "viajarEnAvion",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "aeropuerto",
              "value" : ["x", "a"]
            },
            {
              "name" : "aeropuerto",
              "value" : ["y", "b"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "postconditions" : [
            {
              "name" : "comprarTiquete",
              "value" : ["a", "b"]
            },
            {
              "name" : "viajar",
              "value" : ["x", "a"]
            },
            {
              "name" : "volar",
              "value" : ["a", "b"]
            },
            {
              "name" : "viajar",
              "value" : ["b", "y"]
            }
          ]
        },
        {
          "name" : "viajar",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "postconditions" : [
            {
              "name" : "conseguirTaxi",
              "value" : ["x"]
            },
            {
              "name" : "irTaxi",
              "value" : ["x", "y"]
            }
          ]
        }
      ],
      "operators": [
        {
          "name": "comprarTiquete",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name": "aeropuerto",
              "value": ["a", "x"]
            },
            {
              "name": "aeropuerto",
              "value": ["b", "y"]
            }
          ],
          "del":[],
          "add":[
            {
              "name": "tenerTiquete",
              "value": ["x", "y"]
            }
          ]
        },
        {
          "name" : "volar",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            },
            {
              "name" : "tenerTiquete",
              "value" : ["x", "y"]
            }
          ],
          "del" : [
            {
              "name" : "estar",
              "value" : ["x"]
            },
            {
              "name" : "tenerTiquete",
              "value" : ["x", "y"]
            }
          ],
          "add": [
            {
              "name" : "estar",
              "value" : ["y"]
            }
          ]
        },
        {
          "name" : "conseguirTaxi",
          "variables" : ["x"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "del" : [],
          "add": [
            {
              "name" : "taxi",
              "value" : ["x"]
            }
          ]
        },
        {
          "name" : "irTaxi",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "taxi",
              "value" : ["x"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "del" : [
            {
              "name" : "taxi",
              "value" : ["x"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "add": [
            {
              "name" : "estar",
              "value" : ["y"]
            }
          ]
        }
      ],
      "output": {}
    }
  }
}
