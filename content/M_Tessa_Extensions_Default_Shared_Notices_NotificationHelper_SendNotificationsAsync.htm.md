# NotificationHelper.SendNotificationsAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task SendNotificationsAsync(
    	IDictionary<string, Object> info,
    	Guid cardID,
    	Guid cardTypeID,
    	string cardDigest,
    	IValidationResultBuilder validationResult,
    	INotificationResolver notificationResolver,
    	bool withoutTransaction = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function SendNotificationsAsync ( 
    	info As IDictionary(Of String, Object),
    	cardID As Guid,
    	cardTypeID As Guid,
    	cardDigest As String,
    	validationResult As IValidationResultBuilder,
    	notificationResolver As INotificationResolver,
    	Optional withoutTransaction As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ SendNotificationsAsync(
    	IDictionary<String^, Object^>^ info, 
    	Guid cardID, 
    	Guid cardTypeID, 
    	String^ cardDigest, 
    	IValidationResultBuilder^ validationResult, 
    	INotificationResolver^ notificationResolver, 
    	bool withoutTransaction = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member SendNotificationsAsync : 
            info : IDictionary<string, Object> * 
            cardID : Guid * 
            cardTypeID : Guid * 
            cardDigest : string * 
            validationResult : IValidationResultBuilder * 
            notificationResolver : INotificationResolver * 
            ?withoutTransaction : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _withoutTransaction = defaultArg withoutTransaction false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardDigest [String](https://learn.microsoft.com/dotnet/api/system.string)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
notificationResolver
[INotificationResolver](T_Tessa_Extensions_Default_Shared_Notices_INotificationResolver.htm)
withoutTransaction
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[NotificationHelper -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationHelper.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
