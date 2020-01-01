from django.urls import path

from .views import PublishingCompanyCreate, PublishingCompanyList, PublishingCompanyDetail, PublishingCompanyUpdate, PublishingCompanyDelete

urlpatterns = [
    path('criacao/', PublishingCompanyCreate.as_view(), name='publishing-company-create'),
    path('lista/', PublishingCompanyList.as_view(), name='publishing-company-list'),
    path('detalhes/<int:pk>/', PublishingCompanyDetail.as_view(), name='publishing-company-detail'),
    path('atualizacao/<int:pk>/', PublishingCompanyUpdate.as_view(), name='publishing-company-update'),
    path('delecao/<int:pk>/', PublishingCompanyDelete.as_view(), name='publishing-company-delete'),
]