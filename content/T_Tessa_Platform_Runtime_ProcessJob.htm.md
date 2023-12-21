# ProcessJob - класс
Обёртка для использования объекта WinAPI Job.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ProcessJob : IDisposable
VB __Копировать
     Public NotInheritable Class ProcessJob
    	Implements IDisposable
C++ __Копировать
     public ref class ProcessJob sealed : IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ProcessJob = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessJob
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[ProcessJob](M_Tessa_Platform_Runtime_ProcessJob__ctor.htm)|  Создаёт
экземпляр класса. Выполняет создание объекта Job средствами WinAPI.  
---|---  
## __Методы
[AddProcess](M_Tessa_Platform_Runtime_ProcessJob_AddProcess.htm)|  Добавляет
Handle процесса в объект WinAPI Job.  
---|---  
[Dispose](M_Tessa_Platform_Runtime_ProcessJob_Dispose.htm)|  Освобождает
занятые объектом ресурсы.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](M_Tessa_Platform_Runtime_ProcessJob_Finalize.htm)|  Финализатор
объекта.  
(Переопределяет
[Object.Finalize()](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize))  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
