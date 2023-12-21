# DoubleBoxes - класс
Упакованные значения для часто используемых
[Double](https://learn.microsoft.com/dotnet/api/system.double). Поля класса
можно использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DoubleBoxes
VB __Копировать
     Public NotInheritable Class DoubleBoxes
C++ __Копировать
     public ref class DoubleBoxes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DoubleBoxes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DoubleBoxes
##  __Методы
[Box(Double)](M_Tessa_Platform_DoubleBoxes_Box.htm)|  Возвращает упакованное
значение, причём для предопределённых значений не выполняет операции упаковки.  
---|---  
[Box(Nullable<Double>)](M_Tessa_Platform_DoubleBoxes_Box_1.htm)|  Возвращает
упакованное значение, причём для предопределённых значений не выполняет
операции упаковки.  
## __Поля
[NaN](F_Tessa_Platform_DoubleBoxes_NaN.htm)|  Значение
[NaN](https://learn.microsoft.com/dotnet/api/system.double.nan).  
---|---  
[NegativeInfinity](F_Tessa_Platform_DoubleBoxes_NegativeInfinity.htm)|
Значение
[NegativeInfinity](https://learn.microsoft.com/dotnet/api/system.double.negativeinfinity).  
[NegativeOne](F_Tessa_Platform_DoubleBoxes_NegativeOne.htm)|  Значение -1.  
[PositiveInfinity](F_Tessa_Platform_DoubleBoxes_PositiveInfinity.htm)|
Значение
[PositiveInfinity](https://learn.microsoft.com/dotnet/api/system.double.positiveinfinity).  
[PositiveOne](F_Tessa_Platform_DoubleBoxes_PositiveOne.htm)|  Значение 1.  
[Zero](F_Tessa_Platform_DoubleBoxes_Zero.htm)|  Значение 0.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
