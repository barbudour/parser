# CardTransactionParameter - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTransactionParameter(
    	IValidationResultBuilder validationResult,
    	IDbScope dbScope,
    	Guid? cardID = null,
    	Guid? cardTypeID = null,
    	int version = -1,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	validationResult As IValidationResultBuilder,
    	dbScope As IDbScope,
    	Optional cardID As Guid? = Nothing,
    	Optional cardTypeID As Guid? = Nothing,
    	Optional version As Integer = -1,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardTransactionParameter(
    	IValidationResultBuilder^ validationResult, 
    	IDbScope^ dbScope, 
    	Nullable<Guid> cardID = nullptr, 
    	Nullable<Guid> cardTypeID = nullptr, 
    	int version = -1, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            validationResult : IValidationResultBuilder * 
            dbScope : IDbScope * 
            ?cardID : Nullable<Guid> * 
            ?cardTypeID : Nullable<Guid> * 
            ?version : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardID = defaultArg cardID null
            let _cardTypeID = defaultArg cardTypeID null
            let _version = defaultArg version -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardTransactionParameter
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, связанный с открытой транзакцией.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор карточки, для которой выполняется транзакция, или null, если идентификатор карточки не проверяется. 
cardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор типа карточки, для которой выполняется транзакция, или null, если идентификатор неизвестен. 
version [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
     Номер версии карточки, для которой должна быть открыта транзакция, или [DoNotCheckVersion](F_Tessa_Cards_ComponentModel_CardComponentHelper_DoNotCheckVersion.htm), если версия карточки не проверяется. Версия всегда не проверяется при чтении карточки и может проверяться при изменении карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Токен отмены асинхронной операции.
##  __См. также
#### Ссылки
[CardTransactionParameter -
](T_Tessa_Cards_ComponentModel_CardTransactionParameter.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
