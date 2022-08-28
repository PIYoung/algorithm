def gnomes_is_ordered_or_not(gnomes):
    is_ordered = False
    order_check_list = []
    for idx in range(len(gnomes) - 1):
        check_num = gnomes[idx] - gnomes[idx+1]
        order_check_list.append(check_num < 0)
        
    if len(set(order_check_list)) == 1:
        is_ordered = True
        
    return is_ordered
        

def gnome_sequencing(gnomes_list):
    print("Gnomes:")
    for gnomes in gnomes_list:
        is_ordered = gnomes_is_ordered_or_not(gnomes)
        
        if is_ordered:
            print("Ordered")
        else:
            print("Unordered")

            
if __name__ == "__main__":
    gnomes_list = []
    
    N = int(input())
    
    for _ in range(N):
        gnomes = list(map(int, input().split()))
        gnomes_list.append(gnomes)
        
    gnome_sequencing(gnomes_list)