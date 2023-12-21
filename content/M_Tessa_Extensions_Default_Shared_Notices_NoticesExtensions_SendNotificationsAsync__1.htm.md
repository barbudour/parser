# NoticesExtensions.SendNotificationsAsync<T> \- метод
Выполняет отправку почтовых уведомлений
[INotification](T_Tessa_Extensions_Default_Shared_Notices_INotification.htm)
без привязки к процессу создания или сохранения карточки. Возвращает результат
валидации по отправке уведомлений, который не равен null.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<ValidationResult> SendNotificationsAsync<T>(
    	this INotificationResolver notificationResolver,
    	Guid cardID,
    	Guid cardTypeID,
    	string cardDigest = null,
    	IDictionary<string, Object> info = null,
    	bool withoutTransaction = false,
    	CancellationToken cancellationToken = default,
    	params T[] notifications
    )
    where T : INotification
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SendNotificationsAsync(Of T As INotification) ( 
    	notificationResolver As INotificationResolver,
    	cardID As Guid,
    	cardTypeID As Guid,
    	Optional cardDigest As String = Nothing,
    	Optional info As IDictionary(Of String, Object) = Nothing,
    	Optional withoutTransaction As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing,
    	ParamArray notifications As T()
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : INotification
    static Task<ValidationResult^>^ SendNotificationsAsync(
    	INotificationResolver^ notificationResolver, 
    	Guid cardID, 
    	Guid cardTypeID, 
    	String^ cardDigest = nullptr, 
    	IDictionary<String^, Object^>^ info = nullptr, 
    	bool withoutTransaction = false, 
    	CancellationToken cancellationToken = CancellationToken(), 
    	... array<T>^ notifications
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SendNotificationsAsync : 
            notificationResolver : INotificationResolver * 
            cardID : Guid * 
            cardTypeID : Guid * 
            ?cardDigest : string * 
            ?info : IDictionary<string, Object> * 
            ?withoutTransaction : bool * 
            ?cancellationToken : CancellationToken * 
            notifications : 'T[] 
    (* Defaults:
            let _cardDigest = defaultArg cardDigest null
            let _info = defaultArg info null
            let _withoutTransaction = defaultArg withoutTransaction false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult>  when 'T : INotification
#### Параметры
notificationResolver
[INotificationResolver](T_Tessa_Extensions_Default_Shared_Notices_INotificationResolver.htm)
    Объект, выполняющий получение обработчиков сообщений с последующей отправкой.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cardDigest [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Digest карточки или null, если digest будет неизвестен в уведомлении. Необходимость наличия Digest определяется кодом [INotificationSender](T_Tessa_Extensions_Default_Shared_Notices_INotificationSender.htm). 
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, используемая объектами [INotificationSender](T_Tessa_Extensions_Default_Shared_Notices_INotificationSender.htm) при отправке писем, или null, если дополнительная информация не передаётся. 
withoutTransaction
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что отправка письма выполняется без транзакции. Актуально при использовании на сервере. Укажите true, если известно, что метод выполняется для уже открытой транзакции SQL. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
notifications T[]
    Отправляемые уведомления.
#### Параметры типа
T
    Тип уведомления, реализующий интерфейс [INotification](T_Tessa_Extensions_Default_Shared_Notices_INotification.htm).
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат валидации по отправке уведомлений. Не равен null и может содержать
ошибки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[INotificationResolver](T_Tessa_Extensions_Default_Shared_Notices_INotificationResolver.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NoticesExtensions -
](T_Tessa_Extensions_Default_Shared_Notices_NoticesExtensions.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
