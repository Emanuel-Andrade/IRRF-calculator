class Income_Tax:
  def __init__(self, monthly_income):
    self._monthly_income = monthly_income
    self._exemption_fee = 1903.98
    self._max_first_track = 2826.65
    self._first_track_fee = 0.075
    self._max_second_track = 3751.05
    self._second_track_fee = 0.15
    self._max_third_track = 4664.68
    self._third_track_fee = 0.225
    self._max_fee = 0.275
  
  def _need_to_pay_fee(self):
    if(self._monthly_income <= self._exemption_fee): 
      return False
    else: return True

  def _tax_rate(self):
    first_amount_to_pay = self.first_rate_amount(self._monthly_income)
    second_amount_to_pay = self.second_rate_amount(self._monthly_income)
    thid_amount_to_pay = self.third_rate_amount(self._monthly_income)
    fourth_amount_to_pay = self.fourth_rate_amount(self._monthly_income)
    total = first_amount_to_pay + second_amount_to_pay + thid_amount_to_pay + fourth_amount_to_pay
    return total 
        
  def first_rate_amount(self, amount_to_tax):
    if(amount_to_tax >= self._max_first_track):
     return (self._max_first_track - self._exemption_fee) * self._first_track_fee
    return (amount_to_tax - self._exemption_fee) * self._first_track_fee
  
  def second_rate_amount(self, amount_to_tax):
    if(amount_to_tax >= self._max_second_track):
      return (self._max_second_track - self._max_first_track) * self._second_track_fee
    elif amount_to_tax <= self._max_first_track:
      return 0
    return (amount_to_tax - self._max_first_track) * self._second_track_fee
  
  def third_rate_amount(self, amount_to_tax):
    if(amount_to_tax >= self._max_third_track):
      return (self._max_third_track - self._max_second_track) * self._third_track_fee
    elif amount_to_tax <= self._max_second_track:
      return 0
    return (amount_to_tax - self._max_second_track) * self._third_track_fee
  
  def fourth_rate_amount(self, amount_to_tax):
    if amount_to_tax <= self._max_third_track:
      return 0
    return (amount_to_tax - self._max_third_track) * self._max_fee
    
  def execute(self):
      if(not self._need_to_pay_fee()):
        return f'Sua faixa de salário não e necessário pagar imposto de renda!'
      tax_value = self._tax_rate()
      return f'Seu valor de imposto e {round(tax_value,2)}'
  
