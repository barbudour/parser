# SettingsBuilder - класс
Объект, выполняющий построение объекта с настройками расширений
[ISettings](T_Tessa_Platform_Settings_ISettings.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SettingsBuilder : ISettingsBuilder
VB __Копировать
     Public Class SettingsBuilder
    	Implements ISettingsBuilder
C++ __Копировать
     public ref class SettingsBuilder : ISettingsBuilder
F# __Копировать
     type SettingsBuilder = 
        class
            interface ISettingsBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsBuilder
Implements
    [ISettingsBuilder](T_Tessa_Platform_Settings_ISettingsBuilder.htm)
##  __Заметки
Наследники класса могут переопределять protected-методы.
## __Конструкторы
[SettingsBuilder](M_Tessa_Platform_Settings_SettingsBuilder__ctor.htm)|
Создаёт экземпляр класса с указанием используемых зависимостей.  
---|---  
## __Свойства
[DbScope](P_Tessa_Platform_Settings_SettingsBuilder_DbScope.htm)|  Объект,
предоставляющий доступ к базе данных, или null, если настройки формируются на
клиенте.  
---|---  
[ExtensionContainer](P_Tessa_Platform_Settings_SettingsBuilder_ExtensionContainer.htm)|
Контейнер с расширениями
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm) для
инициализации настроек.  
[Session](P_Tessa_Platform_Settings_SettingsBuilder_Session.htm)|  Сессия
пользователя.  
## __Методы
[CreateContext](M_Tessa_Platform_Settings_SettingsBuilder_CreateContext.htm)|
Создаёт и возвращает контекст расширений.  
---|---  
[CreateSettings](M_Tessa_Platform_Settings_SettingsBuilder_CreateSettings.htm)|
Создаёт и возвращает настройки, формируемые текущим объектом.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryBuildAsync](M_Tessa_Platform_Settings_SettingsBuilder_TryBuildAsync.htm)|
Выполняет построение объекта настроек. Возвращает null в качестве объекта
настроек, если объект не удалось построить. Вторым значением возвращает
результат валидации, который может содержать сообщения об ошибках.  
## __Методы расширения
[BuildAsync](M_Tessa_Platform_Settings_SettingsExtensions_BuildAsync.htm)|
Выполняет построение объекта настроек. Возвращаемое значение гарантированно не
равно null. Выбрасывает исключение при невозможности его построить.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
---|---  
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
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
