# ILdapUnitProvider.CreateOrUpdateRoleAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CreateOrUpdateRoleAsync(
    	IAdSyncContext syncContext,
    	AdConnection conn,
    	AdEntry role,
    	Guid? parentObjectGuid,
    	string parentObjectName,
    	bool updateUser,
    	Func<Task<List<Guid>>> getUsersFunc = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateOrUpdateRoleAsync ( 
    	syncContext As IAdSyncContext,
    	conn As AdConnection,
    	role As AdEntry,
    	parentObjectGuid As Guid?,
    	parentObjectName As String,
    	updateUser As Boolean,
    	Optional getUsersFunc As Func(Of Task(Of List(Of Guid))) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CreateOrUpdateRoleAsync(
    	IAdSyncContext^ syncContext, 
    	AdConnection^ conn, 
    	AdEntry^ role, 
    	Nullable<Guid> parentObjectGuid, 
    	String^ parentObjectName, 
    	bool updateUser, 
    	Func<Task<List<Guid>^>^>^ getUsersFunc = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateOrUpdateRoleAsync : 
            syncContext : IAdSyncContext * 
            conn : AdConnection * 
            role : AdEntry * 
            parentObjectGuid : Nullable<Guid> * 
            parentObjectName : string * 
            updateUser : bool * 
            ?getUsersFunc : Func<Task<List<Guid>>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _getUsersFunc = defaultArg getUsersFunc null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
syncContext
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
role [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
parentObjectGuid
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
parentObjectName
[String](https://learn.microsoft.com/dotnet/api/system.string)
updateUser [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
getUsersFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>>
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
