class Stats(): #отслеживание статистики

  def __init__(self): #инициализация статистики
        self.reset_stats()
        self.run_game = True  #атрибут, отслеживающий есть ли еще жизни и можно ли продолжать игру
        with open('HIGH SCORE', 'r') as f:
            self.high_score = int(f.readline())


  def reset_stats(self): #статистика, изменяющаяся во время игры
         self.guns_left = 2
         self.score = 0


