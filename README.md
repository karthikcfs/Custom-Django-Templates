# Custom-Django-Templates

1. Create templatetags folder in inside application
2. Need to create empty __init__.py
3. Create your custom_tags.py and write your code.
4. In HTML, Need to load the custom_tags.py by {% load custom_tags %}
5. After that you can access your custom_tag - {{product_dict|lookup:product}}
