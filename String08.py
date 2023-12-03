def main(first,last):
    """
    Given two strings, first_name and last_name, return a single string in the format "last, first".
    Args:
        first: str
        last: str
    Returns:
        str: return answer.
        Ikki qator berilgan, birinchi_ism va familiya, "oxirgi, birinchi" formatida bitta qatorni qaytaring.
     Args:
         birinchi: ko'cha
         oxirgi: ko'cha
     Qaytaradi:
         str: javobni qaytarish.
    """
    last=last+","+first
    return last
print(main("Otabek","Tursunov"))