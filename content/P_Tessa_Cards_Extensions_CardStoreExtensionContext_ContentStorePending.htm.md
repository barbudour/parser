# CardStoreExtensionContext.ContentStorePending - свойство
Признак того, что ожидается сохранение содержимого файлов, выполняемое
отложенно после расширений AfterRequest. Используйте событие
[ICardStoreExtensionContext.ContentStoreCompleted], чтобы подписаться на
момент завершения изменений в контенте и выполнить действия в обработчике
события.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ContentStorePending { get; set; }
VB __Копировать
     Public Property ContentStorePending As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool ContentStorePending {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract ContentStorePending : bool with get, set
    override ContentStorePending : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ICardStoreExtensionContext.ContentStorePending](P_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStorePending.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
