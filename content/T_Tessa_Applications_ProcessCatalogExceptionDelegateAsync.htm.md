# ProcessCatalogExceptionDelegateAsync - делегат
Делегат обработки исключения возникшего при загрузке приложений из каталога
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task ProcessCatalogExceptionDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog catalog,
    	[NotNullAttribute] Exception e
    )
VB __Копировать
     Public Delegate Function ProcessCatalogExceptionDelegateAsync ( 
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	<NotNullAttribute> e As Exception
    ) As Task
C++ __Копировать
     public delegate Task^ ProcessCatalogExceptionDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	[NotNullAttribute] Exception^ e
    )
F# __Копировать
     type ProcessCatalogExceptionDelegateAsync = 
        delegate of 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            [<NotNullAttribute>] e : Exception -> Task
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
    Каталог приложений
e [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    Исключение
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
