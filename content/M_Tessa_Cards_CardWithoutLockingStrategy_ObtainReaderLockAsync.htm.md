# CardWithoutLockingStrategy.ObtainReaderLockAsync - метод
Выполняет взятие блокировки на чтение карточки. Возвращает признак успешного
взятия блокировки и идентификатор типа для заданной карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(bool success, Guid cardTypeID)> ObtainReaderLockAsync(
    	Guid cardID,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ObtainReaderLockAsync ( 
    	cardID As Guid,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (success As Boolean, cardTypeID As Guid))
C++ __Копировать
     public:
    virtual Task<ValueTuple<bool, Guid>>^ ObtainReaderLockAsync(
    	Guid cardID, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ObtainReaderLockAsync : 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Guid>> 
    override ObtainReaderLockAsync : 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Guid>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой устанавливается блокировка.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Объект, осуществляющий построение результата валидации с указанием причины, по которой не удалось взять блокировку. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
true, если блокировка успешно взята; false, если в процессе взятия блокировки
произошла ошибка.
#### Реализации
[ICardLockingStrategy.ObtainReaderLockAsync(Guid, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ICardLockingStrategy_ObtainReaderLockAsync.htm)  
##  __См. также
#### Ссылки
[CardWithoutLockingStrategy - ](T_Tessa_Cards_CardWithoutLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
