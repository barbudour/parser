# CardRequestExtensions.SetDisallowCaching - метод
Устанавливает признак того, что не следует выполнять кэширование результата.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDisallowCaching(
    	this CardResponse response,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDisallowCaching ( 
    	response As CardResponse,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDisallowCaching(
    	CardResponse^ response, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDisallowCaching : 
            response : CardResponse * 
            value : bool -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
     Ответ на запрос на действие с карточкой, для которого требуется установить признак того, что не следует выполнять кэширование результата. 
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что не следует выполнять кэширование результата. 
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
