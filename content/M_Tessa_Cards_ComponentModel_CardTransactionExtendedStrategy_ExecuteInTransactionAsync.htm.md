# CardTransactionExtendedStrategy.ExecuteInTransactionAsync - метод
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> ExecuteInTransactionAsync(
    	IValidationResultBuilder validationResult,
    	Func<ITransactionParameter, Task> asyncAction,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ExecuteInTransactionAsync ( 
    	validationResult As IValidationResultBuilder,
    	asyncAction As Func(Of ITransactionParameter, Task),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ ExecuteInTransactionAsync(
    	IValidationResultBuilder^ validationResult, 
    	Func<ITransactionParameter^, Task^>^ asyncAction, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ExecuteInTransactionAsync : 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ITransactionParameter, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ExecuteInTransactionAsync : 
            validationResult : IValidationResultBuilder * 
            asyncAction : Func<ITransactionParameter, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
asyncAction
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ITransactionParameter](T_Tessa_Platform_Data_ITransactionParameter.htm),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Асинхронный метод, принимающий параметр с информацией о транзакции. Исполняется внутри в транзакции. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если транзакция успешно завершилась; false, если в процессе создания или
выполнения транзакции произошло исключение, причём произошёл откат начатой
транзакции.
#### Реализации
[ITransactionStrategy.ExecuteInTransactionAsync(IValidationResultBuilder,
Func<ITransactionParameter, Task>,
CancellationToken)](M_Tessa_Platform_Data_ITransactionStrategy_ExecuteInTransactionAsync.htm)  
##  __См. также
#### Ссылки
[CardTransactionExtendedStrategy -
](T_Tessa_Cards_ComponentModel_CardTransactionExtendedStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
