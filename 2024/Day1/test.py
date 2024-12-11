# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/01 13:51:05 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

out = open("out", mode ="w")

with open("input", mode="r") as file:
    lines = file.readlines()

column1 = []
column2 = []

for line in lines:
    columns = line.split()
    if len(columns) == 2:
        column1.append(columns[0])
        column2.append(columns[1])

for i in column1:
    out.write(i)
    out.write(" ")
for j in column2:
	out.write(j)
	out.write(" ")