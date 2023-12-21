# ILdapUnitProvider.SyncUnmatchedDistinguishedNameAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SyncUnmatchedDistinguishedNameAsync(
    	IAdSyncContext context,
    	AdConnection conn,
    	RoleType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SyncUnmatchedDistinguishedNameAsync ( 
    	context As IAdSyncContext,
    	conn As AdConnection,
    	type As RoleType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SyncUnmatchedDistinguishedNameAsync(
    	IAdSyncContext^ context, 
    	AdConnection^ conn, 
    	RoleType type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SyncUnmatchedDistinguishedNameAsync : 
            context : IAdSyncContext * 
            conn : AdConnection * 
            type : RoleType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
type [RoleType](T_Tessa_Roles_RoleType.htm)
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
