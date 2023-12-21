# CardRequestExtensions.TryGetDigestEventName - метод
Возвращает имя события по расчёту Digest для сохранения в историю действий с
карточкой или null, если имя события не было установлено. Имена стандартных
событий указаны в константах
[CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetDigestEventName(
    	this CardRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetDigestEventName ( 
    	request As CardRequest
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ TryGetDigestEventName(
    	CardRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetDigestEventName : 
            request : CardRequest -> string 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя события по расчёту Digest для сохранения в историю действий с карточкой
или null, если имя события не было установлено.
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
