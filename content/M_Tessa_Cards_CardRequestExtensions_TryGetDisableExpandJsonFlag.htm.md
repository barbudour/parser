# CardRequestExtensions.TryGetDisableExpandJsonFlag - метод
Возвращает флаг, указывающий на то, что при экспорте карточки не нужно
разворачивать JSON-поля карточки из строки в Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetDisableExpandJsonFlag(
    	this CardGetRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetDisableExpandJsonFlag ( 
    	request As CardGetRequest
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetDisableExpandJsonFlag(
    	CardGetRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetDisableExpandJsonFlag : 
            request : CardGetRequest -> bool 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на загрузку карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если флаг установлен, иначе false.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
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
