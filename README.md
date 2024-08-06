# api_imdb

'''
When deserializing data, you always need to call is_valid()


Differences in Detail
Field Definition:
Serializer: Fields must be defined manually.
ModelSerializer: Fields are automatically generated based on the model.

Boilerplate Code:
Serializer: Requires more code, especially for defining fields and handling create/update methods.
ModelSerializer: Reduces boilerplate by automatically handling these aspects.

Use Cases:
Serializer: Best for custom, non-model-based data or when you need extensive customization and validation logic.
ModelSerializer: Best for straightforward CRUD operations on Django models.

Automatic Methods:
Serializer: You must define create and update methods manually.
ModelSerializer: These methods are generated automatically based on the model.

Choosing Between Serializer and ModelSerializer
Use Serializer when you have non-model data, complex validation logic, or need full control over the serialized data.
Use ModelSerializer when working with Django models and you want to quickly create a serializer with minimal custom logic.'''




# Permissions :
In Django, permissions are a way to control access to different parts of your application. They help manage what actions a user can perform, such as reading, writing, or deleting data. Django's permission system is very flexible and can be customized to fit the needs of your application.