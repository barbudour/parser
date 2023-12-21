# NumberContextActionKeys - класс
Названия действий с номерами, устанавливаемых в контексте
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) посредством метода
[SetNumberAction(INumberContext, String, Func<INumberContext, INumberObject,
CancellationToken,
ValueTask>)](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberAction.htm) и
выполняемых посредством метода [ExecuteNumberActionAsync(INumberContext,
String, INumberObject,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm).
Обычно такие действия используются для обратной связи с элементом управления
номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberContextActionKeys
VB __Копировать
     Public NotInheritable Class NumberContextActionKeys
C++ __Копировать
     public ref class NumberContextActionKeys abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberContextActionKeys = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberContextActionKeys
##  __Поля
[CancelRelease](F_Tessa_Cards_Numbers_NumberContextActionKeys_CancelRelease.htm)|
Действие, выполняемое для отмены освобождения номера, выполненного для
действия
[Released](F_Tessa_Cards_Numbers_NumberContextActionKeys_Released.htm).
Актуально для события
[ReleasingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReleasingNumberFromControl.htm),
причём функция устаналивается внутри самого события.  
---|---  
[Released](F_Tessa_Cards_Numbers_NumberContextActionKeys_Released.htm)|
Действие, выполняемое после успешного освобождения номера. Актуально для
события
[ReleasingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReleasingNumberFromControl.htm).  
[Reserved](F_Tessa_Cards_Numbers_NumberContextActionKeys_Reserved.htm)|
Действие, выполняемое после успешного резервирования номера. Актуально для
событий
[ReservingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReservingNumberFromControl.htm)
и
[ReleasingNumberFromControl](F_Tessa_Cards_Numbers_NumberEventTypes_ReleasingNumberFromControl.htm).  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
