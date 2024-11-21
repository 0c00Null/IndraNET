# indra =v0.0.1
# ---------------------
#
#
#
# ---------------------

def _banner():
    print("""

        

            ██╗███╗   ██╗██████╗ ██████╗  █████╗     
            ██║████╗  ██║██╔══██╗██╔══██╗██╔══██╗    
            ██║██╔██╗ ██║██║  ██║██████╔╝███████║    
            ██║██║╚██╗██║██║  ██║██╔══██╗██╔══██║    
            ██║██║ ╚████║██████╔╝██║  ██║██║  ██║    
            ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    
                                                         
            
            ➥  dev by ❝ khorchf ❞ , github @khorchf  
            ➥  version v0.0.1                                                                                          
                                                                                
    """)

_banner()


target = input(" ➤ ")

def _domain():
    print(target)
    if target == "www.akwagroup.com":
        print(" - Target : www.akwagroup.com => port open '8080' ")
    else:
        print(" an error ACCURED! ")

_domain()





















