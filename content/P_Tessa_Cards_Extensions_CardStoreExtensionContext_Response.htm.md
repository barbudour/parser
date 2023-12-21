# CardStoreExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardStoreResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardStoreResponse^ Response {
    	CardStoreResponse^ get () sealed;
    	void set (CardStoreResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardStoreResponse with get, set
    override Response : CardStoreResponse with get, set
#### Значение свойства
[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
