#1076 저항

color_list = ['black','brown','red','orange','yellow','green',
              'blue','violet','grey', 'white']

f_color = color_list.index(input())
s_color = color_list.index(input())
t_color = color_list.index(input())

print((f_color*10+s_color)*(10**t_color))