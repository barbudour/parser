# NotificationResolver.CreateContextAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<INotificationContext> CreateContextAsync(
    	Guid cardID,
    	Guid cardTypeID,
    	string cardDigest,
    	IValidationResultBuilder validationResult,
    	bool withoutTransaction,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateContextAsync ( 
    	cardID As Guid,
    	cardTypeID As Guid,
    	cardDigest As String,
    	validationResult As IValidationResultBuilder,
    	withoutTransaction As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INotificationContext)
C++ __Копировать
     public:
    virtual ValueTask<INotificationContext^> CreateContextAsync(
    	Guid cardID, 
    	Guid cardTypeID, 
    	String^ cardDigest, 
    	IValidationResultBuilder^ validationResult, 
    	bool withoutTransaction, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CreateContextAsync : 
            cardID : Guid * 
            cardTypeID : Guid * 
            cardDigest : string * 
            validationResult : IValidationResultBuilder * 
            withoutTransaction : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INotificationContext> 
    override CreateContextAsync : 
            cardID : Guid * 
            cardTypeID : Guid * 
            cardDigest : string * 
            validationResult : IValidationResultBuilder * 
            withoutTransaction : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INotificationContext> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardDigest [String](https://learn.microsoft.com/dotnet/api/system.string)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
withoutTransaction
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INotificationContext](T_Tessa_Extensions_Default_Shared_Notices_INotificationContext.htm)>
#### Реализации
[INotificationResolver.CreateContextAsync(Guid, Guid, String,
IValidationResultBuilder, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Notices_INotificationResolver_CreateContextAsync.htm)  
##  __См. также
#### Ссылки
[NotificationResolver -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationResolver.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
