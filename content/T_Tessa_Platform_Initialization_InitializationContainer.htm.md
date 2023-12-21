# InitializationContainer - класс
Объект, содержащий информацию, заполняемую при инициализации приложения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class InitializationContainer : IInitializationContainer
VB __Копировать
     Public NotInheritable Class InitializationContainer
    	Implements IInitializationContainer
C++ __Копировать
     public ref class InitializationContainer sealed : IInitializationContainer
F# __Копировать
     [<SealedAttribute>]
    type InitializationContainer = 
        class
            interface IInitializationContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ InitializationContainer
Implements
    [IInitializationContainer](T_Tessa_Platform_Initialization_IInitializationContainer.htm)
##  __Конструкторы
[InitializationContainer](M_Tessa_Platform_Initialization_InitializationContainer__ctor.htm)|
Инициализирует новый экземпляр класса InitializationContainer  
---|---  
##  __Свойства
[CipherInfo](P_Tessa_Platform_Initialization_InitializationContainer_CipherInfo.htm)|
Объект, содержащий настройки по шифрованию клиентских данных для текущего
пользователя. Может быть равен null, если настройки не получены с сервера.  
---|---  
[ConfigurationCacheIsActual](P_Tessa_Platform_Initialization_InitializationContainer_ConfigurationCacheIsActual.htm)|
Признак того, что конфигурация в локальном кэше была актуальна на момент
запуска приложения.  
[ConfigurationInfo](P_Tessa_Platform_Initialization_InitializationContainer_ConfigurationInfo.htm)|
Информация по конфигурации, полученная с сервера в процессе инициализации.  
[Dbms](P_Tessa_Platform_Initialization_InitializationContainer_Dbms.htm)|
Используемая СУБД.  
[DefaultColors](P_Tessa_Platform_Initialization_InitializationContainer_DefaultColors.htm)|
Цвета палитры, настроенные по умолчанию для всех пользователей.  
[Info](P_Tessa_Platform_Initialization_InitializationContainer_Info.htm)|
Дополнительная информация для расширений.  
[IsInitialized](P_Tessa_Platform_Initialization_InitializationContainer_IsInitialized.htm)|
Признак того, что инициализация была выполнена, и свойства объекта заполнены.  
[PersonalRoleSatellite](P_Tessa_Platform_Initialization_InitializationContainer_PersonalRoleSatellite.htm)|
Карточка-сателлит для персональной роли пользователя.  
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
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
