def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec,tuple) or len(rec)!=3:
        raise ValueError
    fio, group, gpa = rec

    if not isinstance(gpa, (int, float)):
        raise TypeError
    if not (0.0 <= gpa <= 5.0):
        raise ValueError

    fio = " ".join(fio.split())
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError

    surname = parts[0].capitalize()
    initials = "".join(name[0].upper() + "." for name in parts[1:])

    group = group.strip()
    if not group:
        raise ValueError

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("  сидорова   ", "ABB-01", 3.999)))