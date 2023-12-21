# CardGetExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardGetResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardGetResponse^ Response {
    	CardGetResponse^ get () sealed;
    	void set (CardGetResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardGetResponse with get, set
    override Response : CardGetResponse with get, set
#### Значение свойства
[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardGetExtensionContext -
](T_Tessa_Cards_Extensions_CardGetExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
