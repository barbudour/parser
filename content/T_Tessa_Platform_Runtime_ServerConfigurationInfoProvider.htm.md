# ServerConfigurationInfoProvider - класс
Объект, предоставляющий информацию по текущей конфигурации на сервере из базы
данных.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ServerConfigurationInfoProvider : IConfigurationInfoProvider
VB __Копировать
     Public NotInheritable Class ServerConfigurationInfoProvider
    	Implements IConfigurationInfoProvider
C++ __Копировать
     public ref class ServerConfigurationInfoProvider sealed : IConfigurationInfoProvider
F# __Копировать
     [<SealedAttribute>]
    type ServerConfigurationInfoProvider = 
        class
            interface IConfigurationInfoProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServerConfigurationInfoProvider
Implements
    [IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
##  __Конструкторы
[ServerConfigurationInfoProvider](M_Tessa_Platform_Runtime_ServerConfigurationInfoProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
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
[GetFlags](M_Tessa_Platform_Runtime_ServerConfigurationInfoProvider_GetFlags.htm)|
Возвращает информацию по специальным режимам конфигурации, настраиваемым в
конфигурационном файле сервера.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInfoAsync](M_Tessa_Platform_Runtime_ServerConfigurationInfoProvider_GetInfoAsync.htm)|
Возвращает информацию по текущей конфигурации. Если информацию не удаётся
получить, из-за отсутствия данных или возникших исключений, то возвращает
ConfigurationInfo.Unknown. Возвращённое значение не равно null.  
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
[CheckSealed](M_Tessa_Platform_Runtime_RuntimeExtensions_CheckSealed.htm)|
Выбрасывает исключение
[ConfigurationSealedException](T_Tessa_Platform_Runtime_ConfigurationSealedException.htm),
если система находится в режиме защиты от изменений в конфигурации
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[CheckStrictSecurity](M_Tessa_Platform_Runtime_RuntimeExtensions_CheckStrictSecurity.htm)|
Выбрасывает исключение
[ConfigurationStrictSecurityException](T_Tessa_Platform_Runtime_ConfigurationStrictSecurityException.htm),
если система находится в режиме защиты повышенной безопасности в конфигурации
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
