def obj_to_post(obj):
    post = dict(vars(obj))
    
    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M')
    else:
        post['update_dt'] = ''
        
    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []
        
    if obj.owner:
        post['owner'] = obj.owner.username
    else:
        post['owner'] = 'Anonymous'
        
    del post['_state']
    
    return post


def prev_next_post(obj):
    try:
        prev_obj = obj.get_prev()
        prevDict = {'id' : prev_obj.id, 'title' : prev_obj.title }
    except obj.DoesNotExist as e:
        prevDict = {}
        
    try:
        next_obj = obj.get_next()
        nextDict = {'id' : next_obj.id, 'title' : next_obj.title }
    except obj.DoesNotExist as e:
        nextDict = {}
        
    return prevDict, nextDict

def make_tag_cloud(qsTag):
    minCount = min([tag.count for tag in qsTag])
    maxCount = max([tag.count for tag in qsTag])
    
    minWeight, maxWegiht = 1, 3
    def get_weight_func(minWeight, maxWeight):
        if minCount - maxCount == 0:
            factor = 1.0
        else:
            factor = (maxWegiht - minWeight) / (maxCount - minCount)
        
        def func(count):
            weight = round(minWeight + (factor * (count - minCount)))
            return weight
        return func
    
    weight_func = get_weight_func(minWeight, maxWegiht)
    tagList = list()
    for tag in qsTag:
        weight = weight_func(tag.count)
        tagList.append({
            'name' : tag.name,
            'count' : tag.count,
            'weight' : weight,
        })
    return tagList