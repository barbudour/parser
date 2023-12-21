# ApplicationDescriptor - класс
Объект, описывающий текущее приложение, которое определяется по клиентской
сессии [ISession](T_Tessa_Platform_Runtime_ISession.htm). Объект недоступен на
сервере. Инициализация объекта при обращении к его свойствам является
потокобезопасной.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationDescriptor : IApplicationDescriptor
VB __Копировать
     Public NotInheritable Class ApplicationDescriptor
    	Implements IApplicationDescriptor
C++ __Копировать
     public ref class ApplicationDescriptor sealed : IApplicationDescriptor
F# __Копировать
     [<SealedAttribute>]
    type ApplicationDescriptor = 
        class
            interface IApplicationDescriptor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationDescriptor
Implements
    [IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
##  __Конструкторы
[ApplicationDescriptor](M_Tessa_Platform_Runtime_ApplicationDescriptor__ctor.htm)|
Создаёт экземпляр класса с указанием клиентской сессии.  
---|---  
## __Свойства
[Alias](P_Tessa_Platform_Runtime_ApplicationDescriptor_Alias.htm)|  Алиас
приложения, который может использоваться для формирования пути к папкам
приложения или в ссылках, или null, если алиас неизвестен.  
---|---  
[ApplicationFolder](P_Tessa_Platform_Runtime_ApplicationDescriptor_ApplicationFolder.htm)|
Путь к папке, из которой запущено приложение.  
[ApplicationVersion](P_Tessa_Platform_Runtime_ApplicationDescriptor_ApplicationVersion.htm)|
Версия приложения.  
[CacheFolder](P_Tessa_Platform_Runtime_ApplicationDescriptor_CacheFolder.htm)|
Путь к папке, из которой запущено приложение.  
[EntryAssembly](P_Tessa_Platform_Runtime_ApplicationDescriptor_EntryAssembly.htm)|
Сборка, которая была определена как сборка, запустившая приложение. Значение
не равно null.  
[Icon](P_Tessa_Platform_Runtime_ApplicationDescriptor_Icon.htm)|  Иконка
приложения или null, если иконка недоступна. Обычно иконка всегда доступна,
т.к. при невозможности получить иконку из внешнего файла, она загружается из
ресурсов сборки или же используется иконка по умолчанию.  
[Name](P_Tessa_Platform_Runtime_ApplicationDescriptor_Name.htm)| Имя
приложения.  
[SettingsFolder](P_Tessa_Platform_Runtime_ApplicationDescriptor_SettingsFolder.htm)|
Путь к папке с настройками приложения.  
##  __Методы
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
##  __События
[Initializing](E_Tessa_Platform_Runtime_ApplicationDescriptor_Initializing.htm)|
Событие, выполняющее инициализацию параметров приложения через свойства в
аргументах событий, в т.ч. на основании конфигурационных файлов и настроек,
полученных от Tessa Applications.  
---|---  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetNameWithBitness](M_Tessa_Platform_Runtime_RuntimeExtensions_GetNameWithBitness.htm)|
Возвращает имя приложения с суффиксом, указывающим на его 64-битность (если
процесс 64-битный).  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[InitializeByDefault](M_Tessa_UI_UIExtensions_InitializeByDefault.htm)|
Добавляет обработчик события для инициализации дескриптора приложения. Метод
можно безопасно вызывать несколько раз.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[RemoveDefaultInitialization](M_Tessa_UI_UIExtensions_RemoveDefaultInitialization.htm)|
Удаляет обработчик события, добавленный методом
[InitializeByDefault(IApplicationDescriptor)](M_Tessa_UI_UIExtensions_InitializeByDefault.htm).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
