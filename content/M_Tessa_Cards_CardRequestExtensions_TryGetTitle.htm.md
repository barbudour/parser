# CardRequestExtensions.TryGetTitle - метод
Возвращает заголовок задания, который выводится вместо типа задания, или null,
если заголовок не задан и выводится тип задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetTitle(
    	this CardTask task
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTitle ( 
    	task As CardTask
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ TryGetTitle(
    	CardTask^ task
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTitle : 
            task : CardTask -> string 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, для которого требуется получить заголовок.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Заголовок задания, который выводится вместо типа задания, или null, если
заголовок не задан и выводится тип задания.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTask](T_Tessa_Cards_CardTask.htm). При вызове метода для
экземпляра следует опускать первый параметр. Дополнительные сведения см. в
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
