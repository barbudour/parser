# CardOnContentStoringEventArgs.Success - свойство
Признак того, что карточка была успешно сохранена, все расширения успешно
выполнены (в т.ч. AfterRequest), после чего успешно сохранено содержимое всех
файлов. Соответствует признаку того, что результат успешен
Context.ValidationResult.IsSuccessful() на момент вызова обработчиков событий
[ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Success { get; }
VB __Копировать
     Public ReadOnly Property Success As Boolean
    	Get
C++ __Копировать
     public:
    property bool Success {
    	bool get ();
    }
F# __Копировать
     member Success : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardOnContentStoringEventArgs -
](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
