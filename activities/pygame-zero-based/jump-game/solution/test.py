def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count

def get_members(group):
    match group:
        case "everyone":
            return ["sales", "engineering"]
        case "sales":
            return ["a", "b"]
        case "engineering":
            return ["c"]

def is_group(member):
    return member in ["everyone", "sales", "engineering"]

print("everyone",  count_users("everyone"))
print("sales", count_users("sales"))
print("engineering", count_users("engineering"))
