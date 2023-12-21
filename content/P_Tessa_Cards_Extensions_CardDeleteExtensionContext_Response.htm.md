# CardDeleteExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDeleteResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardDeleteResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardDeleteResponse^ Response {
    	CardDeleteResponse^ get () sealed;
    	void set (CardDeleteResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardDeleteResponse with get, set
    override Response : CardDeleteResponse with get, set
#### Значение свойства
[CardDeleteResponse](T_Tessa_Cards_CardDeleteResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardDeleteExtensionContext -
](T_Tessa_Cards_Extensions_CardDeleteExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
