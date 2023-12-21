# CatalogApplicationsQuery.GetApplicationsAsync - метод
Возвращает список приложений доступных в каталоге приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IReadOnlyList<IApplicationModel>> GetApplicationsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetApplicationsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IReadOnlyList(Of IApplicationModel))
C++ __Копировать
     public:
    Task<IReadOnlyList<IApplicationModel^>^>^ GetApplicationsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetApplicationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyList<IApplicationModel>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)>>  
Список приложений
## __См. также
#### Ссылки
[CatalogApplicationsQuery -
](T_Tessa_Applications_CatalogApplicationsQuery.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
