# CardRequestExtensions.TryGetBackground - метод
Возвращает цвет фона для задания или null, если цвет фона не установлен.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static StorageColor? TryGetBackground(
    	this CardTask task
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetBackground ( 
    	task As CardTask
    ) As StorageColor?
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Nullable<StorageColor> TryGetBackground(
    	CardTask^ task
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetBackground : 
            task : CardTask -> Nullable<StorageColor> 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, для которого требуется получить цвет фона.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[StorageColor](T_Tessa_Platform_Storage_StorageColor.htm)>  
Цвет фона для задания или null, если цвет фона не установлен.
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
