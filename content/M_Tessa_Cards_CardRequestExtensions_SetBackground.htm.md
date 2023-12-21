# CardRequestExtensions.SetBackground - метод
Устанавливает цвет фона для задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetBackground(
    	this CardTask task,
    	StorageColor? color
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetBackground ( 
    	task As CardTask,
    	color As StorageColor?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetBackground(
    	CardTask^ task, 
    	Nullable<StorageColor> color
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetBackground : 
            task : CardTask * 
            color : Nullable<StorageColor> -> unit 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, для которого требуется установить цвет фона.
color
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[StorageColor](T_Tessa_Platform_Storage_StorageColor.htm)>
    Цвет фона, который требуется установить для задания.
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
