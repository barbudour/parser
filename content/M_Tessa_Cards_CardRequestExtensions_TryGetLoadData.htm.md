# CardRequestExtensions.TryGetLoadData - метод
Возвращает признак того, что следует выполнить загрузку бинарных данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool? TryGetLoadData(
    	this CardRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetLoadData ( 
    	request As CardRequest
    ) As Boolean?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<bool> TryGetLoadData(
    	CardRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetLoadData : 
            request : CardRequest -> Nullable<bool> 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
     Запрос на действие с карточкой, для которого требуется получить признак того, что следует выполнить загрузку бинарных данных. 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Признак того, что следует выполнить загрузку бинарных данных, или null, если
признак не был задан.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequest](T_Tessa_Cards_CardRequest.htm). При вызове метода
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
