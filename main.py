from api import IdenaAPI
# Connect to local node with default settings (with no Custom api)
api = IdenaAPI()
api = IdenaAPI(api_key=input("API KEY:"))
myaddr = api.address()
mybalance = api.balance(myaddr["result"])
sync = api.sync_status()
nodever = api.node_version()
# Check balance
print("Welcome to Idena-CLI wallet v0.1")
print("Made by Toni.Dev, Donation:0x6357cdf056b0dca75a14094987fa7eabbd78be5f")
print("Coinbase Address:", myaddr["result"])
print("Balance:", mybalance["result"]["balance"])
print("Is it syncing:", sync["result"]["syncing"])
print("Node Version:", nodever["result"])
print("1.SEND IDNA")
print("2.START MINING")
print("3.STOP MINING")
print("4.LIST LAST TX")
print("5.EXIT")
def home_act1():
            sendto = input("Send to:")
            amount = input("Amount:")
            sure = input("ARE YOU SURE: Y/N:")
            if sure == 'Y':
                result = api.send(myaddr["result"], sendto, amount)
                print("TX ID:", result["result"], "Sended to:", sendto, "Amount:", amount)
            else:
                exit()
def home_act2():
    start = api.go_online()
    print("Started Mining")
def home_act3():
    stop = api.go_offline()
    print("Stoped Mining")
def home_act5():
    print("You closed Idena Cli Wallet")
    exit()
def home_act4():
    tx = api.transactions(myaddr["result"], 1)
    print("Last Transaction:", "Hash:", tx["result"]["transactions"][0]["hash"], "To:", tx["result"]["transactions"][0]["to"], "Amount:", tx["result"]["transactions"][0]["amount"])
def action():
    loop = True
    while loop:
        # print(menu)
        user_action = input("CHOSE FROM MENU ABOVE:")
        if user_action == '1':
            return home_act1() 
        elif user_action == '2':
            return home_act2()
        elif user_action == '3':
            return home_act3()
        elif user_action == '4':
            return home_act4()
        elif user_action == '5':
            return home_act5()
        else:
            print("Please type \'1\', \'2\', \'3\', or \'4\, \5\'")
action()
#There is no virus in here be free to keep looking :)
