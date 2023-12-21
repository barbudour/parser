# WebServerLimits - класс
Ограничения веб-сервера TESSA. Обычно содержатся в файле app.json и доступны
по свойству [Configuration](P_Tessa_Web_WebServerLimits_Configuration.htm).
Конструктор по умолчанию создаёт объект, в котором все свойства имеют
рекомендованные значения по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebServerLimits
VB __Копировать
     Public NotInheritable Class WebServerLimits
C++ __Копировать
     public ref class WebServerLimits sealed
F# __Копировать
     [<SealedAttribute>]
    type WebServerLimits = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebServerLimits
##  __Конструкторы
[WebServerLimits](M_Tessa_Web_WebServerLimits__ctor.htm)| Инициализирует новый
экземпляр класса WebServerLimits  
---|---  
##  __Свойства
[Configuration](P_Tessa_Web_WebServerLimits_Configuration.htm)|  Объект
настроек, загруженный из конфигурации app.json.  
---|---  
[KeepAliveTimeoutSeconds](P_Tessa_Web_WebServerLimits_KeepAliveTimeoutSeconds.htm)|
Таймаут в секундах на поддержание соединения (т.н. keep alive). По умолчанию
120 секунд.  
[MaxConcurrentConnections](P_Tessa_Web_WebServerLimits_MaxConcurrentConnections.htm)|
Максимальное количество одновременно открытых соединений. Укажите null, чтобы
не ограничивать количество соединений. По умолчанию указано null.  
[MaxConcurrentUpgradedConnections](P_Tessa_Web_WebServerLimits_MaxConcurrentUpgradedConnections.htm)|
Максимальное количество одновременно открытых соединений, которые были
обновлены для использования другого протокола (например, на WebSockets).
Укажите null, чтобы не ограничивать количество соединений. По умолчанию
указано null.  
[MaxRequestBodySizeBytes](P_Tessa_Web_WebServerLimits_MaxRequestBodySizeBytes.htm)|
Максимальный размер в байтах для тела HTTP запроса. По умолчанию 28.6 МиБ (30
000 000 байт). Ограничено отключено для методов с потоковой передачей (такой
как сохранение карточки с файлами или импорт библиотек локализации), а также
для методов контроллеров, реализованных в рамках проекта, в которых задан
атрибут DisableRequestSizeLimit.  
[MaxRequestBufferSizeBytes](P_Tessa_Web_WebServerLimits_MaxRequestBufferSizeBytes.htm)|
Максимальный размер буфера в байтах для запроса. По умолчанию 1 МиБ (1 048 576
байт). Укажите null, чтобы не ограничивать размер буфера.  
[MaxRequestHeaderCount](P_Tessa_Web_WebServerLimits_MaxRequestHeaderCount.htm)|
Максимальное количество заголовков в HTTP запросе. По умолчанию 100
заголовков.  
[MaxRequestHeadersTotalSizeBytes](P_Tessa_Web_WebServerLimits_MaxRequestHeadersTotalSizeBytes.htm)|
Максимальный совокупный размер заголовков в HTTP запросе. По умолчанию 32 КиБ
(32 768 байт).  
[MaxRequestLineSizeBytes](P_Tessa_Web_WebServerLimits_MaxRequestLineSizeBytes.htm)|
Максимальный размер строки запроса HTTP. По умолчанию 8 КиБ (8 192 байт).  
[MaxResponseBufferSizeBytes](P_Tessa_Web_WebServerLimits_MaxResponseBufferSizeBytes.htm)|
Максимальный размер буфера в байтах для ответа на запрос перед тем, как
начинается отправка по сети. По умолчанию 64 КиБ (65 536 байт). Укажите null,
чтобы не ограничивать размер буфера. Укажите 0, чтобы не использовать
буферизацию перед отправкой.  
[MinRequestBodyDataRateBytesPerSecond](P_Tessa_Web_WebServerLimits_MinRequestBodyDataRateBytesPerSecond.htm)|
Средняя скорость передачи, измеряемая в байтах в секунду, в течение интервала
времени
[MinRequestBodyDataRateGraceSeconds](P_Tessa_Web_WebServerLimits_MinRequestBodyDataRateGraceSeconds.htm),
которая минимально допустима для получения данных HTTP запроса от клиента. По
умолчанию 240 байт в секунду.  
[MinRequestBodyDataRateGraceSeconds](P_Tessa_Web_WebServerLimits_MinRequestBodyDataRateGraceSeconds.htm)|
Интервал времени в секундах, для которого измеряется средняя скорость
получения данных HTTP запроса от клиента
[MinRequestBodyDataRateBytesPerSecond](P_Tessa_Web_WebServerLimits_MinRequestBodyDataRateBytesPerSecond.htm).
По умолчанию 5 секунд.  
[MinResponseDataRateBytesPerSecond](P_Tessa_Web_WebServerLimits_MinResponseDataRateBytesPerSecond.htm)|
Средняя скорость передачи, измеряемая в байтах в секунду, в течение интервала
времени
[MinResponseDataRateGraceSeconds](P_Tessa_Web_WebServerLimits_MinResponseDataRateGraceSeconds.htm),
которая минимально допустима для отправки данных HTTP ответа. По умолчанию 240
байт в секунду.  
[MinResponseDataRateGraceSeconds](P_Tessa_Web_WebServerLimits_MinResponseDataRateGraceSeconds.htm)|
Интервал времени в секундах, для которого измеряется средняя скорость отправки
данных HTTP ответа
[MinResponseDataRateBytesPerSecond](P_Tessa_Web_WebServerLimits_MinResponseDataRateBytesPerSecond.htm).
По умолчанию 5 секунд.  
[RequestHeadersTimeoutSeconds](P_Tessa_Web_WebServerLimits_RequestHeadersTimeoutSeconds.htm)|
Максимальное время в секундах, в течение которого сервер ожидает получения
HTTP заголовков. По умолчанию 30 секунд.  
## __Методы
[Apply](M_Tessa_Web_WebServerLimits_Apply.htm)|  Применяет настройки в текущем
объекте к веб-серверу Kestrel.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromConfiguration(Dictionary<String,
Object>)](M_Tessa_Web_WebServerLimits_FromConfiguration.htm)|  Создаёт объект
настроек по заданному объекту с хеш-таблицей. По ключу "WebServerLimits" в
этой хеш-таблице должны быть настройки. Имена настроек соотносятся с именами
свойств текущего объекта.  
[FromConfiguration(IConfigurationManager)](M_Tessa_Web_WebServerLimits_FromConfiguration_1.htm)|
Создаёт объект настроек по заданному объекту конфигурации. В нём по свойству
configurationManager.Configuration.Settings доступна хеш-таблица, в которой
есть ключ "WebServerLimits", содержащий настройки. Имена настроек соотносятся
с именами свойств текущего объекта.  
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
[SetFrom](M_Tessa_Web_WebServerLimits_SetFrom.htm)|  Устанавливает свойства
класса в соответствии с переданным объектом.  
[ToString](M_Tessa_Web_WebServerLimits_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Web - пространство имён](N_Tessa_Web.htm)
