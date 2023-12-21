# IRuntimeSettings - интерфейс
Настройки, связанные с исполняющей средой системы.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRuntimeSettings
VB __Копировать
     Public Interface IRuntimeSettings
C++ __Копировать
     public interface class IRuntimeSettings
F# __Копировать
     type IRuntimeSettings = interface end
##  __Свойства
[MultipleInstances](P_Tessa_Platform_Runtime_IRuntimeSettings_MultipleInstances.htm)|
Признак того, что активен режим работы с несколькими экземплярами сервера. При
этом в запросах к серверу обязательно передаётся InstanceName, в т.ч. для
ссылок на web-клиент.  
---|---  
[QuietMode](P_Tessa_Platform_Runtime_IRuntimeSettings_QuietMode.htm)|  Признак
того, что приложение запускается в тихом режиме, т.е. любой вывод будет только
в лог, а ввод запрещён. По умолчанию false.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
