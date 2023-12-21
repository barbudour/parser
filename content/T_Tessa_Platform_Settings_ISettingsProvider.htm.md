# ISettingsProvider - интерфейс
Объект, предоставляющий доступ к объекту с настройками из любого потока. К
объекту возможно безопасное обращение из нескольких потоков.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISettingsProvider
VB __Копировать
     Public Interface ISettingsProvider
C++ __Копировать
     public interface class ISettingsProvider
F# __Копировать
     type ISettingsProvider = interface end
##  __Методы
[GetSettingsAsync](M_Tessa_Platform_Settings_ISettingsProvider_GetSettingsAsync.htm)|
Возвращает настройки расширений. Возвращаемое значение не равно null. При
первом обращении выполняет инициализацию настроек. Если при инициализации
возникли ошибки, то выбрасывается исключение.  
---|---  
[InvalidateAsync](M_Tessa_Platform_Settings_ISettingsProvider_InvalidateAsync.htm)|
Удаляет закэшированные настройки так, что при следующем обращении к настройкам
будет выполнена их инициализация.  
## __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
