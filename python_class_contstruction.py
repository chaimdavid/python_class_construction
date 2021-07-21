class Sequence:

    def __init__(self, ID, seq_type, sequence, entry_year):
        self.ID=ID
        self.seq_type=seq_type
        self.sequence=sequence
        self.entry_year=entry_year

    def print_info(self):
        print ("ID: " + str(self.ID) + "\nSEQ_TYPE: " + self.seq_type + "\nSEQUENCE: " + self.sequence + "\nENTRY YEAR: " + str(self.entry_year))
        
    def validate(self):
        biotype=self.seq_type.upper()
        if biotype == "DNA" or biotype == "RNA":
            print ("\nAppropriate sequence type")
        else:
            print ("\nNon biological sequence type!")

artifact=Sequence(1,"DNA","GCADAGCDGCCGAD",2021)

artifact.print_info()

artifact.validate()
