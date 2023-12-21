# GlobalEventAwaiter - класс
Объект, выполняющий ожидание глобального события
[IGlobalEvent](T_Chronos_Platform_IPC_IGlobalEvent.htm) совместно с другими
объектами
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GlobalEventAwaiter
VB __Копировать
     Public NotInheritable Class GlobalEventAwaiter
C++ __Копировать
     public ref class GlobalEventAwaiter sealed
F# __Копировать
     [<SealedAttribute>]
    type GlobalEventAwaiter = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalEventAwaiter
##  __Конструкторы
[GlobalEventAwaiter](M_Chronos_Platform_IPC_GlobalEventAwaiter__ctor.htm)|
Создаёт экземпляр класса с указанием глобального события, ожидание которого
будет выполняться.  
---|---  
## __Свойства
[GlobalEvent](P_Chronos_Platform_IPC_GlobalEventAwaiter_GlobalEvent.htm)|
Глобальное событие, ожидание для которого выполняется посредством текущего
объекта.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WaitAnyAsync](M_Chronos_Platform_IPC_GlobalEventAwaiter_WaitAnyAsync.htm)|
Выполняет ожидание либо глобального события
[GlobalEvent](P_Chronos_Platform_IPC_GlobalEventAwaiter_GlobalEvent.htm), либо
любого из переданных объектов
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).  
## __Методы расширения
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
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
