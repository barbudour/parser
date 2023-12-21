# FakeWorkplaceService.GetByNameAsync - метод
Возвращает рабочее место по имени.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IWorkplaceMetadata> GetByNameAsync(
    	string alias,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetByNameAsync ( 
    	alias As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IWorkplaceMetadata)
C++ __Копировать
     public:
    virtual ValueTask<IWorkplaceMetadata^> GetByNameAsync(
    	String^ alias, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetByNameAsync : 
            alias : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IWorkplaceMetadata> 
    override GetByNameAsync : 
            alias : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IWorkplaceMetadata> 
#### Параметры
alias [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя рабочего места. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IWorkplaceMetadata](T_Tessa_Views_Workplaces_IWorkplaceMetadata.htm)>  
The [WorkplaceMetadata](T_Tessa_Views_Workplaces_WorkplaceMetadata.htm).
#### Реализации
[IWorkplaceService.GetByNameAsync(String,
CancellationToken)](M_Tessa_Views_Workplaces_IWorkplaceService_GetByNameAsync.htm)  
##  __См. также
#### Ссылки
[FakeWorkplaceService - ](T_Tessa_Applications_FakeWorkplaceService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
