# CardRequestExtensions.SetDigest(CardInfoStorageObject, String) - метод
Устанавливает Digest для сохранения в историю действий с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDigest(
    	this CardInfoStorageObject request,
    	string digest
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDigest ( 
    	request As CardInfoStorageObject,
    	digest As String
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDigest(
    	CardInfoStorageObject^ request, 
    	String^ digest
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDigest : 
            request : CardInfoStorageObject * 
            digest : string -> unit 
#### Параметры
request [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Запрос к сервису карточек.
digest [String](https://learn.microsoft.com/dotnet/api/system.string)
    Digest для сохранения в историю действий с карточкой.
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
[SetDigest -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetDigest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
