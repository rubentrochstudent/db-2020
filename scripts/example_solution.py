"""
This is a dummy script of a 'solution' of the first 3 queries.

As you can see, a solution contains python functions and nothing else.
"""


def query_01(connection, column_names):
    # Bouw je query
    query="""
    select    name, yearID, HR
    from      Teams
    order by  HR DESC;
    """
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df

def query_02(connection, column_names, datum_x="1980-01-16"):
    # Bouw je query
    query="""
    select    nameFirst, nameLast, birthYear, birthMonth, birthDay
    from      MASTER
    where     debut > '{}'
    order by  nameLast ASC;
    """.format(
        datum_x
    )
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df

def query_03(connection, column_names):
    # Bouw je query
    query="""
    select    p.nameFirst, p.nameLast, t.name
    from      Managers as m NATURAL JOIN MASTER as p NATURAL JOIN Teams as t
    where     m.plyrMgr = 'Y'
    group by  t.teamID, p.playerID;
    order by  t.name ASC;
    """
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df
