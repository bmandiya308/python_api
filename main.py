from flask import Flask, request, jsonify
from flask_restful import Api, Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    author = db.Column(db.String(30))
    first_sentence = db.Column(db.String(100))
    published = db.Column(db.Integer)

    #def __repr__(self):
        #return f"Book(id = {id},title = {title}, author = {author}, first_sentence = {first_sentence},  published = {published})"

#db.create_all()  ##one time activity , otherwise it will overrid

put_args = reqparse.RequestParser()
put_args.add_argument("id",type=int,help="Id is uniq", required=True)
put_args.add_argument("title",type=str,help="title", required=True)
put_args.add_argument("author",type=str,help="Name of Author please", required=True)
put_args.add_argument("first_sentence",type=str,help="Description")
put_args.add_argument("published",type=int,help="published Year")

update_args = reqparse.RequestParser()
update_args.add_argument("id",type=int,help="Id is uniq")
update_args.add_argument("title",type=str,help="title")
update_args.add_argument("author",type=str,help="Name of Author please")
update_args.add_argument("first_sentence",type=str,help="Description")
update_args.add_argument("published",type=int,help="published Year")

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'first_sentence': fields.String,
    'published': fields.String
}

def abort_if_id_doesnt_exist(id):
    if id not in books:
        abort(404, messgae="id is not valid")
def abort_if_id_already_exists(id):
    if id in books:
        abort(409, messgae="id already exists")

class Getdetails(Resource):

##Select
    @marshal_with(resource_fields) ##make return object serilisable
    def get(self,id):
        app.logger.info("Get info")
        result = Books.query.filter_by(id=id).first()
        if not result:
            #app.logger.debug(str(id) + ": Not found in system")
            #app.logger.error(str(id) + ": Not found in system")
            #app.logger.warning(str(id) + ": Not found in system")
            abort(404, message= str(id) + " - is not available")
        return result

##Insert
    @marshal_with(resource_fields)
    def post(self,id):
        result = Books.query.filter_by(id=id).first()
        if result:
            abort(409,message=str(id) + "- Already Created !")
        result = put_args.parse_args()
        book = Books(id=id,title=result['title'],author=result['author'],first_sentence=result['first_sentence'],published=result['published'])
        db.session.add(book)
        db.session.commit()
        return book,201

##Update
    @marshal_with(resource_fields)
    def patch(self,id):
        args = update_args.parse_args()
        result = Books.query.filter_by(id=id).first()
        if not result:
            abort(404, message=str(id) + " - is not available")
        if args['author']:
            result.author = args['author']
        if args['published']:
            result.published = args['published']
        db.session.commit()
        return result

##Delete
    @marshal_with(resource_fields)
    def delete(self,id):
        result = Books.query.filter_by(id=id).first()
        if not result:
            abort(404, message=str(id) + " - Not available so cant delete")
        Books.query.filter_by(id=id).delete()
        db.session.commit()
        return result

api.add_resource(Getdetails, "/getid/<int:id>")

# @app.route('/', methods = ['POST','GET'])
# def index():
#     return jsonify(books)

# @app.route('/getbook/<id>', methods = ['POST','GET'])
# def get(id):
#     return jsonify(books[int(id)])


if __name__ == '__main__':
    #app.run(host='192.168.43.96',port=8081,debug = True)
    import logging
    logging.basicConfig(filename='error.log',format='%(asctime)s - %(message)s',level=logging.DEBUG)
    app.run(host='0.0.0.0')
