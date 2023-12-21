# CardRequestExtensions.SetDigest(Dictionary<String, Object>, String) - метод
Устанавливает Digest для сохранения в историю действий с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDigest(
    	this Dictionary<string, Object> requestInfo,
    	string digest
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDigest ( 
    	requestInfo As Dictionary(Of String, Object),
    	digest As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDigest(
    	Dictionary<String^, Object^>^ requestInfo, 
    	String^ digest
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDigest : 
            requestInfo : Dictionary<string, Object> * 
            digest : string -> unit 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация request.Info для запроса к сервису карточек.
digest [String](https://learn.microsoft.com/dotnet/api/system.string)
    Digest для сохранения в историю действий с карточкой.
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
[SetDigest -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetDigest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
