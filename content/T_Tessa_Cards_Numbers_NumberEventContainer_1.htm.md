# NumberEventContainer<T> \- класс
Класс-контейнер, позволяющий получить результат ссылочного типа события,
происходящего с номером, которое передаётся в метод
[NotifyOnEventAsync(INumberContext, NumberEventType, Func<INumberContext,
CancellationToken, Task<Boolean>>, Func<INumberContext, CancellationToken,
Task<Boolean>>,
CancellationToken)](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NumberEventContainer<T>
    where T : class
VB __Копировать
     Public NotInheritable Class NumberEventContainer(Of T As Class)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class NumberEventContainer sealed
F# __Копировать
     [<SealedAttribute>]
    type NumberEventContainer<'T when 'T : not struct> = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberEventContainer<T>
#### Параметры типа
T
    Ссылочный тип результата события, происходящего с номером.
##  __Конструкторы
[NumberEventContainer<T>](M_Tessa_Cards_Numbers_NumberEventContainer_1__ctor.htm)|
Создаёт экземпляр класса с указанием события, происходящего с номером.  
---|---  
## __Свойства
[Result](P_Tessa_Cards_Numbers_NumberEventContainer_1_Result.htm)|  Результат
действия, полученный после вызова метода [NumberEventFuncAsync(INumberContext,
CancellationToken)](M_Tessa_Cards_Numbers_NumberEventContainer_1_NumberEventFuncAsync.htm),
или null, если метод не был выполнен или был выполнен с ошибками.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NumberEventFuncAsync](M_Tessa_Cards_Numbers_NumberEventContainer_1_NumberEventFuncAsync.htm)|
Выполняет функцию, переданную в конструкторе, и возвращает признак того, что
функция успешно выполнена.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
