# 当前周数和总周数
current_week = 5
total_weeks = 20

# 计算剩余的周数
remaining_weeks = total_weeks - current_week

# 每周有 7天
days_from_remaining_weeks = remaining_weeks * 7

# 当前周剩余的天数（今天是星期五，剩余 2天到下一个星期一）
days_in_current_week = 2  # 从星期五到下一个星期一

# 计算总天数
total_days_until_holiday = days_from_remaining_weeks + days_in_current_week

print(f"距离放假还有 {total_days_until_holiday} 天。")
