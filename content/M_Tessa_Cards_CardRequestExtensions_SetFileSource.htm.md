# CardRequestExtensions.SetFileSource - метод
Устанавливает местоположение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFileSource(
    	this CardResponse response,
    	CardFileSourceType? value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetFileSource ( 
    	response As CardResponse,
    	value As CardFileSourceType?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetFileSource(
    	CardResponse^ response, 
    	Nullable<CardFileSourceType> value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetFileSource : 
            response : CardResponse * 
            value : Nullable<CardFileSourceType> -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
     Ответ на запрос к сервису карточек на получение местоположения контента файла. Тип запроса должен был быть [GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). 
value
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)>
     Местоположение контента файла. Параметр равен null, когда значение требуется удалить. 
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
