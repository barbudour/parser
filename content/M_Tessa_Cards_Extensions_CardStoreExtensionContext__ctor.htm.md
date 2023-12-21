# CardStoreExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на сохранение карточки, типа
сохраняемой карточки, метаинформации по типам карточек и сессии пользователя,
выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreExtensionContext(
    	CardStoreRequest request,
    	CardStoreMethod method,
    	CardType cardType,
    	string cardTypeName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope,
    	ICardTransactionStrategy transactionStrategy,
    	Func<DateTime?> getStoreDateTime,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardStoreRequest,
    	method As CardStoreMethod,
    	cardType As CardType,
    	cardTypeName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dbScope As IDbScope,
    	transactionStrategy As ICardTransactionStrategy,
    	getStoreDateTime As Func(Of DateTime?),
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardStoreExtensionContext(
    	CardStoreRequest^ request, 
    	CardStoreMethod method, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	Func<Nullable<DateTime>>^ getStoreDateTime, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardStoreRequest * 
            method : CardStoreMethod * 
            cardType : CardType * 
            cardTypeName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dbScope : IDbScope * 
            transactionStrategy : ICardTransactionStrategy * 
            getStoreDateTime : Func<Nullable<DateTime>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardStoreExtensionContext
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
method [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm)
    Способ сохранения карточки.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип сохраняемой карточки. Может быть равен null, если неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего операцию.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
     Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и не равно null на сервере. 
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
     Стратегия обеспечения блокировок и выполнения транзакций, используемая сервисом или null, если стратегия не используется, например, на клиенте. 
getStoreDateTime
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>>
     Функция, возвращающая текущие дату и время сохранения для использования в транзакции или null, если код не выполняется в транзакции. Экземпляр класса создаётся раньше, чем будет известно значение свойства [StoreDateTime](P_Tessa_Cards_Extensions_CardStoreExtensionContext_StoreDateTime.htm), поэтому используется функция. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
