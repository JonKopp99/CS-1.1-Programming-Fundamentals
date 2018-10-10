
class Virus(object):
    mortality_rate = 0.0
    repro_rate = 0.0
    virus_name = ""

    def __init__(self, virus_name, mortality_rate, repro_rate):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.repro_rate = repro_rate


def test_virus():
    virus = Virus("HIV", 0.8,0.3)
    assert virus.virus_name == "HIV"
    assert virus.mortality_rate == 0.8
    assert virus.repro_rate == 0.3
test_virus()
