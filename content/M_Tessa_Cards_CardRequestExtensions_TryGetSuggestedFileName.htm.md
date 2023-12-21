# CardRequestExtensions.TryGetSuggestedFileName - метод
Возвращает предпочитаемое имя файла, которое используется для загрузки
предпросмотра или создания файла по шаблону, или null, если используется уже
известное имя файла (то, которое задано в шаблоне).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetSuggestedFileName(
    	this CardGetFileContentResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetSuggestedFileName ( 
    	response As CardGetFileContentResponse
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ TryGetSuggestedFileName(
    	CardGetFileContentResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetSuggestedFileName : 
            response : CardGetFileContentResponse -> string 
#### Параметры
response
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)
    Ответ на запрос на получение контента файла.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Предпочитаемое имя файла, которое используется для загрузки предпросмотра или
создания файла по шаблону, или null, если используется уже известное имя файла
(то, которое задано в шаблоне).
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
