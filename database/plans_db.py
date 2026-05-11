from database.mongo import plans

# CREATE PLAN
async def create_plan(name, price, days, limit):

    await plans.insert_one({
        "name": name,
        "price": price,
        "days": days,
        "limit": limit
    })

# GET PLAN
async def get_plan(name):

    return await plans.find_one({
        "name": name
    })

# GET ALL PLANS
async def get_all_plans():

    return await plans.find().to_list(length=None)

# DELETE PLAN
async def delete_plan(name):

    await plans.delete_one({
        "name": name
    })# Plans DB functions
