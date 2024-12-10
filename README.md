# SLAM_Aplication

SLAM_Aplication é a minha ponderada do professor Rodrigo (o homem, uma máquina, uma besta enjaulada) Nicola.
O intuito dessa ponderada e os pontos em questão para fazer essa ponderada vai estar disposto abaixo com o barema que ele disponibilizou para nós:

## 1. Enunciado

### O que?

Para esta ponderada, sua tarefa será implementar, em um pacote ROS, um nó capaz de utilizar o Turtlebot para mapear um ambiente e navegar de forma autônoma neste ambiente.

### Como?

Para concluir esta atividade, será necessário:

    Criar um pacote ROS;
    Utilizar um pacote para mapeamento de ambientes (e.g. turtlebot3 cartographer);
    Utilizar um pacote para navegar em ambientes (e.g. nav2);
    Integrar ambas funcionalidades em seu pacote através do uso de um - ou mais - launch file;
    Por fim, deve-se criar um nó ROS que utiliza o Simple Commander ou ações ROS puras para comandar o robô através de set points para sua árvore de comportament.

e para começar a documentação, primeiro temos que conectar no robô para começar a fazer tudo de uma maneira mais vívida e realista.

# 1 - Como se conectar com o robô (Terminal do robô)

Em primeiro lugar, temos que conectar o robô por SSH e como que nós fazemos isso ???
Abrimos um terminal novo no computador e escrevemos a seguinte mensagem:

```bash
ssh jarbinhas@10.128.0.9
```
Esse é o ssh do robô (turtlebot3) que foi configurado no início do projeto quando delimitamos como chamaríamos o robô.

Depois disso, no próprio terminal ele vai solicitar a senha e você vai colocar a senha para se conectar com o robô.

```bash
Digite a sua senha: *********
```
Uma vez que você se conectou com o robô, você tem que setar/atribuir um número para que nós consigamos se comunicar com o robô e esse número tem que ser menos que 214 por que ele não aceita um número maior que 214.
Coloque o código abaixo e atribua o número de comunicação com o robô:

```bash
export ROS_DOMAIN_ID=<NUMERO_ABAIXO_DE_214>
```

Depois que eu coloquei o numero eu tenho que escrever mais esses dois comandos para assim configurar o robô 

```bash
colcon build
source install/local_setup.bash
```
Como você teve que abrir um outro terminal para se conectar com o robô, entendo que agora tem-se 2 terminais abertos (um com o ssh do robô e outro com esse projeto aberto "SLAM_Aplication")

## 1.1 COnectando o robô com o preojto (Terminal do projeto)

Aí, no terminal onde o projeto está rodando, você vai ter que rodar o mesmo código para colocar o mesmo número que está usando no robô para estabelecer a comunic:

```bash
export ROS_DOMAIN_ID=<MESMO_NUMERO_ESCOLHIDO>
```
Temos outro comando que tem que rodar no terminal que está o projeto também que é para colocar o turtlebot3 com o modelo = "burger"
Configurando o modelo do robô como burger e o comando é esse abaixo:

```bash
export TURTLEBOT3_MODEL=burger
```

Não esqueça de rodar o bringup no robô:
```bash
ros2 launch turtlebot3_bringup robot.launch.py
```