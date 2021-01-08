from flask import request
from flask_restful import Resource, reqparse
from models.jobPostModel import JobPostModel


class JobPost(Resource):
    ''' Define view/resource Post for each job posting'''
    # instantiate parser and arguments to validate with the parser
    parser = reqparse.RequestParser()
    parser.add_argument("company",
                        type='str',
                        help='company is a required field',
                        required=True,)
    parser.add_argument("role",
                        type='str',
                        help='role is a required field',
                        required=True)
 
    parser.add_argument('status',
                        type='str',
                        help='status is a required field',
                        required=True)
    parser.add_argument('url',
                        type='str',
                        help='url is a required field',
                        required=True)   

    def get(self, post_id):
        '''Handle get request - return jobposts list  or detail given an id'''

        post = JobPostModel.find_by_id(post_id)
        # check the post belongs to the user asking
        if post: 
            return post.json()
        return {'message':"Post not found"}, 404

    def post(self):
        '''Handle put request - create a new jobPost object and add to collection
        Post an post object to the database
        '''
        # data is the args (key : value) sent from the form - if they do not exist, the parser will automatically send msg to the user
        data =  request.get_json()
        # data = JobPost.parser.parse_args()
        try:
            post = JobPostModel(role=data['role'], 
                                company=data['company'],
                                status=data['status'],
                                url=data['url'])
            print(post)
        except:
            return {"message":"An Error occurred creating the post, check that all valued are provided in correct form"}
        try:
            post.save_to_db()
        except:
            return {"message":"An Error occurred adding the post to the db"}, 500
        return post.json() , 201

    def delete(self, post_id):
        '''Handle delete request - delete a post instance if it exists on db'''
        post = JobPostModel.find_by_id(post_id)
        if post:
            post.delete_from_db()
            return {"message":"Post deleted"}
        return {"message": "Post does not exist or "}

    def put(self, post_id):
        '''
        Update existing resource with id if resource exists.
        If resrource does not exit, crate new post with given data
        '''
        data =  request.get_json()
        # data = JobPost.parser.parse_args()
        post = JobPostModel.find_by_id(post_id)

        if post is None: # post does NOT already exist 
            post = JobPostModel(role=data['role'], company=data['company'], status=data['status'], url=data['url']) # create new post object
        else:
            post.role = data['role'] #update the values of the existing post except id because it is still the same object
            post.company = data['company']
            post.url = data['url']
            post.status = data['status']
        post.save_to_db()
        return post.json()

    def patch(self, post_id):
        '''
        Update existing resource with id if resource exists.
        '''
        data =  request.get_json()
        # data = JobPost.parser.parse_args()
        post = JobPostModel.find_by_id(post_id)

        if post is None: # post does NOT already exist 
            return {"message": "post with given id does not exist"}
        else:
            post.status = data['status']
            post.save_to_db()
            return post.json()
            return {"message": "you cannot patch other users post"}


class JobPostList(Resource):
    '''Class to handle posts lists endpoint'''
    def get(self):
        '''Get post objects from the posts table'''
        posts = JobPostModel.query.all()
        # get JSON form for each post
        posts_json = [post.json() for post in posts] # 
        return {"posts": posts_json}
