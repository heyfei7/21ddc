def part_str_at(s, at):
    return s[:at], s[at:]


def format_before_decimal(s):
    parts = [s]
    while len(parts[0]) > 3:
        f, n = part_str_at(parts[0], -3)
        parts.insert(1, n)
        parts[0] = f

    return ",".join(parts)


def format_after_decimal(s, sigfig):
    if sigfig < len(s):
        next_fig = s[sigfig]
        s = s[:sigfig]
        if int(next_fig) >= 5:
            s = s[:-1] + str(int(s[-1]) + 1)
    else:
        s += "0" * (sigfig - len(s))
    return s


def decimal(num, sigfig):
    total_str = str(num)
    decimal_i = total_str.index(".")
    before_decimal = format_before_decimal(total_str[:decimal_i])
    after_decimal = format_after_decimal(total_str[decimal_i+1:], sigfig)
    return before_decimal + "." + after_decimal


def money(i, sigfig):
    return "$" + decimal(i, sigfig)
