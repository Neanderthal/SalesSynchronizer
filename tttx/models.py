# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContactsHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    hash = models.TextField()
    contact_id = models.BigIntegerField()
    position = models.PositiveIntegerField()
    accessed = models.DateTimeField(blank=True, null=True)
    cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contacts_history'


class ContactsRights(models.Model):
    group_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    writable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contacts_rights'
        unique_together = (('group_id', 'category_id'),)


class ShopAbtest(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    create_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shop_abtest'


class ShopAbtestVariants(models.Model):
    abtest_id = models.PositiveIntegerField()
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_abtest_variants'
        unique_together = (('abtest_id', 'code'),)


class ShopAffiliateTransaction(models.Model):
    contact_id = models.PositiveIntegerField()
    create_datetime = models.DateTimeField()
    order_id = models.PositiveIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    balance = models.DecimalField(max_digits=15, decimal_places=4)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_affiliate_transaction'


class ShopApiCourier(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.IntegerField()
    contact_id = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    orders_processed = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    api_token = models.CharField(max_length=32, blank=True, null=True)
    api_pin = models.CharField(max_length=32, blank=True, null=True)
    api_pin_expire = models.DateTimeField(blank=True, null=True)
    api_last_use = models.DateTimeField(blank=True, null=True)
    all_storefronts = models.IntegerField()
    rights_order_edit = models.IntegerField()
    rights_customer_edit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_api_courier'


class ShopApiCourierStorefronts(models.Model):
    courier_id = models.IntegerField()
    storefront = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_api_courier_storefronts'


class ShopCartItems(models.Model):
    code = models.CharField(max_length=32, blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField()
    sku_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=7)
    service_id = models.IntegerField(blank=True, null=True)
    service_variant_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_cart_items'


class ShopCategory(models.Model):
    left_key = models.IntegerField(blank=True, null=True)
    right_key = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField()
    parent_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    full_url = models.CharField(unique=True, max_length=255, blank=True, null=True)
    count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    edit_datetime = models.DateTimeField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)
    sort_products = models.CharField(max_length=32, blank=True, null=True)
    include_sub_categories = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_category'
        unique_together = (('parent_id', 'url'),)


class ShopCategoryOg(models.Model):
    category_id = models.IntegerField(primary_key=True)
    property = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_category_og'
        unique_together = (('category_id', 'property'),)


class ShopCategoryParams(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_category_params'
        unique_together = (('category_id', 'name'),)


class ShopCategoryProducts(models.Model):
    product_id = models.IntegerField()
    category_id = models.IntegerField(primary_key=True)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_category_products'
        unique_together = (('category_id', 'product_id'),)


class ShopCategoryRoutes(models.Model):
    category_id = models.IntegerField(primary_key=True)
    route = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_category_routes'
        unique_together = (('category_id', 'route'),)


class ShopCheckoutFlow(models.Model):
    code = models.CharField(max_length=32, blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    quarter = models.SmallIntegerField(blank=True, null=True)
    month = models.SmallIntegerField(blank=True, null=True)
    step = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_checkout_flow'


class ShopContactCategoryDiscount(models.Model):
    category_id = models.PositiveIntegerField(primary_key=True)
    discount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'shop_contact_category_discount'


class ShopCoupon(models.Model):
    code = models.CharField(unique=True, max_length=32)
    type = models.CharField(max_length=3)
    limit = models.IntegerField(blank=True, null=True)
    used = models.IntegerField()
    value = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    expire_datetime = models.DateTimeField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    create_contact_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'shop_coupon'


class ShopCurrency(models.Model):
    code = models.CharField(primary_key=True, max_length=3)
    rate = models.DecimalField(max_digits=18, decimal_places=10)
    rounding = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    round_up_only = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_currency'


class ShopCustomer(models.Model):
    contact_id = models.PositiveIntegerField(primary_key=True)
    total_spent = models.DecimalField(max_digits=15, decimal_places=4)
    affiliate_bonus = models.DecimalField(max_digits=15, decimal_places=4)
    number_of_orders = models.PositiveIntegerField()
    last_order_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_customer'


class ShopCustomersFilter(models.Model):
    name = models.CharField(max_length=255)
    hash = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    contact_id = models.IntegerField()
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_customers_filter'


class ShopDiscountBySum(models.Model):
    type = models.CharField(max_length=32)
    sum = models.DecimalField(max_digits=15, decimal_places=4)
    discount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'shop_discount_by_sum'


class ShopExpense(models.Model):
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    storefront = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    color = models.CharField(max_length=7, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_expense'


class ShopFeature(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=64)
    status = models.CharField(max_length=7)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    selectable = models.IntegerField()
    multiple = models.IntegerField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'shop_feature'


class ShopFeatureValuesColor(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    code = models.PositiveIntegerField(blank=True, null=True)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_feature_values_color'
        unique_together = (('feature_id', 'value'),)


class ShopFeatureValuesDimension(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    value = models.FloatField()
    unit = models.CharField(max_length=255)
    type = models.CharField(max_length=16)
    value_base_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_feature_values_dimension'
        unique_together = (('feature_id', 'value', 'unit', 'type'),)


class ShopFeatureValuesDouble(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_feature_values_double'
        unique_together = (('feature_id', 'value'),)


class ShopFeatureValuesRange(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    begin = models.FloatField(blank=True, null=True)
    end = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=255)
    type = models.CharField(max_length=16)
    begin_base_unit = models.FloatField(blank=True, null=True)
    end_base_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_feature_values_range'
        unique_together = (('feature_id', 'begin', 'end', 'unit', 'type'),)


class ShopFeatureValuesText(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_feature_values_text'


class ShopFeatureValuesVarchar(models.Model):
    feature_id = models.IntegerField()
    sort = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_feature_values_varchar'
        unique_together = (('feature_id', 'value'),)


class ShopFollowup(models.Model):
    name = models.CharField(max_length=255)
    delay = models.PositiveIntegerField()
    first_order_only = models.PositiveIntegerField()
    same_state_id = models.IntegerField(blank=True, null=True)
    subject = models.TextField()
    body = models.TextField()
    last_cron_time = models.DateTimeField()
    from_field = models.CharField(db_column='from', max_length=32, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    source = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    transport = models.CharField(max_length=5)
    state_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_followup'


class ShopImportexport(models.Model):
    plugin = models.CharField(max_length=64)
    sort = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_importexport'
        unique_together = (('plugin', 'id', 'sort'),)


class ShopNotification(models.Model):
    name = models.CharField(max_length=128)
    event = models.CharField(max_length=64)
    transport = models.CharField(max_length=5)
    source = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_notification'


class ShopNotificationParams(models.Model):
    notification_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_notification_params'
        unique_together = (('notification_id', 'name'),)


class ShopOrder(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField(blank=True, null=True)
    state_id = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=15, decimal_places=8)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    shipping = models.DecimalField(max_digits=15, decimal_places=4)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    assigned_contact_id = models.IntegerField(blank=True, null=True)
    paid_year = models.SmallIntegerField(blank=True, null=True)
    paid_quarter = models.SmallIntegerField(blank=True, null=True)
    paid_month = models.SmallIntegerField(blank=True, null=True)
    paid_date = models.DateField(blank=True, null=True)
    is_first = models.IntegerField()
    unsettled = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    shipping_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShopOrderItems(models.Model):
    order_id = models.IntegerField()
    name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    sku_id = models.IntegerField()
    sku_code = models.CharField(max_length=255)
    type = models.CharField(max_length=7)
    service_id = models.IntegerField(blank=True, null=True)
    service_variant_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    quantity = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    stock_id = models.IntegerField(blank=True, null=True)
    virtualstock_id = models.IntegerField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=4)
    total_discount = models.DecimalField(max_digits=15, decimal_places=4)
    tax_percent = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    tax_included = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_order_items'


class ShopOrderLog(models.Model):
    order_id = models.IntegerField()
    contact_id = models.IntegerField(blank=True, null=True)
    action_id = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    before_state_id = models.CharField(max_length=32)
    after_state_id = models.CharField(max_length=32)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order_log'


class ShopOrderLogParams(models.Model):
    order_id = models.IntegerField()
    log_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_order_log_params'
        unique_together = (('order_id', 'log_id', 'name'),)


class ShopOrderParams(models.Model):
    order_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_order_params'
        unique_together = (('order_id', 'name'),)


class ShopPage(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    full_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    create_contact_id = models.IntegerField()
    sort = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_page'


class ShopPageParams(models.Model):
    page_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_page_params'
        unique_together = (('page_id', 'name'),)


class ShopPlugin(models.Model):
    type = models.CharField(max_length=255)
    plugin = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.TextField()
    status = models.IntegerField()
    sort = models.IntegerField()
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_plugin'


class ShopPluginSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_plugin_settings'
        unique_together = (('id', 'name'),)


class ShopProduct(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    edit_datetime = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    type_id = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    image_filename = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    sku_id = models.IntegerField(blank=True, null=True)
    ext = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    compare_price = models.DecimalField(max_digits=15, decimal_places=4)
    currency = models.CharField(max_length=3, blank=True, null=True)
    min_price = models.DecimalField(max_digits=15, decimal_places=4)
    max_price = models.DecimalField(max_digits=15, decimal_places=4)
    tax_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    cross_selling = models.IntegerField(blank=True, null=True)
    upselling = models.IntegerField(blank=True, null=True)
    rating_count = models.IntegerField()
    total_sales = models.DecimalField(max_digits=15, decimal_places=4)
    category_id = models.IntegerField(blank=True, null=True)
    badge = models.TextField(blank=True, null=True)
    sku_type = models.IntegerField()
    base_price_selectable = models.DecimalField(max_digits=15, decimal_places=4)
    compare_price_selectable = models.DecimalField(max_digits=15, decimal_places=4)
    purchase_price_selectable = models.DecimalField(max_digits=15, decimal_places=4)
    sku_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product'


class ShopProductFeatures(models.Model):
    product_id = models.IntegerField()
    sku_id = models.IntegerField(blank=True, null=True)
    feature_id = models.IntegerField()
    feature_value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_features'
        unique_together = (('product_id', 'sku_id', 'feature_id', 'feature_value_id'),)


class ShopProductFeaturesSelectable(models.Model):
    product_id = models.IntegerField(primary_key=True)
    feature_id = models.IntegerField()
    value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_features_selectable'
        unique_together = (('product_id', 'feature_id', 'value_id'),)


class ShopProductImages(models.Model):
    product_id = models.IntegerField()
    upload_datetime = models.DateTimeField()
    edit_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    size = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=255)
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    ext = models.CharField(max_length=10, blank=True, null=True)
    badge_type = models.IntegerField(blank=True, null=True)
    badge_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product_images'


class ShopProductOg(models.Model):
    product_id = models.IntegerField(primary_key=True)
    property = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_product_og'
        unique_together = (('product_id', 'property'),)


class ShopProductPages(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    create_contact_id = models.IntegerField()
    sort = models.IntegerField()
    status = models.IntegerField()
    keywords = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product_pages'


class ShopProductParams(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'shop_product_params'
        unique_together = (('product_id', 'name'),)


class ShopProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=13)
    related_product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_related'
        unique_together = (('product_id', 'type', 'related_product_id'),)


class ShopProductReviews(models.Model):
    left_key = models.IntegerField(blank=True, null=True)
    right_key = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField()
    parent_id = models.IntegerField()
    product_id = models.IntegerField()
    review_id = models.IntegerField()
    datetime = models.DateTimeField()
    status = models.CharField(max_length=8)
    title = models.CharField(max_length=64, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    contact_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    auth_provider = models.CharField(max_length=100, blank=True, null=True)
    ip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product_reviews'


class ShopProductServices(models.Model):
    product_id = models.IntegerField()
    sku_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField()
    service_variant_id = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    primary_price = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_services'
        unique_together = (('product_id', 'sku_id', 'service_id', 'service_variant_id'),)


class ShopProductSkus(models.Model):
    product_id = models.IntegerField()
    sku = models.CharField(max_length=255)
    sort = models.IntegerField()
    name = models.CharField(max_length=255)
    image_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    primary_price = models.DecimalField(max_digits=15, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=4)
    compare_price = models.DecimalField(max_digits=15, decimal_places=4)
    count = models.IntegerField(blank=True, null=True)
    available = models.IntegerField()
    dimension_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_size = models.IntegerField()
    file_description = models.TextField(blank=True, null=True)
    virtual = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_skus'


class ShopProductStocks(models.Model):
    sku_id = models.IntegerField(primary_key=True)
    stock_id = models.IntegerField()
    product_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_stocks'
        unique_together = (('sku_id', 'stock_id'),)


class ShopProductStocksLog(models.Model):
    product_id = models.IntegerField()
    sku_id = models.IntegerField()
    stock_id = models.IntegerField(blank=True, null=True)
    stock_name = models.CharField(max_length=255, blank=True, null=True)
    before_count = models.IntegerField(blank=True, null=True)
    after_count = models.IntegerField(blank=True, null=True)
    diff_count = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()
    order_id = models.IntegerField(blank=True, null=True)
    transfer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product_stocks_log'


class ShopProductTags(models.Model):
    product_id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_product_tags'
        unique_together = (('product_id', 'tag_id'),)


class ShopPromo(models.Model):
    type = models.CharField(max_length=32)
    title = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=8, blank=True, null=True)
    background_color = models.CharField(max_length=8, blank=True, null=True)
    ext = models.CharField(max_length=6)
    enabled = models.IntegerField()
    countdown_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_promo'


class ShopPromoRoutes(models.Model):
    promo_id = models.PositiveIntegerField()
    storefront = models.CharField(primary_key=True, max_length=255)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_promo_routes'
        unique_together = (('storefront', 'promo_id'),)


class ShopPushClient(models.Model):
    contact_id = models.IntegerField()
    client_id = models.CharField(unique=True, max_length=64)
    shop_url = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    api_token = models.CharField(max_length=32, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_push_client'


class ShopSales(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    date = models.DateField()
    name = models.CharField(max_length=255)
    order_count = models.IntegerField()
    sales = models.FloatField()
    shipping = models.FloatField()
    tax = models.FloatField()
    purchase = models.FloatField()
    cost = models.FloatField()
    new_customer_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_sales'
        unique_together = (('hash', 'name', 'date'),)


class ShopSearchIndex(models.Model):
    word_id = models.IntegerField()
    product_id = models.IntegerField(primary_key=True)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_search_index'
        unique_together = (('product_id', 'word_id'),)


class ShopSearchWord(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_search_word'


class ShopService(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    currency = models.CharField(max_length=3, blank=True, null=True)
    variant_id = models.IntegerField()
    tax_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_service'


class ShopServiceVariants(models.Model):
    service_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    primary_price = models.DecimalField(max_digits=15, decimal_places=4)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_service_variants'


class ShopSet(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=255, blank=True, null=True)
    rule = models.CharField(max_length=32, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    count = models.IntegerField()
    sort = models.IntegerField()
    create_datetime = models.DateTimeField()
    edit_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_set'


class ShopSetProducts(models.Model):
    set_id = models.CharField(primary_key=True, max_length=64)
    product_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_set_products'
        unique_together = (('set_id', 'product_id'),)


class ShopStock(models.Model):
    low_count = models.IntegerField()
    critical_count = models.IntegerField()
    sort = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_stock'


class ShopStockRules(models.Model):
    sort = models.IntegerField()
    stock_id = models.IntegerField(blank=True, null=True)
    virtualstock_id = models.IntegerField(blank=True, null=True)
    rule_type = models.CharField(max_length=255)
    rule_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_stock_rules'


class ShopTag(models.Model):
    name = models.CharField(unique=True, max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_tag'


class ShopTax(models.Model):
    name = models.CharField(max_length=255)
    included = models.IntegerField()
    address_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'shop_tax'


class ShopTaxRegions(models.Model):
    tax_id = models.IntegerField()
    country_iso3 = models.CharField(max_length=3)
    region_code = models.CharField(max_length=8, blank=True, null=True)
    tax_value = models.DecimalField(max_digits=7, decimal_places=4)
    tax_name = models.CharField(max_length=255, blank=True, null=True)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_tax_regions'
        unique_together = (('tax_id', 'country_iso3', 'region_code'),)


class ShopTaxZipCodes(models.Model):
    tax_id = models.IntegerField(primary_key=True)
    zip_expr = models.CharField(max_length=16)
    tax_value = models.DecimalField(max_digits=7, decimal_places=4)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_tax_zip_codes'
        unique_together = (('tax_id', 'zip_expr'),)


class ShopTransfer(models.Model):
    string_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    finalize_datetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9)
    stock_id_from = models.IntegerField()
    stock_id_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_transfer'


class ShopTransferProducts(models.Model):
    product_id = models.IntegerField(primary_key=True)
    sku_id = models.IntegerField()
    transfer_id = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_transfer_products'
        unique_together = (('product_id', 'sku_id', 'transfer_id'),)


class ShopType(models.Model):
    sort = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    cross_selling = models.CharField(max_length=64)
    upselling = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_type'


class ShopTypeFeatures(models.Model):
    type_id = models.IntegerField(primary_key=True)
    feature_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_type_features'
        unique_together = (('type_id', 'feature_id'),)


class ShopTypeServices(models.Model):
    type_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_type_services'
        unique_together = (('type_id', 'service_id'),)


class ShopTypeUpselling(models.Model):
    type_id = models.IntegerField(primary_key=True)
    feature = models.CharField(max_length=32)
    feature_id = models.IntegerField(blank=True, null=True)
    cond = models.CharField(max_length=16)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_upselling'
        unique_together = (('type_id', 'feature'),)


class ShopVirtualstock(models.Model):
    low_count = models.IntegerField()
    critical_count = models.IntegerField()
    sort = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_virtualstock'


class ShopVirtualstockStocks(models.Model):
    virtualstock_id = models.IntegerField()
    stock_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_virtualstock_stocks'


class SiteBlock(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    content = models.TextField()
    create_datetime = models.DateTimeField()
    description = models.TextField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site_block'


class SiteDomain(models.Model):
    name = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=128)
    style = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'site_domain'


class SitePage(models.Model):
    domain_id = models.IntegerField()
    route = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    full_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    create_contact_id = models.IntegerField()
    sort = models.IntegerField()
    status = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_page'


class SitePageParams(models.Model):
    page_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'site_page_params'
        unique_together = (('page_id', 'name'),)


class TeamCalendarExternal(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    integration_level = models.CharField(max_length=12)
    name = models.CharField(max_length=255)
    contact_id = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    calendar_id = models.IntegerField(blank=True, null=True)
    native_calendar_id = models.TextField(blank=True, null=True)
    synchronize_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_calendar_external'


class TeamCalendarExternalParams(models.Model):
    calendar_external_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_calendar_external_params'
        unique_together = (('calendar_external_id', 'name'),)


class TeamEventExternal(models.Model):
    event_id = models.IntegerField()
    calendar_external_id = models.IntegerField()
    native_event_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team_event_external'
        unique_together = (('event_id', 'calendar_external_id'),)


class TeamEventExternalParams(models.Model):
    event_external_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_event_external_params'
        unique_together = (('event_external_id', 'name'),)


class TeamLocation(models.Model):
    group_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_location'


class WaAnnouncement(models.Model):
    app_id = models.CharField(max_length=32)
    text = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wa_announcement'


class WaApiAuthCodes(models.Model):
    code = models.CharField(primary_key=True, max_length=32)
    contact_id = models.IntegerField()
    client_id = models.CharField(max_length=32)
    scope = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wa_api_auth_codes'


class WaApiTokens(models.Model):
    contact_id = models.IntegerField()
    client_id = models.CharField(max_length=32)
    token = models.CharField(primary_key=True, max_length=32)
    scope = models.TextField()
    create_datetime = models.DateTimeField()
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_api_tokens'
        unique_together = (('contact_id', 'client_id'),)


class WaAppSettings(models.Model):
    app_id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wa_app_settings'
        unique_together = (('app_id', 'name'),)


class WaAppTokens(models.Model):
    contact_id = models.IntegerField(blank=True, null=True)
    app_id = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    create_datetime = models.DateTimeField()
    expire_datetime = models.DateTimeField(blank=True, null=True)
    token = models.CharField(unique=True, max_length=32)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_app_tokens'


class WaCache(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wa_cache'


class WaContact(models.Model):
    name = models.CharField(max_length=150)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=150)
    jobtitle = models.CharField(max_length=50)
    company_contact_id = models.IntegerField()
    is_company = models.IntegerField()
    is_user = models.IntegerField()
    login = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password = models.CharField(max_length=128)
    last_datetime = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birth_day = models.PositiveIntegerField(blank=True, null=True)
    birth_month = models.PositiveIntegerField(blank=True, null=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    photo = models.PositiveIntegerField()
    create_datetime = models.DateTimeField()
    create_app_id = models.CharField(max_length=32)
    create_method = models.CharField(max_length=32)
    create_contact_id = models.IntegerField()
    locale = models.CharField(max_length=8)
    timezone = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'wa_contact'


class WaContactCalendars(models.Model):
    name = models.CharField(max_length=255)
    bg_color = models.CharField(max_length=7, blank=True, null=True)
    font_color = models.CharField(max_length=7, blank=True, null=True)
    sort = models.IntegerField()
    is_limited = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_calendars'


class WaContactCategories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    contact_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_categories'
        unique_together = (('category_id', 'contact_id'),)


class WaContactCategory(models.Model):
    name = models.CharField(max_length=255)
    system_id = models.CharField(unique=True, max_length=64, blank=True, null=True)
    app_id = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_category'


class WaContactData(models.Model):
    contact_id = models.IntegerField()
    field = models.CharField(max_length=32)
    ext = models.CharField(max_length=32)
    value = models.CharField(max_length=255)
    sort = models.IntegerField()
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_contact_data'
        unique_together = (('contact_id', 'field', 'sort'),)


class WaContactDataText(models.Model):
    contact_id = models.IntegerField()
    field = models.CharField(max_length=32)
    ext = models.CharField(max_length=32)
    value = models.TextField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_data_text'
        unique_together = (('contact_id', 'field', 'sort'),)


class WaContactEmails(models.Model):
    contact_id = models.IntegerField()
    email = models.CharField(max_length=255)
    ext = models.CharField(max_length=32)
    sort = models.IntegerField()
    status = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'wa_contact_emails'
        unique_together = (('contact_id', 'sort'),)


class WaContactEvents(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    contact_id = models.IntegerField()
    calendar_id = models.IntegerField()
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_allday = models.IntegerField()
    is_status = models.IntegerField()
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_events'


class WaContactFieldValues(models.Model):
    parent_field = models.CharField(max_length=64)
    parent_value = models.CharField(max_length=255)
    field = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_field_values'


class WaContactRights(models.Model):
    group_id = models.IntegerField(primary_key=True)
    app_id = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_contact_rights'
        unique_together = (('group_id', 'app_id', 'name'),)


class WaContactSettings(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    app_id = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wa_contact_settings'
        unique_together = (('contact_id', 'app_id', 'name'),)


class WaCountry(models.Model):
    name = models.CharField(max_length=255)
    iso3letter = models.CharField(primary_key=True, max_length=3)
    iso2letter = models.CharField(unique=True, max_length=2)
    isonumeric = models.CharField(unique=True, max_length=3)
    fav_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_country'


class WaDashboard(models.Model):
    name = models.CharField(max_length=255)
    hash = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'wa_dashboard'


class WaGroup(models.Model):
    name = models.CharField(max_length=255)
    cnt = models.IntegerField()
    icon = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=8)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_group'


class WaLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_id = models.CharField(max_length=32)
    contact_id = models.IntegerField()
    datetime = models.DateTimeField()
    action = models.CharField(max_length=255)
    subject_contact_id = models.IntegerField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_log'


class WaLoginLog(models.Model):
    contact_id = models.IntegerField()
    datetime_in = models.DateTimeField()
    datetime_out = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_login_log'


class WaRegion(models.Model):
    country_iso3 = models.CharField(primary_key=True, max_length=3)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    fav_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_region'
        unique_together = (('country_iso3', 'code'),)


class WaTransaction(models.Model):
    plugin = models.CharField(max_length=50)
    app_id = models.CharField(max_length=50)
    merchant_id = models.CharField(max_length=50, blank=True, null=True)
    native_id = models.CharField(max_length=255)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()
    type = models.CharField(max_length=20)
    parent_id = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=20)
    error = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    view_data = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency_id = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_transaction'


class WaTransactionData(models.Model):
    transaction_id = models.IntegerField()
    field_id = models.CharField(max_length=50)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_transaction_data'


class WaUserGroups(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_user_groups'
        unique_together = (('contact_id', 'group_id'),)


class WaVerificationChannel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    create_datetime = models.DateTimeField(blank=True, null=True)
    system = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wa_verification_channel'


class WaVerificationChannelAssets(models.Model):
    channel_id = models.IntegerField()
    address = models.CharField(max_length=64)
    contact_id = models.IntegerField()
    name = models.CharField(max_length=64)
    value = models.TextField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_verification_channel_assets'
        unique_together = (('channel_id', 'address', 'contact_id', 'name'),)


class WaVerificationChannelParams(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_verification_channel_params'
        unique_together = (('channel_id', 'name'),)


class WaWidget(models.Model):
    widget = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    contact_id = models.IntegerField()
    dashboard_id = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField()
    app_id = models.CharField(max_length=32)
    block = models.IntegerField()
    sort = models.IntegerField()
    size = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wa_widget'


class WaWidgetParams(models.Model):
    widget_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wa_widget_params'
        unique_together = (('widget_id', 'name'),)
