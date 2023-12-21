# CardLockingStrategy.ObtainWriterLockCoreAsync - метод
Выполняет взятие блокировки на запись карточки. Возвращает признак успешного
взятия блокировки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> ObtainWriterLockCoreAsync(
    	Guid cardID,
    	int version,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ObtainWriterLockCoreAsync ( 
    	cardID As Guid,
    	version As Integer,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ ObtainWriterLockCoreAsync(
    	Guid cardID, 
    	int version, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ObtainWriterLockCoreAsync : 
            cardID : Guid * 
            version : int * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ObtainWriterLockCoreAsync : 
            cardID : Guid * 
            version : int * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой устанавливается блокировка.
version [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Ожидаемая версия карточки в базе данных или [CardComponentHelper.DoNotCheckVersion], если проверять версию не требуется. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Объект, осуществляющий построение результата валидации с указанием причины, по которой не удалось взять блокировку. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если блокировка успешно взята; false, если в процессе взятия блокировки
произошла ошибка.
## __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
