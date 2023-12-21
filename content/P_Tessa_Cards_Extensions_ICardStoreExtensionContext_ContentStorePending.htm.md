# ICardStoreExtensionContext.ContentStorePending - свойство
Признак того, что ожидается сохранение содержимого файлов, выполняемое
отложенно после расширений AfterRequest. Используйте событие
[ICardStoreExtensionContext.ContentStoreCompleted], чтобы подписаться на
момент завершения изменений в контенте и выполнить действия в обработчике
события.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool ContentStorePending { get; }
VB __Копировать
     ReadOnly Property ContentStorePending As Boolean
    	Get
C++ __Копировать
    property bool ContentStorePending {
    	bool get ();
    }
F# __Копировать
     abstract ContentStorePending : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[ICardStoreExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
