def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        last_item = items.pop()
        items_list = ", ".join(items)
        items_with_oxford = f'{items_list}, and {last_item}'
        return items_with_oxford
