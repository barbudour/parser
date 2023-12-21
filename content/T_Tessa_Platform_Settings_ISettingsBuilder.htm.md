# ISettingsBuilder - интерфейс
Объект, выполняющий построение объекта с настройками расширений
[ISettings](T_Tessa_Platform_Settings_ISettings.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISettingsBuilder
VB __Копировать
     Public Interface ISettingsBuilder
C++ __Копировать
     public interface class ISettingsBuilder
F# __Копировать
     type ISettingsBuilder = interface end
##  __Методы
[TryBuildAsync](M_Tessa_Platform_Settings_ISettingsBuilder_TryBuildAsync.htm)|
Выполняет построение объекта настроек. Возвращает null в качестве объекта
настроек, если объект не удалось построить. Вторым значением возвращает
результат валидации, который может содержать сообщения об ошибках.  
---|---  
## __Методы расширения
[BuildAsync](M_Tessa_Platform_Settings_SettingsExtensions_BuildAsync.htm)|
Выполняет построение объекта настроек. Возвращаемое значение гарантированно не
равно null. Выбрасывает исключение при невозможности его построить.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
