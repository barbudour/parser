# IConfigurationInfoProvider - интерфейс
Объект, предоставляющий информацию по текущей конфигурации.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConfigurationInfoProvider
VB __Копировать
     Public Interface IConfigurationInfoProvider
C++ __Копировать
     public interface class IConfigurationInfoProvider
F# __Копировать
     type IConfigurationInfoProvider = interface end
##  __Методы
[GetFlags](M_Tessa_Platform_Runtime_IConfigurationInfoProvider_GetFlags.htm)|
Возвращает информацию по специальным режимам конфигурации, настраиваемым в
конфигурационном файле сервера.  
---|---  
[GetInfoAsync](M_Tessa_Platform_Runtime_IConfigurationInfoProvider_GetInfoAsync.htm)|
Возвращает информацию по текущей конфигурации. Если информацию не удаётся
получить, из-за отсутствия данных или возникших исключений, то возвращает
ConfigurationInfo.Unknown. Возвращённое значение не равно null.  
## __Методы расширения
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
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
