# CardRequestExtensions.SetRequestToCache - метод
Устанавливает признак того, что запрос на получение карточки должен обращаться
к кэшу. Значение актуально для карточек-синглтонов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRequestToCache(
    	this CardGetRequest request,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRequestToCache ( 
    	request As CardGetRequest,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRequestToCache(
    	CardGetRequest^ request, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRequestToCache : 
            request : CardGetRequest * 
            value : bool -> unit 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на получение карточки.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что запрос на получение карточки должен обращаться к кэшу.
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
