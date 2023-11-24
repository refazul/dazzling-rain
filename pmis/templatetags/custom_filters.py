from django import template
register = template.Library()

@register.filter(name='date_diff')
def date_diff(value, arg):
    days = (value - arg).days
    years, months, days = years_months_from_days(days)
    return f"{years}-{months}-{days}"

@register.filter(name='yes_no')
def yes_no(value):
    value = 'YES' if value == 'Y' else 'NO'
    return f"{value}"

@register.filter(name='male_female')
def male_female(value):
    value = 'MALE' if value == 'M' else 'FEMALE'
    return f"{value}"

@register.filter(name='dash_no')
def dash_no(value):
    value = '-' if value == 'N' else value
    return f"{value}"

def years_months_from_days(total_days):
    # Average lengths
    days_in_year = 365  # Accounting for leap years
    days_in_month = 30  # Average month length

    # Calculate years and months
    years = int(total_days / days_in_year)
    remaining_days = total_days % days_in_year
    months = int(remaining_days / days_in_month)
    remaining_days = total_days % days_in_month
    days = remaining_days

    return years, months, days
