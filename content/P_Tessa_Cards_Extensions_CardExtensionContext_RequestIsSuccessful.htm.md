# CardExtensionContext.RequestIsSuccessful - свойство
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RequestIsSuccessful { get; set; }
VB __Копировать
     Public Property RequestIsSuccessful As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool RequestIsSuccessful {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract RequestIsSuccessful : bool with get, set
    override RequestIsSuccessful : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ICardExtensionContext.RequestIsSuccessful](P_Tessa_Cards_Extensions_ICardExtensionContext_RequestIsSuccessful.htm)  
##  __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
