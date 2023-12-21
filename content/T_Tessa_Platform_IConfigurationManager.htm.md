# IConfigurationManager - интерфейс
Объект, управляющий конфигурацией приложений Tessa. К объекту возможно
одновременное обращение из нескольких потоков.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConfigurationManager
VB __Копировать
     Public Interface IConfigurationManager
C++ __Копировать
     public interface class IConfigurationManager
F# __Копировать
     type IConfigurationManager = interface end
##  __Свойства
[Configuration](P_Tessa_Platform_IConfigurationManager_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[DefinedSymbols](P_Tessa_Platform_IConfigurationManager_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Errors](P_Tessa_Platform_IConfigurationManager_Errors.htm)| Ошибки, которые
возникли при разборе файлов конфигурации сервера.  
##  __Методы расширения
[TryGetConfigurationException](M_Tessa_Platform_PlatformExtensions_TryGetConfigurationException.htm)|
Возвращает исключение, описывающее все ошибки, которые произошли при
инициализации конфигурации, или null, если ошибок не было. Такое исключение
можно выбросить, чтобы передать больше информации о проблеме с конфигурацией.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
