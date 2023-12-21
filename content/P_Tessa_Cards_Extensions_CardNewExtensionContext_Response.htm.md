# CardNewExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardNewResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardNewResponse^ Response {
    	CardNewResponse^ get () sealed;
    	void set (CardNewResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardNewResponse with get, set
    override Response : CardNewResponse with get, set
#### Значение свойства
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardNewExtensionContext -
](T_Tessa_Cards_Extensions_CardNewExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
