# WfHelper.TryGetSatelliteIDAsync - метод
Возвращает идентификатор карточки-сателлита для резолюций Workflow по
идентификатору основной карточки или null, если карточка-сателлит отсутствует.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> TryGetSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ TryGetSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetSatelliteIDAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор основной карточки, для которой требуется получить идентификатор сателлита. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор карточки-сателлита для резолюций Workflow или null, если
карточка-сателлит отсутствует.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
