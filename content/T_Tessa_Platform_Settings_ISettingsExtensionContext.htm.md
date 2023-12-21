# ISettingsExtensionContext - интерфейс
Контекст расширений для настройки расширений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISettingsExtensionContext : IExtensionContext
VB __Копировать
     Public Interface ISettingsExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class ISettingsExtensionContext : IExtensionContext
F# __Копировать
     type ISettingsExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[DbScope](P_Tessa_Platform_Settings_ISettingsExtensionContext_DbScope.htm)|
Объект, предоставляющий доступ к базе данных, или null, если настройки
формируются на клиенте.  
[Info](P_Tessa_Platform_Settings_ISettingsExtensionContext_Info.htm)|
Дополнительная информация для передачи между расширениями в цепочке
расширений. Информация не сохраняется после завершения инициализации настроек.  
[Session](P_Tessa_Platform_Settings_ISettingsExtensionContext_Session.htm)|
Сессия пользователя.  
[Settings](P_Tessa_Platform_Settings_ISettingsExtensionContext_Settings.htm)|
Настройки расширений, инициализация которых выполняется.  
[ValidationResult](P_Tessa_Platform_Settings_ISettingsExtensionContext_ValidationResult.htm)|
Результат валидации. Добавьте сюда сообщение об ошибке, чтобы процесс
построения настроек завершился исключением. Предупреждения и информационные
сообщения отображаются только в логе.  
## __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
