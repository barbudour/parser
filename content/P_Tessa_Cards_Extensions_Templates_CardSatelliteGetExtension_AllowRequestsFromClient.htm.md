# CardSatelliteGetExtension.AllowRequestsFromClient - свойство
Признак того, что разрешаются запросы на загрузку карточки-сателлита
непосредственно с клиента. Рекомендуется оставить значение по умолчанию false,
если в вашем расширении не предусмотрено собственных средств ограничения
доступа к данным сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual bool AllowRequestsFromClient { get; }
VB __Копировать
     Protected Overridable ReadOnly Property AllowRequestsFromClient As Boolean
    	Get
C++ __Копировать
     protected:
    virtual property bool AllowRequestsFromClient {
    	bool get ();
    }
F# __Копировать
     abstract AllowRequestsFromClient : bool with get
    override AllowRequestsFromClient : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
