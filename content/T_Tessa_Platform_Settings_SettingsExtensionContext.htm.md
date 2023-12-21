# SettingsExtensionContext - класс
Контекст расширений для настройки расширений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SettingsExtensionContext : ISettingsExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public Class SettingsExtensionContext
    	Implements ISettingsExtensionContext, IExtensionContext
C++ __Копировать
     public ref class SettingsExtensionContext : ISettingsExtensionContext, 
    	IExtensionContext
F# __Копировать
     type SettingsExtensionContext = 
        class
            interface ISettingsExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ISettingsExtensionContext](T_Tessa_Platform_Settings_ISettingsExtensionContext.htm)
##  __Заметки
Наследники класса могут добавлять свойства.
## __Конструкторы
[SettingsExtensionContext](M_Tessa_Platform_Settings_SettingsExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Platform_Settings_SettingsExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[DbScope](P_Tessa_Platform_Settings_SettingsExtensionContext_DbScope.htm)|
Объект, предоставляющий доступ к базе данных, или null, если настройки
формируются на клиенте.  
[Info](P_Tessa_Platform_Settings_SettingsExtensionContext_Info.htm)|
Дополнительная информация для передачи между расширениями в цепочке
расширений. Информация не сохраняется после завершения инициализации настроек.  
[Session](P_Tessa_Platform_Settings_SettingsExtensionContext_Session.htm)|
Сессия пользователя.  
[Settings](P_Tessa_Platform_Settings_SettingsExtensionContext_Settings.htm)|
Настройки расширений, инициализация которых выполняется.  
[ValidationResult](P_Tessa_Platform_Settings_SettingsExtensionContext_ValidationResult.htm)|
Результат валидации. Добавьте сюда сообщение об ошибке, чтобы процесс
построения настроек завершился исключением. Предупреждения и информационные
сообщения отображаются только в логе.  
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
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
