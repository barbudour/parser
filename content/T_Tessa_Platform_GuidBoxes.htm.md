# GuidBoxes - класс
Упакованные значения для часто используемых
[Guid](https://learn.microsoft.com/dotnet/api/system.guid). Поля класса можно
использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class GuidBoxes
VB __Копировать
     Public NotInheritable Class GuidBoxes
C++ __Копировать
     public ref class GuidBoxes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type GuidBoxes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GuidBoxes
##  __Методы
[Box(Guid)](M_Tessa_Platform_GuidBoxes_Box.htm)|  Возвращает упакованное
значение, причём для предопределённых значений не выполняет операции упаковки.  
---|---  
[Box(Nullable<Guid>)](M_Tessa_Platform_GuidBoxes_Box_1.htm)|  Возвращает
упакованное значение, причём для предопределённых значений не выполняет
операции упаковки.  
## __Поля
[Empty](F_Tessa_Platform_GuidBoxes_Empty.htm)|  Пустое значение. Соответствует
значению поля
[Empty](https://learn.microsoft.com/dotnet/api/system.guid.empty).  
---|---  
[SystemUserID](F_Tessa_Platform_GuidBoxes_SystemUserID.htm)|  Идентификатор
пользователя System. Соответствует значению поля
[SystemID](F_Tessa_Platform_Runtime_Session_SystemID.htm).  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
