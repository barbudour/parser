# CardRequestExtensions.TryGetWipeDeletedFlag - метод
Возвращает флаг, который указывает на то, что нужно очищать удаленные в
корзину карточки, если они будут мешать импорту.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetWipeDeletedFlag(
    	this CardStoreRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetWipeDeletedFlag ( 
    	request As CardStoreRequest
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetWipeDeletedFlag(
    	CardStoreRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetWipeDeletedFlag : 
            request : CardStoreRequest -> bool 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
