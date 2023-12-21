# CardDeleteExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на удаление карточки, типа
удаляемой карточки, метаинформации по типам карточек и сессии пользователя,
выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDeleteExtensionContext(
    	CardDeleteRequest request,
    	CardDeleteMethod method,
    	CardType cardType,
    	string cardTypeName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope,
    	ICardTransactionStrategy transactionStrategy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardDeleteRequest,
    	method As CardDeleteMethod,
    	cardType As CardType,
    	cardTypeName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dbScope As IDbScope,
    	transactionStrategy As ICardTransactionStrategy,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardDeleteExtensionContext(
    	CardDeleteRequest^ request, 
    	CardDeleteMethod method, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardDeleteRequest * 
            method : CardDeleteMethod * 
            cardType : CardType * 
            cardTypeName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dbScope : IDbScope * 
            transactionStrategy : ICardTransactionStrategy * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardDeleteExtensionContext
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление карточки.
method [CardDeleteMethod](T_Tessa_Cards_CardDeleteMethod.htm)
    Способ удаления карточки.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип удаляемой карточки. Может быть равен null, если неизвестен.
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
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardDeleteExtensionContext -
](T_Tessa_Cards_Extensions_CardDeleteExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
