import os
import pyttsx3
import getpass
import subprocess as sp

PW = "navin"

while True:
	os.system("tput setaf 7")
	pyttsx3.speak("PLease enter your password to continue.")
	pw = getpass.getpass("\n\t If you want to continue, please enter your password: ")
	if pw == PW:
		os.system("tput setaf 6")
		pyttsx3.speak("Correct Password Stark")
		print("\n\Correct password")
		pyttsx3.speak("Terminal sleeping for 2 seconds")
		os.system("sleep 2")
		break
	else:
		os.system("tput setaf 5")
		pyttsx3.speak("Incorrect password Stark")
		print("\tIncorrect password!\n")

while True:
    #Date
    def date():
        pyttsx3.speak("Wait a second, Today's date is printing on the black screen")
        os.system("date")
    
    #Cal
    def cal():
        pyttsx3.speak("Wait a second, Present month's calendar is printing")
        os.system("cal")

    #  LOCAL (Name,Data and Client Node) "core-site.xml" file configuration

    def coresite():
        pyttsx3.speak("Enter your master node ip")
        ip = input("Enter your master node ip: ")
        os.system(f"""
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:9001</value>
</property>
</configuration>' > /etc/hadoop/core-site.xml""")
		
    # LOCAL Name Node "hdfs-site.xml" file configuration

    def hdfssite():
        pyttsx3.speak("Enter a folder name where you want to store the index table of all slaves")
        folder_name = input("Enter your folder name: ")
        os.system(f"""mkdir /{folder_name}
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>' > /etc/hadoop/hdfs-site.xml""")
        os.system("hadoop namenode -format")
        os.system("hadoop-daemon.sh start namenode")


    # LOCAL Data Node "hdfs-site.xml" file configuration

    def datahdfssite():
        pyttsx3.speak("Enter a folder name where you want to store the files coming from the client")
        folder_name = input("Enter your folder name: ")
        os.system(f"""mkdir /{folder_name}
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>' > /etc/hadoop/hdfs-site.xml""")
        os.system("hadoop-daemon.sh start datanode")


    # REMOTE  Name,Data and Client Node "core-site.xml" file configuration

    def Remote_coresite():
        pyttsx3.speak("Enter the master node ip of which you want to be a client")
        ip = input("Enter your master node ip: ")
        port = input("Enter Port No: ")
        os.system(f"""
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:{port}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/core-site.xml\'
""")
		

            # REMOTE  Name Node "hdfs-site.xml" file configuration

    def Remote_hdfssite():
        folder_name = input("Enter your folder name: ")
        os.system(f"""ssh {username}@{remoteip} mkdir /{folder_name}
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/hdfs-site.xml\' 
ssh {username}@{remoteip} hadoop namenode -format 
ssh {username}@{remoteip} hadoop-daemon.sh start namenode
""")
        # REMOTE  Data Node "hdfs-site.xml" file configuration

    def Remote_datahdfssite():
        folder_name = input("Enter your folder name: ")
        os.system(f"""ssh {username}@{remoteip} mkdir /{folder_name}
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/hdfs-site.xml\'
ssh {username}@{remoteip} hadoop-daemon.sh start datanode
""")
    #ping to system
    def ping_to_system():
        pyttsx3.speak("Enter the IP of the system to which you want to ping")
        ping_ip = input("\nEnter the IP of the system to which you want to ping: ")
        print(sp.getoutput("sudo ping {} -c 4".format(ping_ip)))
        pyttsx3.speak("Ping has been done")
    
    #read the network packets 
    def read_network_packets():
        pyttsx3.speak("Do you want to read any particular port number")
        choice = input("\nDo you want to read any particular port number(y/n): ")
        if choice == "y":
                pyttsx3.speak("Enter the protocol name")
                protocol = input("\nEnter the protocol name: ")
                pyttsx3.speak("Enter the port number")
                port_number = input("\nEnter the port number: ")
                print(sp.getoutput("sudo tcpdump -i enp0s3 -c 10 {} {} -n".format(protocol,port_number)))
        else:
                print(sp.getoutput("sudo tcpdump -i enp0s3 -c 10 -n"))

    #python module insatller
    def python_module_installer():
        pyttsx3.speak("Enter the Module Name of python you want to install")
        module_name = input("\nEnter the Module Name: ")
        print(sp.getoutput("sudo pip3 install {}".format(module_name)))
        pyttsx3.speak("Module has been installed")
    
    #Elasticity of HD 
    def configure_lvm():
        pyttsx3.speak("Welcome to the Linux LVM automation Script")
        print("\t\t\tWelcome to the Linux LVM automation Script")
        print("\t\t\t------------------------------------------")


        print("""
1.Press 1 to get the list of all the disks attached to the system
2.Press 2 to create Physical Volume
3.Press 3 to create Volume Group
4.Press 4 to create Logical Volume
5.Press 5 to increase or decrease the Logical Volume
6.Press 6 to remove the Logical Volume
7.Press 7 to remove the Volume Group
8.Press 8 to remove the Physical Volume
9.Press 9 to format the partition
10.Press 10 to mount the partition
11.Press 11 to get a list of mount targets
12.Press 12 to unmount the partition\n""")


        choice=int(input("Enter your Choice: "))
        pyttsx3.speak("Enter your Choice")

        if choice == 1:
                pyttsx3.speak("showing the list of all the disks attached to the system")
                print(sp.getoutput("sudo fdisk -l"))
                input()

        if choice == 2:
                disknameadd = input("\nEnter the disk name: ")
                print(sp.getoutput("sudo pvcreate {}".format(disknameadd)))
                input()

        if choice == 3:
                vgnameadd = input("\nEnter the Volume Group name that you want to keep: ")
                diskNameForVG = input("Enter the disk name(s): ")
                print(sp.getoutput("sudo vgcreate {} {}".format(vgnameadd,diskNameForVG)))
                input()

        if choice == 4:
                lvnameadd = input("\nEnter the Logical Volume name you want: ")
                sizeadd = input("\nEnter the size of the Logical Volume: ")
                vgNameForLV = input("\nEnter the name of the Volume Group from where you want to take your storage space: ")
                print(sp.getoutput("sudo lvcreate --size {} --name {}  {} -y ".format(sizeadd,lvnameadd,vgNameForLV)))
                input()

        if choice == 5:
                sizeExtend = input("\nEnter the Size to extend the Partition (K,M,G,T,P): ")
                partitionExtend = input("\nEnter the Logical Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
                print(sp.getoutput("sudo lvextend --size +{} {}".format(sizeExtend,partitionExtend)))
                print(sp.getoutput("sudo resize2fs {}".format(partitionExtend)))
                input()

        if choice == 6:
                lvnamerm = input("\nEnter the Logical Volume name you want to remove: ")
                vgNameForRM = input("\nEnter the Volume Group name associated with the Logical Volume: ")
                print(sp.getoutput("sudo lvremove /dev/{}/{} -y ".format(vgNameForRM,lvnamerm)))
                input()

        if choice == 7:
                vgnamerm = input("\nEnter the Volume Group name that you want to remove: ")
                print(sp.getoutput("sudo vgremove {}".format(vgnamerm)))
                input()
	
        if choice == 8:
                disknamerm = input("\nEnter the disk name: ")
                print(sp.getoutput("sudo pvremove {}".format(disknamerm)))
                input()
		
        if choice == 9:
                formatPartition = input("\nEnter the Logical Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
                print(sp.getoutput("sudo mkfs.ext4 {}".format(formatPartition)))
                input()

        if choice == 10:
                mountTarget = input("\nEnter the mount target: ")
                mountPartition = input("\nEnter the Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
                print(sp.getoutput("sudo mount {} {}".format(mountPartition,mountTarget)))
                input()

        if choice == 11:
                print(sp.getoutput("sudo df -h"))
                input()

        if choice == 12:
                unmountPartition = input("\nEnter the Partition in the format /dev/<Volume Group Name>/<Logical Volume Name>: ")
                print(sp.getoutput("sudo umount {}".format(unmountPartition)))
                input()

    #Docker
    def install_docker():
        print(sp.getoutput("sudo yum install docker ce --nobest"))
    def docker_commands():
        print("""
Press 1 for getting the list of all the running containers
Press 2 for getting the list of all the images
Press 3 for launching a new container
Press 4 for pulling an image from the repository""")
        docker_choice = int(input())
        if docker_choice == 1:
                print(sp.getoutput("sudo docker ps -a"))
        if docker_choice == 2:
                print(sp.getoutput("sudo docker images"))
        if docker_choice == 3:
                print(sp.getoutput("clear"))
                cont_name = input("\nEnter the container name: ")
                img_name = input("\nEnter the image name: ")
                print(sp.getoutput("sudo docker -dit --name {} {}".format(cont_name,img_name)))
        if docker_choice == 4:
                docker_pull_image = input("\nEnter the image name: ")
                print(sp.getoutput("sudo docker pull {}".format(docker_pull_image)))

    #if config command
    def to_check_ip():
        print(sp.getoutput("sudo ifconfig"))


    #create a new user
    def config_user():
        username_add = input("\nEnter the Username to add: ")
        print(sp.getoutput("sudo useradd {}".format(username_add)))

    #QUery of a software
    def query_program():
        program_name = input("\nEnter the program name: ")
        print(sp.getoutput("sudo rpm -q `which {}`".format(program_name)))

    #Ansible
    def install_ansible():
        print(sp.getoutput("sudo pip3 install ansible"))

        # MAIN WORKING MENU

    def menu():
        print("""
        Press 1 : To run date
        Press 2 : To run cal
        Press 3 : To work on Hadoop
        Press 4 : To Ping to a system
        Press 5 : To read Network Packets
        Press 6 : To install a python module
        Press 7 : To configure LVM
        Press 8 : To install Docker
        Press 9 : To use Docker Commands
        Press 10 : To check IP address
        Press 11 : To create a new User
        Press 12 : To know if any program is installed or not
        Press 13 : To install Ansible
        Press 14 : To exit
                """)


            # Local

    def local():
        os.system("tput setaf 11")
        menu()

        ch = input("\nEnter your Choice: ")
        print()

        os.system("tput setaf 15;clear")

        if ch == "1":
            os.system("clear")
            pyttsx3.speak("Wait a second, current date is printing")
            date()
            local()
        elif ch == "2":
            os.system("clear")
            pyttsx3.speak("Wait a second, current calendar is printing")
            cal()
            local()
        elif ch == "3":
            print("""
Press 1 to Configure Name Node
Press 2 to configure Data node
Press 3 to Configure Client Node
""")
            ch = input("\nEnter your Choice: ")
            print()
            

            if ch == "1":
                os.system("clear")
                coresite()
                hdfssite()
                pyttsx3.speak("Congratulations Now your System is a name node")
                local()
            elif ch == "2":
                os.system("clear")
                datahdfssite()
                coresite()
                pyttsx3.speak("Congratulations Now your System is a data node")
                local()
            elif ch == "3":
                os.system("clear")
                coresite()
                os.system("hadoop namenode -format")
                os.system("hadoop-daemon.sh start clientnode")
                pyttsx3.speak("Congratulations Now your System is a client node")
                local()

            else:
                print("Wrong input")
                local()
        elif ch == "4":
          os.system("clear")
          ping_to_system()
          local()

        elif ch == "5":
          os.system("clear")
          read_network_packets()
          local()

        elif ch =="6":
          os.system("clear")
          python_module_installer()
          local()

        elif ch =="7":
          os.system("clear")
          configure_lvm()   
          local()       

        elif ch =="8":
          os.system("clear")
          install_docker()
          local()

        elif ch =="9":
          os.system("clear")
          docker_commands()
          local()

        elif ch =="10":
          os.system("clear")
          to_check_ip()
          local()

        elif ch =="11":
          os.system("clear")
          config_user()
          local()

        elif ch =="12":
          os.system("clear")
          query_program()
          local()

        elif ch =="13":
          os.system("clear")
          install_ansible()
          local()
        elif ch =="14":
          exit()
        else:
            exit()

            # REMOTE 

    def remote():
        menu()
        rchoice = input("Enter your Choice: ")
        if ch == "1":
            os.system("clear")
            pyttsx3.speak("Wait a second, current date is printing")
            date()
            remote()
        elif ch == "2":
            os.system("clear")
            pyttsx3.speak("Wait a second, current calendar is printing")
            cal()
            remote()   
        elif rchoice == "3":
            print("""
            
            Press 1 : To configure Name Node
            Press 2 : To configure Data Node
            Press 3 : To configure Client Node
                    """)
            rch = input("Enter your Choice: ")
            
            if rch == "1":
                os.system("clear")
                Remote_coresite()
                Remote_hdfssite()
                pyttsx3.speak("Congratulations Now your System is a name node")
                remote()
            elif rch == "2":
                os.system("clear")
                Remote_coresite()
                Remote_datahdfssite()
                pyttsx3.speak("Congratulations Now your System is a data node")
                remote()
            elif rch == "3":
                os.system("clear")
                Remote_coresite()
                os.system("hadoop namenode -format")
                os.system("hadoop-daemon.sh start clientnode")
                pyttsx3.speak("Congratulations Now your System is a client node")
                remote()
            else:
                print("Wrong Input")
                remote()
        elif rch == "4":
          os.system("clear")
          ping_to_system()
          remote()

        elif rch == "5":
          os.system("clear")
          read_network_packets()
          remote()

        elif rch =="6":
          os.system("clear")
          python_module_installer()
          remote()

        elif rch =="7":
          os.system("clear")
          configure_lvm()   
          remote()       

        elif rch =="8":
          os.system("clear")
          install_docker()
          remote()

        elif rch =="9":
          os.system("clear")
          docker_commands()
          remote()

        elif rch =="10":
          os.system("clear")
          to_check_ip()
          remote()

        elif rch =="11":
          os.system("clear")
          config_user()
          remote()

        elif rch =="12":
          os.system("clear")
          query_program()
          remote()

        elif rch =="13":
          os.system("clear")
          install_ansible()
          remote()
        
        elif rchoice == "14":
            exit()

    # First Menu Code Start
    pyttsx3.speak("Hello, This is Jarvis")
    pyttsx3.speak("And You are using me so, For me You are my Iron Man.")
   

    os.system("tput setaf 9")

    print("\n\t\tWelcome to ARTH")
    pyttsx3.speak("Welcome to ARTH Program..")

    os.system("tput setaf 10")

    print("\n\tTell me What Do You Want To Do")
    pyttsx3.speak("So Tell me What do you want to do")

    os.system("tput setaf 14")

    print("""\n\tWhere you want to work\n
Press 1 For Local
Press 2 For Remote
Press 3 To Exit 
""")

    choice = input("Please enter your choice: ")
    pyttsx3.speak("Enter your choice Stark.")
    os.system("clear")

    if choice == "1":
        local()
        pyttsx3.speak("Local menu is loading")
    elif choice == "2":
        username = input("Enter User Name: ")
        remoteip = input("Enter LogIn ip: ")
        os.system("tput setaf 9")
        print("Press Enter 3 Times to continue")
        os.system("tput setaf 15")
        sp.getoutput("ssh-keygen")
        os.system(f"ssh-copy-id root@{remoteip}")
        remote()
        pyttsx3.speak("Remote menu is starting")

    elif choice == "3":
        exit()

    else:
        print("Wrong input")
