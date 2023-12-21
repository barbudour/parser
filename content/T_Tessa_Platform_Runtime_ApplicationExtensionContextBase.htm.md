# ApplicationExtensionContextBase - класс
Базовый интерфейс для событий, связанных с приложением, таких как
открытие/закрытие приложения и его инициализация.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ApplicationExtensionContextBase : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public MustInherit Class ApplicationExtensionContextBase
    	Implements IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public ref class ApplicationExtensionContextBase abstract : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
F# __Копировать
     [<AbstractClassAttribute>]
    type ApplicationExtensionContextBase = 
        class
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationExtensionContextBase
Derived
[Tessa.Platform.Initialization.InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm)
[Tessa.Platform.Runtime.ApplicationExtensionContext](T_Tessa_Platform_Runtime_ApplicationExtensionContext.htm)
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Заметки
Наследники класса могут добавлять дополнительные свойства и реализовывать
интерфейсы.
## __Конструкторы
[ApplicationExtensionContextBase](M_Tessa_Platform_Runtime_ApplicationExtensionContextBase__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
---|---  
[CancellationToken](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[EnableTracing](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[Info](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
[Session](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
[ValidationResult](P_Tessa_Platform_Runtime_ApplicationExtensionContextBase_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
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
