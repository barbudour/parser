# CardWithoutTransactionStrategy.ExecuteInWriterLockAsync - метод
Выполняет запрос на изменение карточки внутри блокировки reader/writer и
внутри транзакции. Последним действием внутри делегата asyncAction должно быть
увеличение номера версии карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> ExecuteInWriterLockAsync(
    	Guid cardID,
    	int version,
    	IValidationResultBuilder validationResult,
    	Func<ICardTransactionParameter, Task> asyncAction,
    	bool releaseLock = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ExecuteInWriterLockAsync ( 
    	cardID As Guid,
    	version As Integer,
    	validationResult As IValidationResultBuilder,
    	asyncAction As Func(Of ICardTransactionParameter, Task),
    	Optional releaseLock As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ ExecuteInWriterLockAsync(
    	Guid cardID, 
    	int version, 
    	IValidationResultBuilder^ validationResult, 
    	Func<ICardTransactionParameter^, Task^>^ asyncAction, 
    	bool releaseLock = true, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ExecuteInWriterLockAsync : 
            cardID : Guid * 
            version : int * 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ICardTransactionParameter, Task> * 
            ?releaseLock : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _releaseLock = defaultArg releaseLock true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ExecuteInWriterLockAsync : 
            cardID : Guid * 
            version : int * 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ICardTransactionParameter, Task> * 
            ?releaseLock : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _releaseLock = defaultArg releaseLock true
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
    Объект, осуществляющий построение результата валидации.
asyncAction
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardTransactionParameter](T_Tessa_Cards_ComponentModel_ICardTransactionParameter.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Запрос на изменение карточки, принимающий параметр с информацией о транзакции, которая включает токен отмены операции в свойстве CancellationToken. Исполняется внутри SQL-транзакции. 
releaseLock [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что блокировку необходимо освободить при успешном завершении действий с карточкой. Устанавливайте значение false только в случае, если карточка удалена к моменту освобождения блокировки. В случае возникновения исключений блокировка будет снята в случае, если она была установлена, независимо от значения этого параметра. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если запрос успешно завершился; false, если в процессе создания
транзакции или выполнения запроса произошло исключение, причём произошёл откат
начатой транзакции.
#### Реализации
[ICardTransactionStrategy.ExecuteInWriterLockAsync(Guid, Int32,
IValidationResultBuilder, Func<ICardTransactionParameter, Task>, Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInWriterLockAsync.htm)  
##  __См. также
#### Ссылки
[CardWithoutTransactionStrategy -
](T_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
