import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import inquirer
import typer
from nav2_simple_commander.robot_navigator import BasicNavigator
from tf_transformations import quaternion_from_euler
from geometry_msgs.msg import PoseStamped


app = typer.Typer()

# turtle_controller
# turtlebot3_teleop
# /turtle1/cmd_vel
# cmd_vel
class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.twist_msg = Twist()

    def send_cmd_vel(self, linear_vel, angular_vel):
        self.twist_msg.linear.x = linear_vel
        self.twist_msg.angular.z = angular_vel
        self.publisher_.publish(self.twist_msg)
        print(f"Linear Vel: {linear_vel}, Angular Vel: {angular_vel}")
        
# Definir os pontos que o robô vai (nome, x, y, z)

pontos = [
    {
        'nome': 'Ponto 1',
        'x': 1.45,
        'y': -0.5,
        'z': 0.0
    },
    {
        'nome': 'Ponto 2',
        'x': 0.84,
        'y': 0.35,
        'z': 0.0
    },
    {
        'nome': 'Ponto 3',
        'x': 0.0,
        'y': 0.0,
        'z': 0.2
    }
]


def create_pose_stamped(navigator, pos_x, pos_y, rot_z):
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()  # Use navigator here
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose


@app.command()
def control():
    rclpy.init()
    nav = BasicNavigator()
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, 0.0)
    initial_pose = PoseStamped()
    node = TeleopTurtle()
    
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = nav.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = q_x
    initial_pose.pose.orientation.y = q_y
    initial_pose.pose.orientation.z = q_z
    initial_pose.pose.orientation.w = q_w
    
    nav.setInitialPose(initial_pose)
    nav.waitUntilNav2Active()

    
    print("Controle do TurtleBot3")
    questions = [inquirer.List(
        name='command',
        message='Selecione uma ação:',
        choices=['Frente', 'Trás', 'Esquerda', 'Direita', 'Emergência (Parar Funcionamento)', 'Ir para ponto', 'Sair']
    )]
    
    try:
        while True:
            command = inquirer.prompt(questions)['command']
            match command:
                case 'Sair':
                    break
                case 'Frente':
                    node.send_cmd_vel(0.2, 0.0) 
                case 'Trás':
                    node.send_cmd_vel(-0.2, 0.0)
                case 'Esquerda':
                    node.send_cmd_vel(0.0, 0.5)
                case 'Direita':
                    node.send_cmd_vel(0.0, -0.5)
                case 'Emergência':
                    node.send_cmd_vel(0.0, 0.0)
                case 'Ir para ponto':
                    # print('Pontos disponíveis:')

                    name_points = [ponto['nome'] for ponto in pontos]

                    point_question = [
                        inquirer.List(
                            name='point',
                            message='Selecione o ponto de destino:',
                            choices=name_points
                        )
                    ]
                    selected_point_name = inquirer.prompt(point_question)['point']
                    selected_point = [ponto for ponto in pontos if ponto['nome'] == selected_point_name][0]

                    goal_pose = create_pose_stamped(nav, selected_point['x'], selected_point['y'], selected_point['z'])

                    nav.followWaypoints([goal_pose])
                                        
    except Exception as e:
        print(f'Erro: {e}. Parando movimentação do robô.')
        node.send_cmd_vel(0.0, 0.0)
    finally:
        node.send_cmd_vel(0.0, 0.0)
        rclpy.shutdown()

if __name__ == "__main__":
    app()