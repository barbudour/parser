# AdExtensionContext - конструктор
Инициализирует новый экземпляр класса
[AdExtensionContext](T_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AdExtensionContext(
    	IAdSyncContext syncContext,
    	AdConnection connection,
    	AdEntry entry,
    	Card card,
    	bool updateUser = false,
    	List<AdEntry> users = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	syncContext As IAdSyncContext,
    	connection As AdConnection,
    	entry As AdEntry,
    	card As Card,
    	Optional updateUser As Boolean = false,
    	Optional users As List(Of AdEntry) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    AdExtensionContext(
    	IAdSyncContext^ syncContext, 
    	AdConnection^ connection, 
    	AdEntry^ entry, 
    	Card^ card, 
    	bool updateUser = false, 
    	List<AdEntry^>^ users = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            syncContext : IAdSyncContext * 
            connection : AdConnection * 
            entry : AdEntry * 
            card : Card * 
            ?updateUser : bool * 
            ?users : List<AdEntry> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _updateUser = defaultArg updateUser false
            let _users = defaultArg users null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> AdExtensionContext
#### Параметры
syncContext
[IAdSyncContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
connection
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
entry [AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)
card [Card](T_Tessa_Cards_Card.htm)
updateUser [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
users
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
## __См. также
#### Ссылки
[AdExtensionContext -
](T_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
