from distutils.core import setup

# Функция установки
setup(name="MathProtEnergyProcSynDatas",
      version="1.0",
      author="Igor Starostin",
      author_email="starostinigo@yandex.ru",
      description="Syntetic datas by modeling by mathematical prototiping method of energy process",
      packages=["MathProtEnergyProcSynDatas",
                "MathProtEnergyProcSynDatas.DatasSyntetic",
                "MathProtEnergyProcSynDatas.tests"],
      scripts=["testMathProtEnergyProcSynDatas.py"]
      )
