def tower_of_hanoi(num_of_disk,start_tower,temp_tower,final_tower):
    if num_of_disk == 1:
        print("Move disk 1 from ",start_tower,'to ',final_tower)
        return
    else:
        tower_of_hanoi(num_of_disk - 1,start_tower,final_tower,temp_tower)
        print("Move disk ",num_of_disk,'from disk ',start_tower,'to',final_tower)
        tower_of_hanoi(num_of_disk - 1,temp_tower,start_tower,final_tower)
    

tower_of_hanoi(10,'A','X','B')