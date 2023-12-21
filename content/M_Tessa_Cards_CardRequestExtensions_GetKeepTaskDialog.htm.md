# CardRequestExtensions.GetKeepTaskDialog(Dictionary<String, Object>) - метод
Возвращает значение показывающее требуется ли оставить открытым окно диалога
или нет.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetKeepTaskDialog(
    	this Dictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetKeepTaskDialog ( 
    	info As Dictionary(Of String, Object)
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool GetKeepTaskDialog(
    	Dictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetKeepTaskDialog : 
            info : Dictionary<string, Object> -> bool 
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Словарь в котором находится проверяемое значение.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если окно диалога должно остаться открытым, иначе - false.
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
[GetKeepTaskDialog -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_GetKeepTaskDialog.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
