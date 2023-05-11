import copy
import sys

try:
    hidden1 = [
    ["  ","A","B","C","D","E","F","G","H","I","J"],
    ["1 ","-","-","-","-","-","-","-","-","-","-"],
    ["2 ","-","-","-","-","-","-","-","-","-","-"],
    ["3 ","-","-","-","-","-","-","-","-","-","-"],
    ["4 ","-","-","-","-","-","-","-","-","-","-"],
    ["5 ","-","-","-","-","-","-","-","-","-","-"],
    ["6 ","-","-","-","-","-","-","-","-","-","-"],
    ["7 ","-","-","-","-","-","-","-","-","-","-"],
    ["8 ","-","-","-","-","-","-","-","-","-","-"],
    ["9 ","-","-","-","-","-","-","-","-","-","-"],
    ["10","-","-","-","-","-","-","-","-","-","-"]]


    hidden2 = [
    ["  ","A","B","C","D","E","F","G","H","I","J"],
    ["1 ","-","-","-","-","-","-","-","-","-","-"],
    ["2 ","-","-","-","-","-","-","-","-","-","-"],
    ["3 ","-","-","-","-","-","-","-","-","-","-"],
    ["4 ","-","-","-","-","-","-","-","-","-","-"],
    ["5 ","-","-","-","-","-","-","-","-","-","-"],
    ["6 ","-","-","-","-","-","-","-","-","-","-"],
    ["7 ","-","-","-","-","-","-","-","-","-","-"],
    ["8 ","-","-","-","-","-","-","-","-","-","-"],
    ["9 ","-","-","-","-","-","-","-","-","-","-"],
    ["10","-","-","-","-","-","-","-","-","-","-"]]  #I created the 2d empty list that the program prints
    
    def hidden_joiner(h):#This function turns hidden list to strings
        a = ""
        for lines in h:
            a += " ".join(lines) + "\n"
        return a

    def write_output(output_lines):#This is writer to the empty file.
        with open("Battleship.out", "w") as outputs_file:
            outputs_file.writelines(output_lines)


    ship_count = {"C":1, "B":2, "D":1, "S":1, "P":4}
    ship_count_1 = {"C":1, "B":2, "D":1, "S":1, "P":4}
    ship_count_2 = {"C":1, "B":2, "D":1, "S":1, "P":4}
    ship_size = {"C":5, "B":4, "D":3, "S":3, "P":2}
    damaged_ship_1 = {"C":0, "B":0, "D":0, "S":0, "P":0}
    damaged_ship_2 = {"C":0, "B":0, "D":0, "S":0, "P":0}#I will count how many ships remain

    pos1 = []

    with open(sys.argv[1], "r") as inputs_file:
        input_lines = inputs_file.read().splitlines()

        counter_p=1
        counter_b=1
        ### HORIZONTAL
        for values in input_lines:
            ## FOR 'P'
            new_values = values.replace('P;P', 'P' + str(counter_p) + ';P' + str(counter_p))#This is for distinguishing which named same ships.
            if values != new_values:
                counter_p+=1
            
            ## FOR 'B'
            new_values_b = new_values.replace('B;B;B;B', 'B' + str(counter_b) + ';B' + str(counter_b) + ';B' + str(counter_b) + ';B' + str(counter_b))
            if new_values_b != new_values:
                counter_b+=1
            a = new_values_b.split(";")
            pos1.append(a)

        ### VERTICAL  
        for jdx,line_pos1 in enumerate(pos1):
            if 'P' in line_pos1:
                p_index = line_pos1.index('P')
                down = pos1[jdx+1][p_index]
                if down == 'P':
                    new='P' + str(counter_p)
                    pos1[jdx][p_index] = new
                    pos1[jdx+1][p_index]= new
                    counter_p+=1
            if 'B' in line_pos1:
                b_index = line_pos1.index('B')
                down = pos1[jdx+1][b_index]
                if down == 'B':
                    down_2 = pos1[jdx+1][b_index]
                    if down_2 == 'B':
                        down_3 = pos1[jdx+2][b_index]
                        if down_3 == 'B':
                            new='B' + str(counter_b)
                            pos1[jdx][b_index] = new
                            pos1[jdx+1][b_index]= new
                            pos1[jdx+2][b_index]= new
                            pos1[jdx+3][b_index]= new
                            counter_b+=1
                    

    pos2 = []

    with open(sys.argv[2], "r") as comp_file:
        comp_lines = comp_file.read().splitlines()
        
        counter_p=1
        counter_b=1
        ### HORIZONTAL
        for values in comp_lines:
            ## FOR 'P'
            new_values = values.replace('P;P', 'P' + str(counter_p) + ';P' + str(counter_p))
            if values != new_values:
                counter_p+=1
            
            ## FOR 'B'
            new_values_b = new_values.replace('B;B;B;B', 'B' + str(counter_b) + ';B' + str(counter_b) + ';B' + str(counter_b) + ';B' + str(counter_b))
            if new_values_b != new_values:
                counter_b+=1
            a = new_values_b.split(";")
            pos2.append(a)

        ### VERTICAL  
        for jdx,line_pos2 in enumerate(pos2):
            if 'P' in line_pos2:
                p_index = line_pos2.index('P')
                down = pos2[jdx+1][p_index]
                if down == 'P':
                    new='P' + str(counter_p)
                    pos2[jdx][p_index] = new
                    pos2[jdx+1][p_index]= new
                    counter_p+=1
            if 'B' in line_pos2:
                b_index = line_pos2.index('B')
                down = pos2[jdx+1][b_index]
                if down == 'B':
                    down_2 = pos2[jdx+1][b_index]
                    if down_2 == 'B':
                        down_3 = pos2[jdx+2][b_index]
                        if down_3 == 'B':
                            new='B' + str(counter_b)
                            pos2[jdx][b_index] = new
                            pos2[jdx+1][b_index]= new
                            pos2[jdx+2][b_index]= new
                            pos2[jdx+3][b_index]= new
                            counter_b+=1
                    

    with open(sys.argv[3], "r") as inputs_file:
        input_lines = inputs_file.read().splitlines()
        for values in input_lines:
            shoot1 = values.split(";")
            shoot1 = shoot1[:-1]#last element of the input is ";" so i had to delete the last element
            for i in shoot1:
                shoot = i.split(",")
                if int(shoot[0]) > 10 or int(shoot[0]) < 0 or shoot[1] not in ["A","B","C","D","E","F","G","H","I","J"]:
                    raise AssertionError


    with open(sys.argv[4], "r") as comp_file:
        comp_lines = comp_file.read().splitlines()
        for values in comp_lines:
            shoot2 = values.split(";")
            shoot2 = shoot2[:-1]
            for i in shoot1:
                shoot = i.split(",")
                if int(shoot[0]) > 10 or int(shoot[0]) < 0 or shoot[1] not in ["A","B","C","D","E","F","G","H","I","J"]:
                    raise AssertionError

    def turn(player):# it shows the turn
        if player == 1:
            hamle = shoot1[0].split(",")
            shoot1.pop(0)
            letter = hamle[1]
            return int(hamle[0]), get_index_for_letter(letter), letter
        elif player == 2:
            hamle = shoot2[0].split(",")
            shoot2.pop(0)
            letter = hamle[1]
            return int(hamle[0]), get_index_for_letter(letter), letter

    def get_index_for_letter(letter):
        return hidden2[0].index(letter)


    def main():# the main algorithm of the game
        move = 1
        round = 0
        output='Battle of Ships Game\n'
        while True:
            before_hidden_1=copy.deepcopy(hidden1)
            before_hidden_2=copy.deepcopy(hidden2)

            if move == 1:
                current = turn(1)
                x=current[0]-1
                y=current[1]-1

                line = pos2[x]

                if line[y] == '':
                    sign = 'O'
                else:
                    set_ship_count(2,line[y])
                    sign = 'X'

                set_hidden(1,sign,x,y)

                if len(shoot2) > 0:
                    move = 2
                    round += 1
                    output += "\nPlayer1's Move\n"
                else:
                    output += "\nPlayer1 Wins\n\nFinal Information\n\n"
                    output += "Player1's Board\tPlayer2's Board\n"
                    output += "\n".join("{}\t{}".format(' '.join(x), ' '.join(y)) for x, y in zip(hidden1, hidden2))
                    output += get_current_ship_status()
                    break
                    
            elif move == 2:

                current = turn(2)

                x=current[0]-1
                y=current[1]-1

                line = pos1[x]

                if line[y] == '':
                    sign = 'O'
                else:
                    set_ship_count(1,line[y])
                    sign = 'X'

                set_hidden(2,sign,x,y)

                if len(shoot1) > 0:
                    move = 1
                    output += "\nPlayer2's Move\n"
                else:
                    output += "\nPlayer2 Wins!\n\nFinal Information\n\n"
                    output += "Player1's Board\t\tPlayer2's Board\n"
                    output += "\n".join("{}\t{}".format(' '.join(x), ' '.join(y)) for x, y in zip(hidden1, hidden2))#it prints the tables side by side
                    output += get_current_ship_status()
                    
                    break
            else:
                break

            output += "\nRound:{}\t\t\t\tGrid Size: 10x10\n\n".format(round)
            output += "Player1's Hidden Board\tPlayer2's Hidden Board\n"
            output += "\n".join("{}\t{}".format(' '.join(x), ' '.join(y)) for x, y in zip(before_hidden_1, before_hidden_2))
            output += get_current_ship_status()
            output += "\n\nEnter your move: {},{}\n".format(current[0],current[2])
            

        return output

    def get_current_ship_status():#shows how many ships remained
        ship_output = ''
        # C
        c1 = ''
        for i in range(ship_count_1["C"]):
            c1 += ' -'
        for j in range(ship_count["C"]-ship_count_1["C"]):
            c1 += ' x'
        ship_output += '\n\nCarrier {}'.format(c1)

        c2 = ''
        for i in range(ship_count_2["C"]):
            c2 += ' -'
        for j in range(ship_count["C"]-ship_count_2["C"]):
            c2 += ' x'
        ship_output += '\t\tCarrier {}'.format(c2)
        # B
        b1 = ''
        for i in range(ship_count_1["B"]):
            b1 += ' -'
        for j in range(ship_count["B"]-ship_count_1["B"]):
            b1 += ' x'
        ship_output += '\nBattleship {}'.format(b1)

        b2 = ''
        for i in range(ship_count_2["B"]):
            b2 += ' -'
        for j in range(ship_count["B"]-ship_count_2["B"]):
            b2 += ' x'
        ship_output += '\t\tBattleship {}'.format(b2)
        # D
        d1 = ''
        for i in range(ship_count_1["D"]):
            d1 += ' -'
        for j in range(ship_count["D"]-ship_count_1["D"]):
            d1 += ' x'
        ship_output += '\nDestroyer {}'.format(d1)
        
        d2 = ''
        for i in range(ship_count_2["D"]):
            d2 += ' -'
        for j in range(ship_count["D"]-ship_count_2["D"]):
            d2 += ' x'
        ship_output += '\t\tDestroyer {}'.format(d2)
        # S
        s1 = ''
        for i in range(ship_count_1["S"]):
            s1 += ' -'
        for j in range(ship_count["S"]-ship_count_1["S"]):
            s1 += ' x'
        ship_output += '\nSubmarine {}'.format(s1)
        
        s2 = ''
        for i in range(ship_count_2["S"]):
            s2 += ' -'
        for j in range(ship_count["S"]-ship_count_2["S"]):
            s2 += ' x'
        ship_output += '\t\tSubmarine {}'.format(s2)
        # P
        p1 = ''
        for i in range(ship_count_1["P"]):
            p1 += ' -'
        for j in range(ship_count["P"]-ship_count_1["P"]):
            p1 += ' x'
        ship_output += '\nPatrol Boat {}'.format(p1)

        p2 = ''
        for i in range(ship_count_2["P"]):
            p2 += ' -'
        for j in range(ship_count["P"]-ship_count_2["P"]):
            p2 += ' x'
        ship_output += '\tPatrol Boat {}'.format(p2)

        
        return ship_output

    def set_hidden(player,sign,x,y):
        x+=1
        y+=1
        if player == 1:
            hidden2[x][y]=sign
        elif player == 2:
            hidden1[x][y]=sign
        else:
            print('error')

    p_damage_1={}
    p_damage_2={}
    b_damage_1={}
    b_damage_2={}

    def set_ship_count(player,ship):#ship counter
        if player == 1:
            if 'P' in list(ship):
                if ship in p_damage_1:
                    p_damage_1[ship] = p_damage_1[ship] + 1
                else:
                    p_damage_1[ship] = 1

                if p_damage_1[ship] != 2:
                    return
                else:
                    ship_count_1["P"] = ship_count_1["P"] - 1

            if 'B' in list(ship):
                if ship in b_damage_1:
                    b_damage_1[ship] = b_damage_1[ship] + 1
                else:
                    b_damage_1[ship] = 1

                if b_damage_1[ship] != 4:
                    return
                else:
                    ship_count_1["B"] = ship_count_1["B"] - 1

            if 'C' in ship or 'S' in ship or 'D' in ship:
                damaged_ship_1[ship] = damaged_ship_1[ship] + 1
                if damaged_ship_1[ship] != ship_size[ship]:
                    return
                else:
                    ship_count_1[ship] = ship_count_1[ship] - 1

        elif player == 2:
            if 'P' in list(ship):
                if ship in p_damage_2:
                    p_damage_2[ship] = p_damage_2[ship] + 1
                else:
                    p_damage_2[ship] = 1
                
                if p_damage_2[ship] != 2:
                    return
                else:
                    ship_count_2["P"] = ship_count_2["P"] - 1
                    
            if 'B' in list(ship):
                if ship in b_damage_2:
                    b_damage_2[ship] = b_damage_2[ship] + 1
                else:
                    b_damage_2[ship] = 1

                if b_damage_2[ship] != 4:
                    return
                else:
                    ship_count_2["B"] = ship_count_2["B"] - 1
                    

            if 'C' in ship or 'S' in ship or 'D' in ship:
                damaged_ship_2[ship] = damaged_ship_2[ship] + 1
                if damaged_ship_2[ship] != ship_size[ship]:
                    return
                else:
                    ship_count_2[ship] = ship_count_2[ship] - 1

        else:
            print('error')
        
    output_file_lines =  main()
    write_output(output_file_lines)
except IOError:
    write_output("IOError: input file(s) {} or {} or {} or {} is/are not reachable.").format(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
except IndexError:
    write_output('IndexError: shooting files {} and {} must be like "8,A;2,E;4,F;"').format(sys.argv[3],sys.argv[4])
except ValueError:
    write_output('ValueError: shooting files {} and {} must be like "8,A;2,E;4,F;"').format(sys.argv[3],sys.argv[4])
except AssertionError:
    write_output('AssertionError: Invalid Operation. The table is 10x10')
except:
    write_output('kaBOOM: run for your life!')

