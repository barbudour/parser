# ClientTessaViewModelRepositoryImplementer.GetAsync - метод
Возвращает элементы из хранилища
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IEnumerable<TessaViewModel>> GetAsync(
    	IGetModelRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync ( 
    	request As IGetModelRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IEnumerable(Of TessaViewModel))
C++ __Копировать
     public:
    virtual Task<IEnumerable<TessaViewModel^>^>^ GetAsync(
    	IGetModelRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            request : IGetModelRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IEnumerable<TessaViewModel>> 
    override GetAsync : 
            request : IGetModelRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IEnumerable<TessaViewModel>> 
#### Параметры
request [IGetModelRequest](T_Tessa_Views_IGetModelRequest.htm)
     Параметры запроса 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[TessaViewModel](T_Tessa_Views_TessaViewModel.htm)>>  
Результат выполнения запроса
#### Реализации
[IRepository<TGetRequest, TChangeRequest, TResponse>.GetAsync(TGetRequest,
CancellationToken)](M_Tessa_Views_IRepository_3_GetAsync.htm)  
##  __См. также
#### Ссылки
[ClientTessaViewModelRepositoryImplementer -
](T_Tessa_Applications_ClientTessaViewModelRepositoryImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
