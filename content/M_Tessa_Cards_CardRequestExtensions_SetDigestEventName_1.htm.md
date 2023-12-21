# CardRequestExtensions.SetDigestEventName(CardRequest, String) - метод
Устанавливает имя события по расчёту Digest для сохранения в историю действий
с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDigestEventName(
    	this CardRequest request,
    	string digestEventName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDigestEventName ( 
    	request As CardRequest,
    	digestEventName As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDigestEventName(
    	CardRequest^ request, 
    	String^ digestEventName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDigestEventName : 
            request : CardRequest * 
            digestEventName : string -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
digestEventName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя события по расчёту Digest для сохранения в историю действий с карточкой. Обычно указывается из констант [CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm) для стандартных событий, или любая уникальная строка для других событий. 
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
[SetDigestEventName -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetDigestEventName.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
