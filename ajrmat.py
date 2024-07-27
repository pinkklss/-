team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

team1_string = "В команде Мастера кода участников: %d !" % team1_num
print(team1_string)

total_participants_string = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(total_participants_string)

score_2_string = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score_2_string)

team2_time_string = "Волшебники данных решили задачи за {:.2f} с !".format(team2_time)
print(team2_time_string)

scores_string = f"Команды решили {score_1} и {score_2} задач."
print(scores_string)

result_string = f"Результат битвы: {challenge_result}"
print(result_string)

avg_time_string = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(avg_time_string)
