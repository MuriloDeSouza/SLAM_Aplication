# SLAM_Aplication

# Como se conectar com o robô.

Conecte o robô com o ssh:

export ROS_DOMAIN_ID=<NUMERO_ABAIXO_DE_214>

Fazer no computador tambem então tem que abrir outro terminal e fazer isso.

Configurando o modelo do robô como burger

export TURTLEBOT3_MODEL=burger

Não esqueça de rodar o bringup no robô:

ros2 launch turtlebot3_bringup robot.launch.py