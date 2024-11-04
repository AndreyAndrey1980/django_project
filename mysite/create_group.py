# Create default groups and permissions
from django.contrib.auth.models import Group, Permission

# Create a group
group = Group.objects.create(name='moders')

# Assign a permission to the group
moderator_permissions = ["set_false_product_published_status", "change_product_description", "change_product_category"]
for perm in moderator_permissions:
    permission = Permission.objects.get(codename=perm)
    group.permissions.add(permission)

# Save the group
group.save()
