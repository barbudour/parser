# ILdapUnitProvider.SyncManualAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SyncManualAsync(
    	IAdSyncContext context,
    	RoleType type,
    	Guid cardId,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SyncManualAsync ( 
    	context As IAdSyncContext,
    	type As RoleType,
    	cardId As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SyncManualAsync(
    	IAdSyncContext^ context, 
    	RoleType type, 
    	Guid cardId, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SyncManualAsync : 
            context : IAdSyncContext * 
            type : RoleType * 
            cardId : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
type [RoleType](T_Tessa_Roles_RoleType.htm)
cardId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
