# NumberBuilderParameters - класс
Известные платформе параметры, используемые для передачи в метод
[GetAsync<T>(INumberContext, Object,
CancellationToken)](M_Tessa_Cards_Numbers_INumberBuilder_GetAsync__1.htm) для
получения результатов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberBuilderParameters
VB __Копировать
     Public NotInheritable Class NumberBuilderParameters
C++ __Копировать
     public ref class NumberBuilderParameters abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberBuilderParameters = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberBuilderParameters
##  __Поля
[CanEditNumber](F_Tessa_Cards_Numbers_NumberBuilderParameters_CanEditNumber.htm)|
Возвращает [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) \-
признак того, что поля номера можно редактировать вручную, а также доступно
выделение или освобождение посредством
[CanReplaceNumber](F_Tessa_Cards_Numbers_NumberBuilderParameters_CanReplaceNumber.htm).
Реализация по умолчанию возвращает значение в зависимости от разрешений в
[CardPermissions](P_Tessa_Cards_CardPermissionInfo_CardPermissions.htm).  
---|---  
[CanReplaceNumber](F_Tessa_Cards_Numbers_NumberBuilderParameters_CanReplaceNumber.htm)|
Возвращает [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) \-
признак того, что номер можно выделить или освободить вручную. Реализация по
умолчанию всегда возвращает true.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
