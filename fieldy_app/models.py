from django.db import models

TYPE = [('contract_company', 'contract_company'), ('vendor_company', 'vendor_company'), ('customer_company', 'customer_company')]
CUSTOMER_TYPE = [('contact_customer', 'contact_customer'), ('company_customer', 'company_customer')]
DELIVERY_TYPE = [('office', 'office'), ('residence', 'residence')]


# Create your models here.
class CustomerGroup(models.Model):
    id_customer_group = models.IntegerField(primary_key=True, blank=False)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=191, blank=True, null=True)
    fax = models.CharField(max_length=191, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    id_address_billing = models.IntegerField(blank=True, null=True)
    id_address_shipping = models.IntegerField(blank=True, null=True)
    id_address_front = models.IntegerField(blank=True, null=True)
    files = models.TextField(blank=True, null=True)
    id_customer_plan = models.IntegerField(blank=True, null=True)
    id_country = models.IntegerField(blank=True, null=True)
    lead_source = models.CharField(max_length=191, blank=True, null=True)
    contact_person_name = models.TextField(blank=True, null=True)
    contact_person_first_name = models.TextField(blank=True, null=True)
    contact_person_last_name = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=265, choices=TYPE)
    customer_type = models.CharField(max_length=265, choices=CUSTOMER_TYPE)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'customer_group'


class Users(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.TextField()
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    job_title = models.TextField(blank=True, null=True)
    social_media_handles = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    email_verified_at = models.DateTimeField(auto_now=True, blank=True)
    password = models.TextField()
    remember_token = models.CharField(max_length=191, blank=True, null=True)
    phone = models.CharField(max_length=191, blank=True, null=True)
    secondary_phone = models.CharField(max_length=191, blank=True, null=True)
    home_phone = models.CharField(max_length=191, blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    joining_date = models.DateTimeField(auto_now=True, blank=True)
    user_image = models.CharField(max_length=191, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    service_type_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    permission_overwrite = models.IntegerField()
    relieve_date = models.DateTimeField(auto_now=True, blank=True)
    user_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    is_contractor = models.IntegerField(blank=True, null=True)
    id_customer_group = models.IntegerField(blank=True, null=True)
    regional_setting = models.JSONField(blank=False, null=True)
    inactive_by_subscription = models.IntegerField(blank=True, null=True)
    financial_setting = models.JSONField(blank=False, null=True)
    invited_by = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'users'


class Addresses(models.Model):
    id_address = models.IntegerField(primary_key=True, blank=False)
    id_tenant = models.IntegerField(blank=True, null=True)
    branch_name = models.TextField(blank=True, null=True)
    branch_email = models.TextField(blank=True, null=True)
    branch_mobile_number = models.CharField(max_length=191, blank=True, null=True)
    contact_person_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    line_1 = models.TextField(blank=True, null=True)
    line_2 = models.TextField(blank=True, null=True)
    landmark = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=191, blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    state_code = models.CharField(max_length=191, blank=True, null=True)
    id_country = models.CharField(max_length=191, blank=True, null=True)
    delivery_type = models.CharField(max_length=265, choices=DELIVERY_TYPE)
    coords = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'addresses'


class CustomerGroupAddresses(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    tenant_id = models.IntegerField()
    id_customer_group = models.IntegerField()
    id_address = models.IntegerField()
    is_primary = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'customer_group_addresses'


