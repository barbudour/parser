# CardGetFileVersionsExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetFileVersionsResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardGetFileVersionsResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardGetFileVersionsResponse^ Response {
    	CardGetFileVersionsResponse^ get () sealed;
    	void set (CardGetFileVersionsResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardGetFileVersionsResponse with get, set
    override Response : CardGetFileVersionsResponse with get, set
#### Значение свойства
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardGetFileVersionsExtensionContext -
](T_Tessa_Cards_Extensions_CardGetFileVersionsExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
