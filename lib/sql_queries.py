select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        bears.name
    FROM bears
    ORDER BY name
"""

# OKAY TILL THIS PART

alive = True
dead = 0

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = f"""
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY age   
    WHERE alive = {alive};
"""

select_oldest_bear_and_returns_name_and_age = """
    Write your SQL query here
"""
select_youngest_bear_and_returns_name_and_age = """
    Write your SQL query here
"""