# CardRequestExtensions.SetFile - метод
Устанавливает файл для использования в универсальном запросе к API карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFile(
    	this CardRequest request,
    	CardFile file
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetFile ( 
    	request As CardRequest,
    	file As CardFile
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetFile(
    	CardRequest^ request, 
    	CardFile^ file
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetFile : 
            request : CardRequest * 
            file : CardFile -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
file [CardFile](T_Tessa_Cards_CardFile.htm)
     Файл, устанавливаемый в запросе. Параметр равен null, когда значение требуется удалить. 
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
