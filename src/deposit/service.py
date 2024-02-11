from dateutil.relativedelta import relativedelta
from . import schemas


def calculate_deposit(deposit_data:schemas.Deposit) -> dict:
    """Calculate deposit amounts by months in period

    Args:
        deposit_data (schemas.Deposit): Model of requested data for calculation with first date, amount, rate, periods

    Returns:
        dict: Dict with date and amount of deposits on current date
    """
    profit_by_dates = {}
    amount = deposit_data.amount
    for iteration in range(1, deposit_data.periods + 1):
        date_of_payment = str(deposit_data.date + relativedelta(months=iteration - 1))
        amount = ((12 * 100) + deposit_data.rate) * amount / (12 * 100)
        profit_by_dates.update({ date_of_payment : int(amount) if round(amount, 2).is_integer() else round(amount, 2)})
    return profit_by_dates