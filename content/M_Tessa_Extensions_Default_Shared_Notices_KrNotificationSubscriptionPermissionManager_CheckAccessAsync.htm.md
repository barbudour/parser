# KrNotificationSubscriptionPermissionManager.CheckAccessAsync(Card,
IValidationResultBuilder, CancellationToken) - метод
Метод для проверки доступа по объекту карточки для текущего сотрудника. Данный
метод доступен как на стороне сервера, так и клиента.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<bool> CheckAccessAsync(
    	Card card,
    	IValidationResultBuilder validationResult = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function CheckAccessAsync ( 
    	card As Card,
    	Optional validationResult As IValidationResultBuilder = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> CheckAccessAsync(
    	Card^ card, 
    	IValidationResultBuilder^ validationResult = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CheckAccessAsync : 
            card : Card * 
            ?validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override CheckAccessAsync : 
            card : Card * 
            ?validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Объект карточки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
    Билдер результата валидации, куда пишется ошибка валидации, если он задан.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если проверка прошла успешно, иначе false.
#### Реализации
[INotificationSubscriptionPermissionManager.CheckAccessAsync(Card,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Notices_INotificationSubscriptionPermissionManager_CheckAccessAsync_1.htm)  
##  __См. также
#### Ссылки
[KrNotificationSubscriptionPermissionManager -
](T_Tessa_Extensions_Default_Shared_Notices_KrNotificationSubscriptionPermissionManager.htm)
[CheckAccessAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Notices_KrNotificationSubscriptionPermissionManager_CheckAccessAsync.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
