# CardRequestExtensions.ResetRequestToCache - метод
Сбрасывает признак того, что запрос на получение карточки должен обращаться к
кэшу. После выполнения метода запрос будет выполняться стандартным образом,
т.е. в обход кэша. Значение актуально для карточек-синглтонов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ResetRequestToCache(
    	this CardGetRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ResetRequestToCache ( 
    	request As CardGetRequest
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ResetRequestToCache(
    	CardGetRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ResetRequestToCache : 
            request : CardGetRequest -> unit 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на получение карточки.
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
