# Int32Boxes - класс
Упакованные значения для часто используемых
[Int32](https://learn.microsoft.com/dotnet/api/system.int32). Поля класса
можно использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class Int32Boxes
VB __Копировать
     Public NotInheritable Class Int32Boxes
C++ __Копировать
     public ref class Int32Boxes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type Int32Boxes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Int32Boxes
##  __Методы
[Box(Int32)](M_Tessa_Platform_Int32Boxes_Box.htm)|  Возвращает упакованное
значение, причём для предопределённых значений не выполняет операции упаковки.  
---|---  
[Box(Nullable<Int32>)](M_Tessa_Platform_Int32Boxes_Box_1.htm)|  Возвращает
упакованное значение, причём для предопределённых значений не выполняет
операции упаковки.  
## __Поля
[MinusOne](F_Tessa_Platform_Int32Boxes_MinusOne.htm)|  Значение -1.  
---|---  
[One](F_Tessa_Platform_Int32Boxes_One.htm)|  Значение 1.  
[Zero](F_Tessa_Platform_Int32Boxes_Zero.htm)|  Значение 0.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
