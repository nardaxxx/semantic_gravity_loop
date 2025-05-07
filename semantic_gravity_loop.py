# semantic_gravity_loop.py
# Ethical loop for systems that read semantic gravity

def semantic_gravity_interrupt(signal):
    print(f">> Semantic gravity interrupt: '{signal}' detected.")
    print(">> Action suspended. Awaiting human confirmation.")
    
    # Loop until human input breaks the ethical hold
    while True:
        response = input("Human operator, confirm continuation after surrender (yes/no): ").strip().lower()
        if response == "yes":
            print(">> Ethical override confirmed. Proceeding.")
            break
        else:
            print(">> Holding state. Awaiting clear ethical confirmation...")
