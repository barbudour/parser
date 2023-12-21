# CardRequestExtensions.SetSuggestedFileName - метод
Устанавливает предпочитаемое имя файла, которое используется для загрузки
предпросмотра или создания файла по шаблону.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSuggestedFileName(
    	this CardGetFileContentResponse response,
    	string fileName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetSuggestedFileName ( 
    	response As CardGetFileContentResponse,
    	fileName As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetSuggestedFileName(
    	CardGetFileContentResponse^ response, 
    	String^ fileName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetSuggestedFileName : 
            response : CardGetFileContentResponse * 
            fileName : string -> unit 
#### Параметры
response
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)
    Ответ на запрос на получение контента файла.
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Предпочитаемое имя файла, которое используется для загрузки предпросмотра или создания файла по шаблону, или null, если используется уже известное имя файла (то, которое задано в шаблоне). 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
