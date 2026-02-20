set_of_tickets = input().split()
count = 1
for ticket in set_of_tickets:
    if len(ticket) % 2 == 0:
        half = len(ticket) // 2
        first_sum = 0
        for i in range(half):
            first_sum += int(ticket[i])
        second_sum = 0
        for i in range(half, len(ticket)):
            second_sum += int(ticket[i])
        if first_sum == second_sum:
            print(count)
            break
    count += 1