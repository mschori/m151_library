from rest_framework import serializers
from .models import Book, Author, Customer, Place, Rent


class BookSerializer(serializers.ModelSerializer):
    author_pks = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='authors', write_only=True,
                                                    many=True, label='Authors')

    def __init__(self, *args, **kwargs):
        # Get additional parameters from constructor
        depth = kwargs.pop('depth', None)
        fields = kwargs.pop('fields', None)

        # Add author_pks to fields if field is not None from constructor
        fields.append('author_pks') if fields is not None else None

        # Set Meta-Tags
        self.Meta.depth = depth if depth is not None else 1
        self.Meta.fields = fields if fields is not None else '__all__'

        # Call super-constructor
        super(BookSerializer, self).__init__()

    class Meta:
        model = Book


class AuthorSerializer(serializers.ModelSerializer):
    # Create field-list for nested-books
    book_fields = ['id', 'isbn', 'title', 'pages', 'is_borrowed']

    # Create book-list for nested books with options
    book_list = BookSerializer(many=True, read_only=True, depth=0, fields=book_fields)

    # Change image-options to allow post/put/patch without an image
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Author
        fields = '__all__'
        depth = 1


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):
    customer_pk = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer',
                                                     write_only=True, label='Customer')
    book_pk = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='books', write_only=True,
                                                 many=True, label='Books')

    class Meta:
        model = Rent
        fields = '__all__'
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    rent_list = RentSerializer(many=True, read_only=True)
    place_pk = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(), source='place', write_only=True,
                                                  label='Place')

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1
