# ILdapUnitProvider.CreateOrUpdateUserAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CreateOrUpdateUserAsync(
    	IAdSyncContext syncContext,
    	AdConnection conn,
    	AdEntry user,
    	bool updateUser = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateOrUpdateUserAsync ( 
    	syncContext As IAdSyncContext,
    	conn As AdConnection,
    	user As AdEntry,
    	Optional updateUser As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CreateOrUpdateUserAsync(
    	IAdSyncContext^ syncContext, 
    	AdConnection^ conn, 
    	AdEntry^ user, 
    	bool updateUser = true, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateOrUpdateUserAsync : 
            syncContext : IAdSyncContext * 
            conn : AdConnection * 
            user : AdEntry * 
            ?updateUser : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _updateUser = defaultArg updateUser true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
syncContext
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
user [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
updateUser [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
