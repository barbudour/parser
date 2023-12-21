# CardRequestExtensions.SetDigestEventName(Dictionary<String, Object>, String)
- метод
Устанавливает имя события по расчёту Digest для сохранения в историю действий
с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDigestEventName(
    	this Dictionary<string, Object> requestInfo,
    	string digestEventName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDigestEventName ( 
    	requestInfo As Dictionary(Of String, Object),
    	digestEventName As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDigestEventName(
    	Dictionary<String^, Object^>^ requestInfo, 
    	String^ digestEventName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDigestEventName : 
            requestInfo : Dictionary<string, Object> * 
            digestEventName : string -> unit 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация request.Info для запроса к сервису карточек.
digestEventName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя события по расчёту Digest для сохранения в историю действий с карточкой. Обычно указывается из констант [CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm) для стандартных событий, или любая уникальная строка для других событий. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
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
[SetDigestEventName -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetDigestEventName.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
