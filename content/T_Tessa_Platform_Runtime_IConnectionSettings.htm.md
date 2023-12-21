# IConnectionSettings - интерфейс
Настройки для подключения к сервисам Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConnectionSettings : ISealable
VB __Копировать
     Public Interface IConnectionSettings
    	Inherits ISealable
C++ __Копировать
     public interface class IConnectionSettings : ISealable
F# __Копировать
     type IConnectionSettings = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[BaseAddress](P_Tessa_Platform_Runtime_IConnectionSettings_BaseAddress.htm)|
Базовый адрес сервисов.  
---|---  
[CloseTimeout](P_Tessa_Platform_Runtime_IConnectionSettings_CloseTimeout.htm)|
Таймаут на закрытие соединения с сервером.  
[InstanceName](P_Tessa_Platform_Runtime_IConnectionSettings_InstanceName.htm)|
Имя экземпляра.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[OpenTimeout](P_Tessa_Platform_Runtime_IConnectionSettings_OpenTimeout.htm)|
Таймаут на открытие соединения с сервером.  
[Proxy](P_Tessa_Platform_Runtime_IConnectionSettings_Proxy.htm)| Прокси-объект
для взаимодействия по сети.  
[SendTimeout](P_Tessa_Platform_Runtime_IConnectionSettings_SendTimeout.htm)|
Таймаут на отправку данных на сервер.  
[ServerCode](P_Tessa_Platform_Runtime_IConnectionSettings_ServerCode.htm)|
Код сервера или null, если код сервера не используется. Необязательный
параметр, может использоваться, например, при отображении кода сервера в
процессе логина в приложении ApplicationManager.  
[SkipWinAuth](P_Tessa_Platform_Runtime_IConnectionSettings_SkipWinAuth.htm)|
Признак того, что при незаданных параметрах логина/пароля пропускается попытка
Windows-аутентификации.  
## __Методы
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
