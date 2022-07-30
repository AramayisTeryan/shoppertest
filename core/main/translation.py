from .models import News, HomeCarusel, HomeCategory, HomeSubCategory, HomeBrand, HomeFeatureItem, HomeRec, HomeBlog, HeadBlog, HeadFooter, Circle, Map, BlogSingle, BlogDavis, BlogJanis, HomeContact, ShippingBlog, ErrorBlog, HomeCart, ShopperLogo
from modeltranslation.translator import register, TranslationOptions

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(HomeCarusel)
class HomeCaruselTranslationOptions(TranslationOptions):
    fields = ('name1', 'name2', 'about',)

@register(HomeCategory)
class HomeCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(HomeSubCategory)
class HomeSubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(HomeBrand)
class HomeBrandTranslationsOptions(TranslationOptions):
    fields = ('name',)

@register(HomeFeatureItem)
class HomeFeatureItemTranslationOptions(TranslationOptions):
    fields = ('about',)

@register(HomeRec)
class HomeRecTranslationOptions(TranslationOptions):
    fields =('about',)

@register(HomeBlog)
class HomeBlogTranslationOptions(TranslationOptions):
    fields = ('name2', 'about1', 'about2',)

@register(HeadBlog)
class HeadBlogTranslationOptions(TranslationOptions):
    fields = ('name1',)

@register(HeadFooter)
class HeadFooterTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)

@register(Circle)
class CirleTranslationoptions(TranslationOptions):
    fields = ('name', 'about',)

@register(Map)
class MapTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(BlogSingle)
class BlogSingleTranslationOptions(TranslationOptions):
    fields = ('name1', 'name2', 'about1', 'about2',)

@register(BlogDavis)
class BlogDavisTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)

@register(BlogJanis)
class BlogJanisTranslationoptions(TranslationOptions):
    fields = ('about',)

@register(HomeContact)
class HomeContactTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ShippingBlog)
class ShippingBlogTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ErrorBlog)
class ErrorBlogTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)

@register(HomeCart)
class HomeCartTranslationOptions(TranslationOptions):
    fields = ('name1', 'name2', 'about1', 'about2',)

@register(ShopperLogo)
class ShopperLogoTranslationOptions(TranslationOptions):
    fields = ('img',)