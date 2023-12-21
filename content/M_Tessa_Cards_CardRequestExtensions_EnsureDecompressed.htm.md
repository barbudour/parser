# CardRequestExtensions.EnsureDecompressed - метод
Гарантирует, что ответ на запрос по получению карточки не содержит сжатую
карточку. Если карточка сжата, то метод производит её декомпрессию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void EnsureDecompressed(
    	this CardGetResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub EnsureDecompressed ( 
    	response As CardGetResponse
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void EnsureDecompressed(
    	CardGetResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member EnsureDecompressed : 
            response : CardGetResponse -> unit 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
     Ответ на запрос по получению карточки, для которого требуется гарантировать, что возвращённая карточка не сжата и к ней можно обращаться стандартным способом. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm). При вызове
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
