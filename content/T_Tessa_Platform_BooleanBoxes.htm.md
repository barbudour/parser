# BooleanBoxes - класс
Упакованные значения для часто используемых
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Поля класса
можно использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class BooleanBoxes
VB __Копировать
     Public NotInheritable Class BooleanBoxes
C++ __Копировать
     public ref class BooleanBoxes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type BooleanBoxes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ BooleanBoxes
##  __Методы
[Box(Boolean)](M_Tessa_Platform_BooleanBoxes_Box.htm)|  Возвращает упакованное
значение, причём для предопределённых значений не выполняет операции упаковки.  
---|---  
[Box(Nullable<Boolean>)](M_Tessa_Platform_BooleanBoxes_Box_1.htm)|  Возвращает
упакованное значение, причём для предопределённых значений не выполняет
операции упаковки.  
## __Поля
[False](F_Tessa_Platform_BooleanBoxes_False.htm)|  Значение false.  
---|---  
[True](F_Tessa_Platform_BooleanBoxes_True.htm)|  Значение true.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
