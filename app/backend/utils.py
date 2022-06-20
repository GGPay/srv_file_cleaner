
class StringClean:
    @staticmethod
    def remove_whitespace(in_str: str):
        out_str = in_str.strip()
        return out_str

    @staticmethod
    def remove_after_backslash(in_str: str):
        out_str = in_str.split('/', 1)[0]
        return out_str

    @staticmethod
    def remove_leading_zeros(in_str: str):
        out_str = in_str.strip("0")
        return out_str

    @staticmethod
    def remove_shorter_number_by_whitespace(in_str: str):
        splitted_str = in_str.split(' ', 1)

        out_str = ""
        for str_part in splitted_str:
            if len(str_part) > len(out_str):
                out_str = str_part

        return out_str

    @staticmethod
    def remove_shorter_number_by_colon(in_str: str):
        splitted_str = in_str.split(':', 1)

        out_str = ""
        for str_part in splitted_str:
            if len(str_part) > len(out_str):
                out_str = str_part

        return out_str

    @staticmethod
    def clean_string(in_str: str) -> str:

        l_str = StringClean.remove_whitespace(in_str)
        l_str = StringClean.remove_after_backslash(l_str)
        l_str = StringClean.remove_shorter_number_by_whitespace(l_str)
        l_str = StringClean.remove_shorter_number_by_colon(l_str)
        l_str = StringClean.remove_leading_zeros(l_str)

        return l_str

if __name__ == '__main__':
    l_str = "01: 1626181 "
    #l_str = "6982-11-13D2/40"
    #l_str = "0001626181 "

    clean_string = StringClean.remove_whitespace(l_str)
    clean_string = StringClean.remove_after_backslash(clean_string)
    clean_string = StringClean.remove_shorter_number_by_whitespace(clean_string)
    clean_string = StringClean.remove_shorter_number_by_colon(clean_string)
    clean_string = StringClean.remove_leading_zeros(clean_string)
    pass

