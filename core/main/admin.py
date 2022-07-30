from django.contrib import admin
from .models import News, HomeCarusel, HomeCategory, HomeSubCategory, HomeFeatureItem, HomeBrand, HomeRec, HomeBlog, HeadBlog, HeadFooter, Circle, Map, BlogSingle, BlogDavis, BlogJanis, HomeContact, ShippingBlog, ErrorBlog, ShopperLogo, HomeCart
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass

class HomeCaruselAdmin(TranslationAdmin):
    pass

class HomeCategoryAdmin(TranslationAdmin):
    pass

class HomeSubCategoryAdmin(TranslationAdmin):
    pass

class HomeBrandAdmin(TranslationAdmin):
    pass

class HomeFeatureItemAdmin(TranslationAdmin):
    pass

class HomeRecAdmin(TranslationAdmin):
    pass

class HomeBlogAdmin(TranslationAdmin):
    pass

class HeadBlogAdmin(TranslationAdmin):
    pass

class HeadFooterAdmin(TranslationAdmin):
    pass

class CircleAdmin(TranslationAdmin):
    pass

class MapAdmin(TranslationAdmin):
    pass

class BlogSingleAdmin(TranslationAdmin):
    pass

class BlogDavisAdmin(TranslationAdmin):
    pass

class BlogJanisAdmin(TranslationAdmin):
    pass

class HomeContactAdmin(TranslationAdmin):
    pass

class ShippingBlogAdmin(TranslationAdmin):
    pass

class ErrorBlogAdmin(TranslationAdmin):
    pass

class ShopperLogoAdmin(TranslationAdmin):
    pass

class HomeCartAdmin(TranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)
admin.site.register(HomeCarusel, HomeCaruselAdmin)
admin.site.register(HomeCategory, HomeCategoryAdmin)
admin.site.register(HomeSubCategory, HomeSubCategoryAdmin)
admin.site.register(HomeBrand, HomeBrandAdmin)
admin.site.register(HomeFeatureItem, HomeFeatureItemAdmin)
admin.site.register(HomeRec, HomeRecAdmin)
admin.site.register(HomeBlog, HomeBlogAdmin)
admin.site.register(HeadBlog, HeadBlogAdmin)
admin.site.register(HeadFooter, HeadFooterAdmin)
admin.site.register(Circle, CircleAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(BlogSingle, BlogSingleAdmin)
admin.site.register(BlogDavis, BlogDavisAdmin)
admin.site.register(BlogJanis, BlogJanisAdmin)
admin.site.register(HomeContact, HomeContactAdmin)
admin.site.register(ShippingBlog, ShippingBlogAdmin)
admin.site.register(ErrorBlog, ErrorBlogAdmin)
admin.site.register(ShopperLogo, ShopperLogoAdmin)
admin.site.register(HomeCart, HomeCartAdmin)