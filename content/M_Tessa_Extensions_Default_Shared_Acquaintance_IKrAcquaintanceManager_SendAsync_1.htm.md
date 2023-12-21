# IKrAcquaintanceManager.SendAsync(Guid, IReadOnlyList<String>, Boolean,
String, String, Dictionary<String, Object>, Nullable<Guid>, Nullable<Guid>,
Boolean, CancellationToken) - метод
Производит отправку массового ознакомления карточки
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Acquaintance](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ValidationResult> SendAsync(
    	Guid mainCardID,
    	IReadOnlyList<string> roleNameList,
    	bool excludeDeputies = false,
    	string comment = null,
    	string placeholderAliases = null,
    	Dictionary<string, Object> info = null,
    	Guid? notificationCardID = null,
    	Guid? senderID = null,
    	bool addSuccessMessage = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SendAsync ( 
    	mainCardID As Guid,
    	roleNameList As IReadOnlyList(Of String),
    	Optional excludeDeputies As Boolean = false,
    	Optional comment As String = Nothing,
    	Optional placeholderAliases As String = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional notificationCardID As Guid? = Nothing,
    	Optional senderID As Guid? = Nothing,
    	Optional addSuccessMessage As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
    Task<ValidationResult^>^ SendAsync(
    	Guid mainCardID, 
    	IReadOnlyList<String^>^ roleNameList, 
    	bool excludeDeputies = false, 
    	String^ comment = nullptr, 
    	String^ placeholderAliases = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	Nullable<Guid> notificationCardID = nullptr, 
    	Nullable<Guid> senderID = nullptr, 
    	bool addSuccessMessage = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SendAsync : 
            mainCardID : Guid * 
            roleNameList : IReadOnlyList<string> * 
            ?excludeDeputies : bool * 
            ?comment : string * 
            ?placeholderAliases : string * 
            ?info : Dictionary<string, Object> * 
            ?notificationCardID : Nullable<Guid> * 
            ?senderID : Nullable<Guid> * 
            ?addSuccessMessage : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _excludeDeputies = defaultArg excludeDeputies false
            let _comment = defaultArg comment null
            let _placeholderAliases = defaultArg placeholderAliases null
            let _info = defaultArg info null
            let _notificationCardID = defaultArg notificationCardID null
            let _senderID = defaultArg senderID null
            let _addSuccessMessage = defaultArg addSuccessMessage false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    ID карточки
roleNameList
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
    Список имен ролей для ознакомления
excludeDeputies
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Определяет, нужно ли отправлять ознакомление на заместителей
comment [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Комментарий
placeholderAliases
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Алиасы плейсхолдеров
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Дополнительная информация, которая передается в info методов замены плейсхолдеров
notificationCardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Карточка уведомления, которая используется для отправки ознакомления. По умолчанию используется [AcquaintanceID](F_Tessa_Extensions_Default_Shared_DefaultNotifications_AcquaintanceID.htm). Данный параметр не передается с клиента на сервер и его использование допускается только на серверной стороне. 
senderID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Сотрудник, от имени которого производится отправка ознакомления. Если не задан или некорректен, отправка производится от текущего сотрудника. Данный параметр не передается с клиента на сервер и его использование допускается только на серверной стороне. 
addSuccessMessage
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что при успешной отправке на ознакомление требуется вывести информационное сообщение в ValidationResult о количестве сотрудников, которым было направлено ознакомление. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Возвращает результат валидации отправки массового ознакомления
##  __См. также
#### Ссылки
[IKrAcquaintanceManager -
](T_Tessa_Extensions_Default_Shared_Acquaintance_IKrAcquaintanceManager.htm)
[SendAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Acquaintance_IKrAcquaintanceManager_SendAsync.htm)
[Tessa.Extensions.Default.Shared.Acquaintance - пространство
имён](N_Tessa_Extensions_Default_Shared_Acquaintance.htm)
