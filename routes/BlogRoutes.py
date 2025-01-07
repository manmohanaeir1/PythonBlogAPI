from flask import Blueprint, jsonify, request


from services.Service import get_blogs_by_id, get_all_blogs, create_new_blog, update_existing_blog, remove_blog


blog_bp = Blueprint('blogs', __name__)


@blog_bp.route('/api/v1/blogs', methods=['GET'])
def get_blogs():
    blogs = get_all_blogs()
    blog_list =  jsonify({'id': blog.id, 'title': blog.title, 'description': blog.description} for blog in blogs) 
    return jsonify({'blogs': blog_list})