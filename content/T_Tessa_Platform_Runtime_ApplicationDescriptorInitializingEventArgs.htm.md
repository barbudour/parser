# ApplicationDescriptorInitializingEventArgs - класс
Аргументы события
[Initializing](E_Tessa_Platform_Runtime_IApplicationDescriptor_Initializing.htm),
выполняющего инициализацию параметров приложения через свойства в аргументах
событий, в т.ч. на основании конфигурационных файлов и настроек, полученных от
Tessa Applications.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationDescriptorInitializingEventArgs : EventArgs
VB __Копировать
     Public NotInheritable Class ApplicationDescriptorInitializingEventArgs
    	Inherits EventArgs
C++ __Копировать
     public ref class ApplicationDescriptorInitializingEventArgs sealed : public EventArgs
F# __Копировать
     [<SealedAttribute>]
    type ApplicationDescriptorInitializingEventArgs = 
        class
            inherit EventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __ ApplicationDescriptorInitializingEventArgs
##  __Конструкторы
[ApplicationDescriptorInitializingEventArgs](M_Tessa_Platform_Runtime_ApplicationDescriptorInitializingEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[EntryAssembly](P_Tessa_Platform_Runtime_ApplicationDescriptorInitializingEventArgs_EntryAssembly.htm)|
Сборка, используемая в качестве точки входа в приложение. Не равна null.  
---|---  
[Icon](P_Tessa_Platform_Runtime_ApplicationDescriptorInitializingEventArgs_Icon.htm)|
Иконка приложения или null, если иконка не определена и будет использоваться
иконка по умолчанию.  
[Name](P_Tessa_Platform_Runtime_ApplicationDescriptorInitializingEventArgs_Name.htm)|
Имя приложения, используемое для отображения в интерфейсе. По умолчанию имя
определяется по информации из текущей сборки .exe.  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
