# CardTransactionStrategy.ExecuteInReaderLockAsync - метод
Выполняет запрос на чтение карточки внутри блокировки reader/writer.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> ExecuteInReaderLockAsync(
    	Guid cardID,
    	IValidationResultBuilder validationResult,
    	Func<ICardTransactionParameter, Task> asyncAction,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ExecuteInReaderLockAsync ( 
    	cardID As Guid,
    	validationResult As IValidationResultBuilder,
    	asyncAction As Func(Of ICardTransactionParameter, Task),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ ExecuteInReaderLockAsync(
    	Guid cardID, 
    	IValidationResultBuilder^ validationResult, 
    	Func<ICardTransactionParameter^, Task^>^ asyncAction, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ExecuteInReaderLockAsync : 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ICardTransactionParameter, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ExecuteInReaderLockAsync : 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ICardTransactionParameter, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой устанавливается блокировка.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
asyncAction
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardTransactionParameter](T_Tessa_Cards_ComponentModel_ICardTransactionParameter.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Запрос на чтение карточки, принимающий параметр с информацией о транзакции, которая включает идентификатор типа карточки и токен отмены операции в свойстве CancellationToken. 
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
[ICardTransactionStrategy.ExecuteInReaderLockAsync(Guid,
IValidationResultBuilder, Func<ICardTransactionParameter, Task>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInReaderLockAsync.htm)  
##  __См. также
#### Ссылки
[CardTransactionStrategy -
](T_Tessa_Cards_ComponentModel_CardTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
