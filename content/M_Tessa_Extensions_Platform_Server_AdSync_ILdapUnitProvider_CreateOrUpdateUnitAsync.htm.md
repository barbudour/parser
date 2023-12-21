# ILdapUnitProvider.CreateOrUpdateUnitAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CreateOrUpdateUnitAsync(
    	IAdSyncContext syncContext,
    	AdConnection conn,
    	AdEntry unit,
    	Guid? parentObjectGuid,
    	string parentObjectName,
    	bool updateUser,
    	List<AdEntry> users = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateOrUpdateUnitAsync ( 
    	syncContext As IAdSyncContext,
    	conn As AdConnection,
    	unit As AdEntry,
    	parentObjectGuid As Guid?,
    	parentObjectName As String,
    	updateUser As Boolean,
    	Optional users As List(Of AdEntry) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CreateOrUpdateUnitAsync(
    	IAdSyncContext^ syncContext, 
    	AdConnection^ conn, 
    	AdEntry^ unit, 
    	Nullable<Guid> parentObjectGuid, 
    	String^ parentObjectName, 
    	bool updateUser, 
    	List<AdEntry^>^ users = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateOrUpdateUnitAsync : 
            syncContext : IAdSyncContext * 
            conn : AdConnection * 
            unit : AdEntry * 
            parentObjectGuid : Nullable<Guid> * 
            parentObjectName : string * 
            updateUser : bool * 
            ?users : List<AdEntry> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _users = defaultArg users null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
syncContext
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
unit [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
parentObjectGuid
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
parentObjectName
[String](https://learn.microsoft.com/dotnet/api/system.string)
updateUser [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
users
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)>
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
