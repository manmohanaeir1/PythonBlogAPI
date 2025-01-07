from repository.BlogRepository import get_blogs, get_blog, create_blog, update_blog, delete_blog

def get_all_blogs():
    return get_blogs()

def get_single_blog(id):
    return get_blog(id)

def create_new_blog(title, description):
    return create_blog(title, description)


def update_existing_blog(id, title, description):
    return update_blog(id, title, description)


def remove_blog(id):
    return delete_blog(id)


