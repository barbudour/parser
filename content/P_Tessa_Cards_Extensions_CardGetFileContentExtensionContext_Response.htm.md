# CardGetFileContentExtensionContext.Response - свойство
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetFileContentResponse Response { get; set; }
VB __Копировать
     Public Property Response As CardGetFileContentResponse
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CardGetFileContentResponse^ Response {
    	CardGetFileContentResponse^ get () sealed;
    	void set (CardGetFileContentResponse^ value) sealed;
    }
F# __Копировать
     abstract Response : CardGetFileContentResponse with get, set
    override Response : CardGetFileContentResponse with get, set
#### Значение свойства
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)
#### Реализации
[ICardRequestExtensionContext<TRequest,
TResponse>.Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)  
##  __См. также
#### Ссылки
[CardGetFileContentExtensionContext -
](T_Tessa_Cards_Extensions_CardGetFileContentExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
