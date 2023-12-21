# CardRequestExtensions.TryGetDisallowCaching - метод
Возвращает признак того, что не следует выполнять кэширование результата.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool? TryGetDisallowCaching(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetDisallowCaching ( 
    	response As CardResponse
    ) As Boolean?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<bool> TryGetDisallowCaching(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetDisallowCaching : 
            response : CardResponse -> Nullable<bool> 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
     Ответ на запрос на действие с карточкой, для которого требуется получить признак того, что не следует выполнять кэширование результата. 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Признак того, что не следует выполнять кэширование результата, или null, если
признак не был задан.
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
