# ProcessNameResolver - класс
Объект, обеспечивающий получение отображаемого имени приложения по
запускающему файлу процесса, обычно по .exe.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ProcessNameResolver : IProcessNameResolver
VB __Копировать
     Public NotInheritable Class ProcessNameResolver
    	Implements IProcessNameResolver
C++ __Копировать
     public ref class ProcessNameResolver sealed : IProcessNameResolver
F# __Копировать
     [<SealedAttribute>]
    type ProcessNameResolver = 
        class
            interface IProcessNameResolver
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessNameResolver
Implements
    [IProcessNameResolver](T_Tessa_Platform_IProcessNameResolver.htm)
##  __Конструкторы
[ProcessNameResolver](M_Tessa_Platform_ProcessNameResolver__ctor.htm)|
Инициализирует новый экземпляр класса ProcessNameResolver  
---|---  
##  __Методы
[Contains](M_Tessa_Platform_ProcessNameResolver_Contains.htm)|  Возвращает
признак того, что текущий объект содержит информацию по имени приложения для
заданного имени файла, запускающего приложение.  
---|---  
[CreateDefault](M_Tessa_Platform_ProcessNameResolver_CreateDefault.htm)|
Создаёт экземпляр класса ProcessNameResolver, содержащего информацию по именам
часто используемых приложений.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Register](M_Tessa_Platform_ProcessNameResolver_Register.htm)|  Выполняет
регистрацию имени приложения, пригодного для отображения пользователю, по
имени файла, запускающего приложение.  
[Remove](M_Tessa_Platform_ProcessNameResolver_Remove.htm)| Удаляет информацию
по имени приложения для заданного имени файла, запускающего приложение.  
[Resolve](M_Tessa_Platform_ProcessNameResolver_Resolve.htm)|  Возвращает имя
приложения, пригодное для отображению пользователю. Если подходящего имени не
было найдено, то возвращает значение параметра executableName.  
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
[Resolve](M_Tessa_Platform_PlatformExtensions_Resolve.htm)|  Возвращает имя
процесса, пригодное для отображения пользователю.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
