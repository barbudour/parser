# ClientTessaViewModelRepositoryImplementer.NewAsync - метод
Осуществляет создание новоых элементов в хранилище
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task NewAsync(
    	IStoreTessaViewRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NewAsync ( 
    	request As IStoreTessaViewRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ NewAsync(
    	IStoreTessaViewRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract NewAsync : 
            request : IStoreTessaViewRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override NewAsync : 
            request : IStoreTessaViewRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
request [IStoreTessaViewRequest](T_Tessa_Views_IStoreTessaViewRequest.htm)
     Параметры запроса 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IRepository<TGetRequest, TChangeRequest, TResponse>.NewAsync(TChangeRequest,
CancellationToken)](M_Tessa_Views_IRepository_3_NewAsync.htm)  
##  __См. также
#### Ссылки
[ClientTessaViewModelRepositoryImplementer -
](T_Tessa_Applications_ClientTessaViewModelRepositoryImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
