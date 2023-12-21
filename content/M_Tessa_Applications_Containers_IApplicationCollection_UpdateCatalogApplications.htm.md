# IApplicationCollection.UpdateCatalogApplications - метод
Вызывает обновление списка приложений для каталога приложений catalog
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void UpdateCatalogApplications(
    	[NotNullAttribute] IApplicationCatalog catalog,
    	[NotNullAttribute] IEnumerable<IApplicationModel> applications
    )
VB __Копировать
     Sub UpdateCatalogApplications ( 
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	<NotNullAttribute> applications As IEnumerable(Of IApplicationModel)
    )
C++ __Копировать
     void UpdateCatalogApplications(
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	[NotNullAttribute] IEnumerable<IApplicationModel^>^ applications
    )
F# __Копировать
     abstract UpdateCatalogApplications : 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            [<NotNullAttribute>] applications : IEnumerable<IApplicationModel> -> unit 
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
    Каталог приложений
applications
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)>
    Список приложений
##  __См. также
#### Ссылки
[IApplicationCollection -
](T_Tessa_Applications_Containers_IApplicationCollection.htm)
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
