# CardRequestExtensions.TryGetTypedResponseStorage - метод
Возвращает хранилище для строготипизированного ответа на запрос для
универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, Object> TryGetTypedResponseStorage(
    	this CardResponse cardResponse
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTypedResponseStorage ( 
    	cardResponse As CardResponse
    ) As Dictionary(Of String, Object)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Dictionary<String^, Object^>^ TryGetTypedResponseStorage(
    	CardResponse^ cardResponse
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTypedResponseStorage : 
            cardResponse : CardResponse -> Dictionary<string, Object> 
#### Параметры
cardResponse [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Универсальный ответ на запрос к API карточек.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Хранилище для строготипизированного ответа на запрос для универсальных
расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
