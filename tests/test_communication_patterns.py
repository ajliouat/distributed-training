from src.communication_patterns import CommunicationPatterns

def test_communication_patterns():
    comm = CommunicationPatterns("ring")
    comm.optimize()

if __name__ == "__main__":
    test_communication_patterns()