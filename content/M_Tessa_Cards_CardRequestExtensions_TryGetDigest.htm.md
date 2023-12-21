# CardRequestExtensions.TryGetDigest - метод
Возвращает Digest для сохранения в историю действий с карточкой или null, если
Digest не был установлен.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetDigest(
    	this CardInfoStorageObject request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetDigest ( 
    	request As CardInfoStorageObject
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ TryGetDigest(
    	CardInfoStorageObject^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetDigest : 
            request : CardInfoStorageObject -> string 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Digest для сохранения в историю действий с карточкой или null, если Digest не
был установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).
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
