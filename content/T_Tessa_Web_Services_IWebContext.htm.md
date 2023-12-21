# IWebContext - интерфейс
Контекст обработки на веб-сервере.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWebContext
VB __Копировать
     Public Interface IWebContext
C++ __Копировать
     public interface class IWebContext
F# __Копировать
     type IWebContext = interface end
##  __Методы
[SetLocalizationService](M_Tessa_Web_Services_IWebContext_SetLocalizationService.htm)|
Метод для установки
[ILocalizationService](T_Tessa_Localization_ILocalizationService.htm) в
контекст в качестве текущего сервиса локализации.  
---|---  
[SetSessionToken](M_Tessa_Web_Services_IWebContext_SetSessionToken.htm)|
Метод для установки
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) в контекст в
качестве текущего токена, содержащего информацию о сессии.  
[TryGetLocalizationService](M_Tessa_Web_Services_IWebContext_TryGetLocalizationService.htm)|
Возвращает текущий сервис локализации, установленный через
[SetLocalizationService(ILocalizationService)](M_Tessa_Web_Services_IWebContext_SetLocalizationService.htm),
или null, если сервис локализации не установлен.  
[TryGetSessionToken](M_Tessa_Web_Services_IWebContext_TryGetSessionToken.htm)|
Возвращает текущий токен, содержащий информацию о сессии, установленный через
[SetSessionToken(ISessionToken)](M_Tessa_Web_Services_IWebContext_SetSessionToken.htm),
или null, если токен не установлен.  
## __См. также
#### Ссылки
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
