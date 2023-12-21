# CatalogApplicationsQuery - конструктор
Initializes a new instance of the
[CatalogApplicationsQuery](T_Tessa_Applications_CatalogApplicationsQuery.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CatalogApplicationsQuery(
    	[NotNullAttribute] GetCatalogContainerDelegateAsync getCatalogContainerFuncAsync,
    	[NotNullAttribute] IApplicationCatalog catalog,
    	[NotNullAttribute] ProcessCatalogExceptionDelegateAsync processExceptionAsync
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> getCatalogContainerFuncAsync As GetCatalogContainerDelegateAsync,
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	<NotNullAttribute> processExceptionAsync As ProcessCatalogExceptionDelegateAsync
    )
C++ __Копировать
     public:
    CatalogApplicationsQuery(
    	[NotNullAttribute] GetCatalogContainerDelegateAsync^ getCatalogContainerFuncAsync, 
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	[NotNullAttribute] ProcessCatalogExceptionDelegateAsync^ processExceptionAsync
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] getCatalogContainerFuncAsync : GetCatalogContainerDelegateAsync * 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            [<NotNullAttribute>] processExceptionAsync : ProcessCatalogExceptionDelegateAsync -> CatalogApplicationsQuery
#### Параметры
getCatalogContainerFuncAsync
[GetCatalogContainerDelegateAsync](T_Tessa_Applications_GetCatalogContainerDelegateAsync.htm)
     Функция получения контейнера получения зависимостей 
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Каталог приложений 
processExceptionAsync
[ProcessCatalogExceptionDelegateAsync](T_Tessa_Applications_ProcessCatalogExceptionDelegateAsync.htm)
     The process Exception. 
## __Исключения
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)|  A
delegate callback throws an exception.  
---|---  
## __См. также
#### Ссылки
[CatalogApplicationsQuery -
](T_Tessa_Applications_CatalogApplicationsQuery.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
