# CardRequestExtensions.TryGetFileSource - метод
Возвращает местоположение контента файла или null, если местоположение не было
установлено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardFileSourceType? TryGetFileSource(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetFileSource ( 
    	response As CardResponse
    ) As CardFileSourceType?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<CardFileSourceType> TryGetFileSource(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetFileSource : 
            response : CardResponse -> Nullable<CardFileSourceType> 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
     Ответ на запрос к сервису карточек на получение местоположения контента файла. Тип запроса должен был быть [GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)>  
Местоположение контента файла или null, если местоположение не было
установлено.
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
