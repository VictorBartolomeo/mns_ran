class ComptaUtils:

    @staticmethod
    def moyenne(tuple):
        cumul=0

        for elemtn in tuple:
            cumul += elemtn

        return cumul/len(tuple)