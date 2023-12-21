# Tessa.Web - пространство имён
API для сервера приложений на ASP.NET Core.
##  __Классы
[DisableFormValueModelBindingAttribute](T_Tessa_Web_DisableFormValueModelBindingAttribute.htm)|  
---|---  
[SessionMethodAttribute](T_Tessa_Web_SessionMethodAttribute.htm)|  Указывает,
что метод поддерживает сессию Tessa для проверки доступа и для передачи
информации о клиенте.  
[SessionTokenAttribute](T_Tessa_Web_SessionTokenAttribute.htm)|  Указывает,
что параметр типа
[String](https://learn.microsoft.com/dotnet/api/system.string) содержит
сериализованный токен
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm). Атрибут следует
задать для параметра метода в интерфейсе контракта, если сервис используется в
WCF, или для параметра метода контроллера, если сервис используется в ASP.NET
Core.  
[WebExtensions](T_Tessa_Web_WebExtensions.htm)|  
[WebHelper](T_Tessa_Web_WebHelper.htm)|  
[WebListenEndPoint](T_Tessa_Web_WebListenEndPoint.htm)|  Информация по точке
прослушивания для Kestrel.  
[WebServerLimits](T_Tessa_Web_WebServerLimits.htm)|  Ограничения веб-сервера
TESSA. Обычно содержатся в файле app.json и доступны по свойству
[Configuration](P_Tessa_Web_WebServerLimits_Configuration.htm). Конструктор по
умолчанию создаёт объект, в котором все свойства имеют рекомендованные
значения по умолчанию.  
[WebServerOptions](T_Tessa_Web_WebServerOptions.htm)|  Настройки веб-сервера
TESSA, используемого для Kestrel. Обычно содержатся в файле app.json и
доступны по свойству
[Configuration](P_Tessa_Web_WebServerOptions_Configuration.htm). Конструктор
по умолчанию создаёт объект, в котором все свойства имеют рекомендованные
значения по умолчанию.  
[WebStartupBase](T_Tessa_Web_WebStartupBase.htm)|  
## __Структуры
[EndPointsResult](T_Tessa_Web_EndPointsResult.htm)|  
---|---  
## __Перечисления
[HttpsRedirectMode](T_Tessa_Web_HttpsRedirectMode.htm)|  Режим редиректа с
протокола HTTP на endpoint с протоколом HTTPS.  
---|---  
[WebListenMode](T_Tessa_Web_WebListenMode.htm)|  Способ прослушивания конечных
точек (endpoints) в Kestrel.
