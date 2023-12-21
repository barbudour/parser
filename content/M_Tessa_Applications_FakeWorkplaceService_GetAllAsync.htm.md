# FakeWorkplaceService.GetAllAsync - метод
Возвращает список доступных рабочих мест.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IEnumerable<IWorkplaceMetadata>> GetAllAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAllAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of IWorkplaceMetadata))
C++ __Копировать
     public:
    virtual ValueTask<IEnumerable<IWorkplaceMetadata^>^> GetAllAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAllAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<IWorkplaceMetadata>> 
    override GetAllAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<IWorkplaceMetadata>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IWorkplaceMetadata](T_Tessa_Views_Workplaces_IWorkplaceMetadata.htm)>>  
Асинхронная задача.
#### Реализации
[IWorkplaceService.GetAllAsync(CancellationToken)](M_Tessa_Views_Workplaces_IWorkplaceService_GetAllAsync.htm)  
##  __См. также
#### Ссылки
[FakeWorkplaceService - ](T_Tessa_Applications_FakeWorkplaceService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
