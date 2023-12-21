# CardNewExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на создание структуры карточки,
типа карточки, структура которой создаётся, метаинформации по типам карточек и
сессии пользователя, выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewExtensionContext(
    	CardNewRequest request,
    	CardNewMethod method,
    	CardType cardType,
    	string cardTypeName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardNewRequest,
    	method As CardNewMethod,
    	cardType As CardType,
    	cardTypeName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional dbScope As IDbScope = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardNewExtensionContext(
    	CardNewRequest^ request, 
    	CardNewMethod method, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardNewRequest * 
            method : CardNewMethod * 
            cardType : CardType * 
            cardTypeName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardNewExtensionContext
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание структуры карточки.
method [CardNewMethod](T_Tessa_Cards_CardNewMethod.htm)
    Способ создания карточки.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, структура которой создаётся. Может быть равен null, если неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего операцию.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и не равно null на сервере. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardNewExtensionContext -
](T_Tessa_Cards_Extensions_CardNewExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
