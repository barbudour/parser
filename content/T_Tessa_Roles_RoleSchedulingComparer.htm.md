# RoleSchedulingComparer - класс
Сравнивает объекты ролевой модели по свойствам, ответственным за планирование.
Используется для проверки необходимости того, что объект необходимо
запланировать по другому расписанию.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleSchedulingComparer : IEqualityComparer<IRoleSchedulingProvider>
VB __Копировать
     Public NotInheritable Class RoleSchedulingComparer
    	Implements IEqualityComparer(Of IRoleSchedulingProvider)
C++ __Копировать
     public ref class RoleSchedulingComparer sealed : IEqualityComparer<IRoleSchedulingProvider^>
F# __Копировать
     [<SealedAttribute>]
    type RoleSchedulingComparer = 
        class
            interface IEqualityComparer<IRoleSchedulingProvider>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleSchedulingComparer
Implements
    [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[IRoleSchedulingProvider](T_Tessa_Roles_IRoleSchedulingProvider.htm)>
##  __Конструкторы
[RoleSchedulingComparer](M_Tessa_Roles_RoleSchedulingComparer__ctor.htm)|
Инициализирует новый экземпляр класса RoleSchedulingComparer  
---|---  
##  __Свойства
[Instance](P_Tessa_Roles_RoleSchedulingComparer_Instance.htm)| Экземпляр
класса.  
---|---  
##  __Методы
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Equals(IRoleSchedulingProvider,
IRoleSchedulingProvider)](M_Tessa_Roles_RoleSchedulingComparer_Equals.htm)|
Сравнивает объекты ролевой модели по свойствам, ответственным за планирование.
Используется для проверки необходимости того, что объект необходимо
запланировать по другому расписанию.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(IRoleSchedulingProvider)](M_Tessa_Roles_RoleSchedulingComparer_GetHashCode.htm)|
Возвращает хеш-код объекта, полученный из полей, ответственных за
планирование.  
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
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
