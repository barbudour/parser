# ILdapUnitProvider.SyncStaticRoleAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SyncStaticRoleAsync(
    	IAdSyncContext context,
    	AdConnection conn,
    	Guid objectId,
    	bool syncUsers = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SyncStaticRoleAsync ( 
    	context As IAdSyncContext,
    	conn As AdConnection,
    	objectId As Guid,
    	Optional syncUsers As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SyncStaticRoleAsync(
    	IAdSyncContext^ context, 
    	AdConnection^ conn, 
    	Guid objectId, 
    	bool syncUsers = true, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SyncStaticRoleAsync : 
            context : IAdSyncContext * 
            conn : AdConnection * 
            objectId : Guid * 
            ?syncUsers : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _syncUsers = defaultArg syncUsers true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
objectId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
syncUsers [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
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
