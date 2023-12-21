# GetCatalogApplicationsDelegateAsync - делегат
Делегат получения списка моделей приложений, содержащихся в каталоге catalog.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<IReadOnlyList<IApplicationModel>> GetCatalogApplicationsDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog catalog,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function GetCatalogApplicationsDelegateAsync ( 
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IReadOnlyList(Of IApplicationModel))
C++ __Копировать
     public delegate Task<IReadOnlyList<IApplicationModel^>^>^ GetCatalogApplicationsDelegateAsync(
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type GetCatalogApplicationsDelegateAsync = 
        delegate of 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyList<IApplicationModel>>
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
    Каталог приложений.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)>>  
Список приложений.
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
